from dotenv import load_dotenv
import os
import logging
import subprocess
import telegram

from telegram import ParseMode
from telegram.ext import Updater
from subprocess import run

load_dotenv('config.env')
TOKEN = os.environ['TOKEN']
TARGET_ID = os.environ['TARGET_CHAT_ID']

LOGGER = logging.getLogger(__name__)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s:  %(message)s',level=logging.INFO)
logging.info("\U0001F7E2 BOT ONLINE!")

#Notification with Chat emoji
telegram.Bot(token=TOKEN).sendMessage(chat_id=TARGET_ID, text="\U0001F4AC BOT ONLINE!")
#Notification with Green Dot emoji
#telegram.Bot(token=TOKEN).sendMessage(chat_id=TARGET_ID, text="\U0001F7E2 BOT ONLINE!")

def cd(update, context):
     message = update.effective_message
     cmd = message.text.split(' ', 1)
     if len(cmd) == 1:
         message.reply_text('Missing command')
         return
     else:
         cmd = cmd[1]
         try:
             os.chdir(cmd)
             message.reply_text("Current Path:\n"+os.getcwd(), parse_mode=ParseMode.MARKDOWN)
         except OSError:
             message.reply_text("ERROR: Directory does not exists", parse_mode=ParseMode.MARKDOWN)


def mkdir(update, context):
     message = update.effective_message
     cmd = message.text.split(' ', 1)
     if len(cmd) == 1:
         message.reply_text('Missing command')
         return
     cmd = cmd[1]
     os.makedirs(cmd, exist_ok=True)
     message.reply_text("Directory created", parse_mode=ParseMode.MARKDOWN)


def r(update,context):
    message = update.effective_message
    cmd = message.text.split(' ', 1)
    if len(cmd) == 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No command to execute was given.')
        #return sendMessage('No command to execute was given.', context.bot, update.message)
    cmd = cmd[1]
    process = run(cmd, capture_output=True, shell=True)
    reply = ''
    stderr = process.stderr.decode('utf-8')
    stdout = process.stdout.decode('utf-8')
    if len(stdout) != 0:
        reply += f"*Output*\n`{stdout}`\n"
        LOGGER.info(f"Shell - {cmd}\n{stdout}")
    if len(stderr) != 0:
        reply += f"*Error*\n`{stderr}`\n"
        LOGGER.error(f"Shell - {cmd}\n{stderr}")
    if len(reply) > 3000:
        with open('shell_output.txt', 'w') as file:
            file.write(reply)
        with open('shell_output.txt', 'rb') as doc:
            context.bot.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id)
    elif len(reply) != 0:
        message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


def getfile(update,context):
	chat_id=update.effective_chat.id
	context.bot.send_document(chat_id=chat_id ,document=open(context.args[0],'rb'))

	
from telegram.ext import CommandHandler
start_handler = CommandHandler('r', r)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('cd', cd)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('mkdir', mkdir)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('getfile', getfile)
dispatcher.add_handler(start_handler)

updater.start_polling()

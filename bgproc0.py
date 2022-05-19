from dotenv import load_dotenv
import time
import requests
import os

load_dotenv('config.env')
url = os.environ["URLS"]
url = url.split(" ")
timer_lmt = int(os.environ["TIMER_LIMIT"])-1800  #Heroku will sleep IF IDEAL for 30 minutes (1800 seconds)
timer = 0

while timer < timer_lmt:
  for i in url:
    status = requests.get(i).status_code
    print(f"response of {i} = {status}")
  time.sleep(int(os.environ["INTERVAL"]))
  timer = timer + int(os.environ["INTERVAL"])

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Settings:
```bash
CLOUDFOLDER: Cloud folder path, can leave empty

INTERVAL: Interval between next ping in seconds; Default is 5 minutes

RCLONE_CONFIG_URL: Rclone config file URL

TARGET_CHAT_ID: Telegram chat ID, message @userinfobot to get ID; a notification of bot online will send to chat ID

TIMER_LIMIT: Keep website alive for how long (in seconds); Default is 14400 (4 Hours)

TOKEN: Telegram bot token, can leave empty

TRACKERS_URL: URL that contains tracker list; app will automatic download from URL then add tracker list to config file

URLS: App's URL or other URLs (used to disable webapp auto sleep function)

WEBPASSWORD: Password

WEBUSER: Username
```

## qBittorrent autorun cmd:

Current Default:
```bash
/script "%I" "%N" nofolder # Will upload contents directly to cloud's specified root folder

/script "%I" "%N" # Will upload contents based on original torrent's content respective folders
```

Previous command: ***rclone copy /Downloads/"%N" rclonedrivename:/***



## Notes:
bgproc0.py will disable auto sleep; if not require, remove ***"& python3 bgproc0.py & wait;"*** from ***heroku.yml*** file

***Atlernative: Use UptimeRobot to check site every 5 minutes (alternative)***


## Extra:
Can use ***Remote Torrent Adder*** to auto add torrent/magnet to qBittorrent

https://chrome.google.com/webstore/detail/remote-torrent-adder/oabphaconndgibllomdcjbfdghcmenci

```bash
Settings:
Type: qBittorrent WebUI
Host: yourappname.herokuapp.com
Port: 80
SSL: Uncheck
Username: yourusername
Password: yourpassword
```

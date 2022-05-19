wget -O /.config/rclone/rclone.conf $RCLONE_CONFIG_URL

#---
#Insert username, password & cloud drive name to config file
#---
sed -i 's|'rclone_drive_name'|'$(rclone listremotes |head -1)'|g' /.config/qBittorrent/qBittorrent.conf
echo >> /.config/qBittorrent/qBittorrent.conf
echo WebUI'\'Username=$WEBUSER >> /.config/qBittorrent/qBittorrent.conf
echo >> /.config/qBittorrent/qBittorrent.conf
md5hash=$(echo -n $WEBPASSWORD | md5sum | head -c 32)
echo WebUI'\'Password_ha1=@ByteArray'('$md5hash')'>> /.config/qBittorrent/qBittorrent.conf
if [ ! -z "$TRACKERS_URL" ]    #Add trackers ONLY if TRACKERS_URL provided
then
    wget -O /trackers.txt https://trackerslist.com/all.txt
    sed -i '/^$/d' /trackers.txt
    sed -z -i 's/\n/\\n/g' /trackers.txt
    (echo -n "Bittorrent\TrackersList="; cat trackers.txt) >> /.config/qBittorrent/qBittorrent.conf
fi

#---
#Insert env value to script
#---
sed -i 's|ENVVAR_CLOUDDRIVE|'$(rclone listremotes |head -1)'|g' /script
sed -i 's|ENVVAR_CLOUDFOLDER|'$CLOUDFOLDER'|g' /script

#---
#Start Bot
#---
if [ ! -z "$TOKEN" ]    #Start bot ONLY if TOKEN provided
then
    python3 bgproc1.py &
fi

while :
do
    qbittorrent-nox --webui-port=$PORT
done

#Run following cmd enable process killable from bot
#qbittorrent-nox --webui-port=$PORT &

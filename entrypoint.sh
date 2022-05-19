#!/bin/bash
mkdir -p /Downloads
mkdir -p /.config/rclone
mkdir -p /.config/tmpvar

wget -O /config.env $CONFIG_URL
echo "#!/bin/bash" > /.config/tmpvar/tempfile
echo "" >> /.config/tmpvar/tempfile  #Add new line
cat /config.env >> /.config/tmpvar/tempfile
echo "" >> /.config/tmpvar/tempfile  #Add new line
cat /start.sh >> /.config/tmpvar/tempfile
cat /.config/tmpvar/tempfile > /start.sh
rm -r /.config/tmpvar

./start.sh

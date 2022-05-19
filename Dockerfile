FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Singapore
RUN apt-get update \
    && apt-get install -y wget curl bash busybox tree unzip unrar tar iputils-ping net-tools dnsutils python3 python3-pip gunicorn qbittorrent-nox tzdata rclone git aria2
RUN pip3 install --no-cache-dir python-dotenv python-telegram-bot requests

COPY . .
RUN unzip vuetorrent.zip && rm vuetorrent.zip
RUN mkdir -p /.config/qBittorrent
RUN chmod -R 777 /.config/qBittorrent
RUN mv /qBittorrent.conf /.config/qBittorrent/qBittorrent.conf
RUN chmod +x /.config/qBittorrent/qBittorrent.conf
RUN chmod +x /script
RUN chmod +x /entrypoint.sh
RUN chmod +x /start.sh

EXPOSE 6881 6881/udp 8085

CMD /entrypoint.sh

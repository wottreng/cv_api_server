#!/bin/bash
# https://techglimpse.com/exclude-directories-when-using-tar-linux-command/
# ----------------------------
#echo -e "venv\n.git\n.gitignore\nsend_to_server.sh" > .exclude.txt
tar -cvzf project.tar -X ./server/exclude.txt ./*
#ssh root@10.42.112.19 "rm -r /server/yolo-api/*"
scp project.tar root@10.42.112.19:/server/yolo-api/
ssh root@10.42.112.19 "cd /server/yolo-api/ && tar -xvzf project.tar && systemctl restart yolo-api.service"
#
echo "sent to server"
# check server
echo "check server...."
sleep 6
resp=$(curl  "http://10.42.112.19:1300/ping")
if [ "$resp" == "pong" ]; then
    echo "server is up"
else
    echo "server is down"
fi
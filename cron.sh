#!/bin/bash
# script for creating a timelapse video with rapistill and store it in /home/pi$
# START AND END TIME ARE PUT IN CRONTAB
# the webpages used as sourced for information are listed at the end of this fi$

#touch now.txt

DATE=$(date +"%Y-%m-%d_%H-%M")
#fswebcam -r 640x480 --no-banner /home/pi/beach/$DATE.jpg

#curl -s -o /dev/null http://localhost:8080/0/action/snapshot
#sleep 1
#[ /tmp/motion/lastsnap.jpg -nt now.txt ] && cp  /tmp/motion/lastsnap.jpg /home/pi/beach/$DATE.jpg && echo "/home/pi/beach/$DATE.jpg saved"

ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i  /dev/video0 -t 00:00:10  /home/pablo/beach/$DATE.mkv
ffmpeg -sseof -1 -i /home/pablo/beach/$DATE.mkv -update 1 -q:v 1 /home/pablo/beach/$DATE.jpg

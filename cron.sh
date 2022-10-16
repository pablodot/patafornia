#!/bin/bash
# script for creating a timelapse video with rapistill and store it in /home/pi$
# START AND END TIME ARE PUT IN CRONTAB
# the webpages used as sourced for information are listed at the end of this fi$
DATE=$(date +"%Y-%m-%d_%H-%M")
sudo raspistill -o /home/pablo/beach/$DATE.jpg

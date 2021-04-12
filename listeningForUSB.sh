#!/bin/bash

MOUNT_FOLDER='/media/pi'

inotifywait --monitor --quiet --event create $MOUNT_FOLDER | \
while read event; do
	folder=$(echo $event|cut --delimiter ' ' --field 3)
	
	if [[ $folder == "AJOUT" ]]; then
		sleep 5
		source /home/pi/Documents/lectura-plus/copy_from_usb.sh
	elif [[ $folder == "SUPPR" ]]; then
		sleep 5
		source /home/pi/Documents/lectura-plus/delete_from_usb.sh
	else
		echo "clé usb non reconnue"
	fi
done

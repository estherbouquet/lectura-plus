#!/bin/bash

input_folder='/home/pi/Documents/lectura-plus/input/'

utf="utf-8"

for files in $input_folder*.txt; # for txt files in input
do
	encoding=$(file -i "$files" | sed "s/.*charset=\(.*\)$/\1/") 
	# -i display file's encoding
	# sed is a stream editor that enables you to modify text
	# the rest, idk
	
	if [ ! "$utf" == "${encoding}" ] # if the encoding is != from utf-8
	then
	echo "recoding from ${encoding} to $utf file : $files" #debug
	recode ${encoding}..$utf $files #recode file with the utf-8 encoding
	fi

done


for dir in $input_folder; # for all the folders in input
do
	for files in "$dir"*/*.txt; # and for all the txt files in those subdirectories
	do
		encoding=$(file -i "$files" | sed "s/.*charset=\(.*\)$/\1/") 
		
		if [ ! "$utf" == "${encoding}" ] # if the encoding is != from utf-8
		then
		echo "recoding from ${encoding} to $utf file : $files" # debug
		recode ${encoding}..$utf $files #recode file with the utf-8 encoding
		fi
	done
done



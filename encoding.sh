#!/bin/bash

input_folder='/home/pi/Documents/lectura-plus/input'

utf="utf-8"

for files in $input_folder/*.txt; # for txt files in input
do
	sed -i "s/\’/\'/g" $files #remplace les quotations marks en cp1252 par des apostrophes ce qui évite les problèmes réencodage cp1252>utf-8
	sed -i "s/\œ/\oe/g" $files
	sed -i "s/\—/\-/g" $files
	sed -i "s/\ /\ /g" $files
	sed -i "s/\–/\-/g" $files
	
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




#!/bin/bash

# Mettre tous les fichiers dans un sous dossier de la clé usb (genre /articles)

# usb_folder=/media/NOM_USB/lectura

if [ -d "/home/pi/Documents/lectura-plus/articles" ] # Si le dossier /articles existe dans lectura-plus
then 
	echo "Directory ./articles/ exists!"
	usb='/media/pi/KEVCHA/articles/*'
	#usb='/home/pi/Documents/lectura-plus/articles/*'
	# On crée les trois dossiers
	#mkdir '/Users/leabelzunces/code/lectura-plus/input'
	#mkdir '/Users/leabelzunces/code/lectura-plus/output'
	#mkdir '/Users/leabelzunces/code/lectura-plus/images'
	mkdir '/home/pi/Documents/lectura-plus/input'
	mkdir '/home/pi/Documents/lectura-plus/output'
	if [ ! -d "images" ] # si le dossier images n'existe pas
	then
		mkdir '/home/pi/Documents/lectura-plus/images' # on le crée
	fi
	# On les stocke dans des variables
	#input_folder='/Users/leabelzunces/code/lectura-plus/input'
	#output_folder='/Users/leabelzunces/code/lectura-plus/output'
	#images_folder='/Users/leabelzunces/code/lectura-plus/images'
	input_folder='/home/pi/Documents/lectura-plus/input/'
	output_folder='/home/pi/Documents/lectura-plus/output/'
	images_folder='home/pi/Documents/lectura-plus/images/'

	# On copie récursivement les fichiers de la clé usb dans le dossier input
	cp -r $usb $input_folder

	#On réencode les fichiers txt qui ne sont pas encodés en utf-8 en appelant le script encoding.sh
	source /home/pi/Documents/lectura-plus/encoding.sh

	# On exécute le script python qui convertit les fichiers du dossier input en HTML dans ./output puis en jpg dans ./images
	python3 file_converter.py

	# On supprime les dossiers input et output
	rm -r $input_folder
	rm -r $output_folder
	
	source /home/pi/Documents/lectura-plus/listeningForPushedButton.sh
	
else # Si usb_test n'existe pas 
	echo "Directory ./articles/ doesn't exists!"
	python3 -c 'from led import problem; problem()' # Lance la fonction problem() dans led.py (fait clignoter la led 3 fois)
fi

#!/bin/bash

if [ -d "/media/pi/AJOUT/articles" ] # Si le dossier /articles existe sur la clé AJOUT
then 
	echo "Directory ./articles/ exists!"
	usb='/media/pi/AJOUT/articles/*'
	#usb='/home/pi/Documents/lectura-plus/articles/*'
	# On crée les trois dossiers
	#mkdir '/Users/leabelzunces/code/lectura-plus/input'
	#mkdir '/Users/leabelzunces/code/lectura-plus/output'
	#mkdir '/Users/leabelzunces/code/lectura-plus/images'
	mkdir '/home/pi/Documents/lectura-plus/input'
	mkdir '/home/pi/Documents/lectura-plus/output'

	# On les stocke dans des variables
	#input_folder='/Users/leabelzunces/code/lectura-plus/input'
	#output_folder='/Users/leabelzunces/code/lectura-plus/output'
	#images_folder='/Users/leabelzunces/code/lectura-plus/images'
	input_folder='/home/pi/Documents/lectura-plus/input/'
	output_folder='/home/pi/Documents/lectura-plus/output/'
	images_folder='home/pi/Documents/lectura-plus/images/'

	python3 -c 'from led import turnOnGreen; turnOnGreen()' #Allume la led verte au début de la copie et pendant l'encoding
	echo "leds allumées"
	
	# On copie récursivement les fichiers de la clé usb dans le dossier input
	cp -r $usb $input_folder
	echo "c'est copié"
	
	#On corrige les noms de fichiers qui contiennent des espaces 
	python3 rename_bad_filenames.py
	
	#On réencode les fichiers txt qui ne sont pas encodés en utf-8 en appelant le script encoding.sh
	source /home/pi/Documents/lectura-plus/encoding.sh
	echo "encoding terminé"
	
	python3 -c 'from led import turnOnYellow; turnOnYellow()' #Allume la led blue au début de la conversion txt>HTML>images

	# On exécute le script python qui convertit les fichiers du dossier input en HTML dans ./output puis en jpg dans ./images
	python3 file_converter.py
	echo "conversion finie"
	
	python3 -c 'from led import turnOffGreen; turnOffGreen()' #Eteint la led verte 
	python3 -c 'from led import turnOffYellow; turnOffYellow()' # et la led bleue à la fin de la conversion
	python3 -c 'from led import tranferEnded; tranferEnded()' # transfert terminé avec succès
	python3 -c 'from led import cleanLed; cleanLed()' # On nettoie les ports utilisés par les leds
	echo "leds éteintes"
	
	# On supprime les dossiers input et output
	rm -r $input_folder
	rm -r $output_folder
	echo "tout est fini"
	
else # Si le dossier articles sur AJOUT n'existe pas 
	echo "Directory ./articles/ doesn't exists!"
	python3 -c 'from led import errDirMissing; errDirMissing()' # Lance la fonction errDirMissing() dans led.py (fait clignoter la led rouge)
fi

#!/bin/bash

# POUR EFFACER LES ARTICLES-IMAGES PRESENTS SUR LE RASPBERRY

if [ -f "/media/pi/SUPPR/suppression.txt" ] # si on détecte un fichier suppression.txt dans la clé SUPPR
then
	sudo rm -rf '/home/pi/Documents/lectura-plus/images' # on supprime le dossier images/ sur le raspberry
	python3 -c 'from led import dirImagesDeleted; dirImagesDeleted()' # Lance la fonction problem() dans led.py (allume les 3 led comme une guirlande)
else # Si le fichier suppression.txt n'existe pas sur SUPPR
	echo "File suppression.txt doesn't exists!"
	python3 -c 'from led import errFileMissing; errFileMissing()' # Lance la fonction errFileMissing() dans led.py (fait clignoter la led rouge)
fi

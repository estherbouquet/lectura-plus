#!/bin/bash

# POUR EFFACER LES ARTICLES-IMAGES PRESENTS SUR LE RASPBERRY

if [ -f "/media/pi/SUPPR/suppression.txt" ] # si on détecte un fichier suppression.txt dans la clé SUPPR
then
	sudo rm -rf '/home/pi/Documents/lectura-plus/images' # on supprime le dossier images/ sur le raspberry
	python3 -c 'from led import problem; problem()' # Lance la fonction problem() dans led.py (fait clignoter la led 3 fois)
fi

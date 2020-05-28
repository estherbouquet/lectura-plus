#!/bin/bash

# Mettre tous les fichiers dans un sous dossier de la clé usb (genre /articles)

# usb_folder=/media/NOM_USB/lectura
#file='/Users/leabelzunces/code/lectura-plus/test.txt'
usb='/home/pi/Documents/lectura-plus/usb_test/*'

# On crée les trois dossiers
#mkdir '/Users/leabelzunces/code/lectura-plus/input'
#mkdir '/Users/leabelzunces/code/lectura-plus/output'
#mkdir '/Users/leabelzunces/code/lectura-plus/images'
mkdir '/home/pi/Documents/lectura-plus/input'
mkdir '/home/pi/Documents/lectura-plus/output'
mkdir '/home/pi/Documents/lectura-plus/images'

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

# On exécute le script python qui convertit les fichiers du dossier input en HTML
python3 markdown_converter.py

# On exécute le script qui ouvre le fichier HTML et fait un screenshot

# python3 make_screenshot.py

# On supprime le dossier input et output
rm -rf $input_folder
rm -rf $output_folder

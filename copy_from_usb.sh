# Mettre tous les fichiers dans un sous dossier de la clé usb (genre /input)

# usb_folder=/media/NOM_USB/input
#file='/Users/leabelzunces/code/lectura-plus/test.txt'
file='/home/pi/Documents/lectura-plus-master/test.txt'

# On crée les trois dossiers
#mkdir '/Users/leabelzunces/code/lectura-plus/input'
#mkdir '/Users/leabelzunces/code/lectura-plus/output'
#mkdir '/Users/leabelzunces/code/lectura-plus/images'
mkdir '/home/pi/Documents/lectura-plus-master/input'
mkdir '/home/pi/Documents/lectura-plus-master/output'
mkdir '/home/pi/Documents/lectura-plus-master/images'

# On les stocke dans des variables
#input_folder='/Users/leabelzunces/code/lectura-plus/input'
#output_folder='/Users/leabelzunces/code/lectura-plus/output'
#images_folder='/Users/leabelzunces/code/lectura-plus/images'
input_folder='/home/pi/Documents/lectura-plus-master/input'
output_folder='/home/pi/Documents/lectura-plus-master/output'
images_folder='home/pi/Documents/lectura-plus-master/images'

# On copie les fichiers de la clé usb dans le dossier input
cp $file $input_folder

# On exécute le script python qui convertit les fichiers du dossier input en HTML
python3 markdown_converter.py

# On exécute le script qui ouvre le fichier HTML et fait un screenshot

# python3 make_screenshot.py

# On supprime le dossier input
rm -rf $input_folder

# Mettre tous les fichiers dans un sous dossier de la clé usb (genre /input)

# usb_folder=/media/NOM_USB/input
file='/Users/leabelzunces/code/lectura/test.txt'

# On crée les trois dossiers
mkdir '/Users/leabelzunces/code/lectura/input'
mkdir '/Users/leabelzunces/code/lectura/output'
mkdir '/Users/leabelzunces/code/lectura/images'

# On les stocke dans des variables
input_folder='/Users/leabelzunces/code/lectura/input'
output_folder='/Users/leabelzunces/code/lectura/output'
images_folder='/Users/leabelzunces/code/lectura/images'

# On copie les fichiers de la clé usb dans le dossier input
cp $file $input_folder

# On exécute le script python qui convertit les fichiers du dossier input en HTML
python3 markdown_converter.py

# On exécute le script qui ouvre le fichier HTML et fait un screenshot

# python3 make_screenshot.py

# On supprime le dossier input
rm -rf $input_folder

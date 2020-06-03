# GESTION DES FICHIERS IMAGES

import os

# On définit le dossier avec tous les fichiers importés
input_folder = './input'

# On crée une liste qui contiendra le nom des images repérées dans le dossier input
JPGFilenames = []
jpgFilenames = []

def returnImgFound():
	
	for subdir, dirs, files in os.walk(input_folder): # Pour chaque chemin, dossiers et fichiers dans ./input_folder
		for filename in files: # et pour chaque nom de fichier pour chaque fichier
			fullpath = subdir + os.sep + filename # on enregistre le chemin du fichier et son nom dans une variable de type str (important sinon erreur d'ouverture car chemin et nom de nature différente)
			
			if filename.endswith(".JPG"): # Si le fichier finit par .JPG
				formatted_filename = os.path.splitext(filename)[0] # On supprime l'extension .JPG du nom du fichier
				JPGFilenames.append(formatted_filename) # On ajoute le nom formaté à notre liste
		
			if filename.endswith(".jpg"): # Si le fichier finit par .JPG
				formatted_filename = os.path.splitext(filename)[0] # On supprime l'extension .JPG du nom du fichier
				jpgFilenames.append(formatted_filename) # On ajoute le nom formaté à notre liste
				
	return JPGFilenames, jpgFilenames

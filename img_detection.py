import os

# On crée deux listes qui contiendront le nom des images repérées dans ./input/
image_filenames = []

# Fonction qui trouve les images dans ./input/ et sous-dossiers
# et qui les stocke dans une des listes
def find_image_file(input_folder):
	for current_dir, dirs, files in os.walk(input_folder): # Pour chaque chemin, dossiers et fichiers dans ./input_folder
		for filename in files: # et pour chaque nom de fichier pour chaque fichier
			fullpath = current_dir + os.sep + filename # on enregistre le chemin du fichier et son nom dans une variable de type str (important sinon erreur d'ouverture car chemin et nom de nature différente)

			if filename.endswith((".JPG", ".jpg")): # Si le fichier finit par .JPG ou .jpg
				formatted_filename = os.path.splitext(filename)[0] # On supprime l'extension .JPG du nom du fichier
				image_filenames.append(formatted_filename) # On ajoute le nom formaté à notre liste

# Fonction qui détecte si le nom du fichier texte courant correspond au nom d'une image listée
# si oui, retourne l'image avec son chemin d'accès dans une balise <img>, si non, ne retourne rien
def corresponding_image_for_filename(filename, input_folder, subdir):
	if filename in image_filenames: # Si current est identique à une des strings dans JPGFilenames (et donc si boolean == true)
		value = f"'.{subdir}/{filename}.jpg" # on recrée le chemin d'accès de l'image pour pouvoir l'afficher dans le fichier html
		valueInHTMLTag = f"<img src='{value}'>\n" # on entoure value d'une balise <img>
		return valueInHTMLTag # et on retourne l'image .JPG avec sa balise
  else: # Autrement
    return '' # on ne retourne rien


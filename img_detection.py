import os

# On crée deux listes qui contiendront le nom des images repérées dans ./input/
JPGFilenames = []
jpgFilenames = []

# Fonction qui trouve les images dans ./input/ et sous-dossiers
# et qui les stocke dans une des listes
def findImg(input_folder):
	
	for subdir, dirs, files in os.walk(input_folder): # Pour chaque chemin, dossiers et fichiers dans ./input_folder
		for filename in files: # et pour chaque nom de fichier pour chaque fichier
			fullpath = subdir + os.sep + filename # on enregistre le chemin du fichier et son nom dans une variable de type str (important sinon erreur d'ouverture car chemin et nom de nature différente)
			
			if filename.endswith(".JPG"): # Si le fichier finit par .JPG
				formatted_filename = os.path.splitext(filename)[0] # On supprime l'extension .JPG du nom du fichier
				JPGFilenames.append(formatted_filename) # On ajoute le nom formaté à notre liste
		
			if filename.endswith(".jpg"): # Si le fichier finit par .jpg
				formatted_filename = os.path.splitext(filename)[0] # On supprime l'extension .jpg du nom du fichier
				jpgFilenames.append(formatted_filename) # On ajoute le nom formaté à notre liste


# Fonction qui détecte si le nom du fichier texte courant correspond au nom d'une image listée
# si oui, retourne l'image avec son chemin d'accès dans une balise <img>, si non, ne retourne rien
def returnIfCorrespondingImgFor(current, input_folder, subdir):
	
	# V ou F, current est dans la liste xxxFilenames
	booleanJPG = current in JPGFilenames
	booleanjpg = current in jpgFilenames

	if booleanJPG: # Si current est identique à une des strings dans JPGFilenames (et donc si boolean == true)
		index = JPGFilenames.index(current) # on récupère l'index 
		value = JPGFilenames[index] # on récupère la valeur (str) qui correspond à l'emplacement de l'index
		value = '.'+subdir + "/" + value + ".JPG" # on recrée le chemin d'accès de l'image pour pouvoir l'afficher dans le fichier html
		valueInHTMLTag = '<img src="' + value + '"></img>\n' # on entoure value d'une balise <img>
		return valueInHTMLTag # et on retourne l'image .JPG avec sa balise

	elif booleanjpg: # Si current est identique à une des strings dans jpgFilenames (et donc si boolean == true)
		index = jpgFilenames.index(current)
		value = jpgFilenames[index]
		value = '.'+subdir + "/" + value + ".jpg"
		valueInHTMLTag = '<img src="' + value + '"></img>\n'
		return valueInHTMLTag # on retourne l'image .jpg avec sa balise
	else: # Autrement
		return '' # on ne retourne rien

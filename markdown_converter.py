import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import os
import imgkit #à installer à la main via `sudo apt-get install wkhtmltopdf`
import qrcodegenerator

# On définit le dossier avec tous les fichiers importés
input_folder = './input'
# On crée une liste qui contiendra le nom des images repérées dans le dossier input
imgFilenames = []

# Pour chaque chemin, dossiers et fichiers dans ./input_folder
for path, dirs, files in os.walk(input_folder):
	for filename in files: # et pour chaque nom de fichier pour chaque fichier
		fullpath = os.path.join(path, filename) # on enregistre le chemin du fichier et son nom dans une variable de type str (important sinon erreur d'ouverture car chemin et nom de nature différente)
		
		# GESTION DES FICHIERS IMAGE
		if filename.endswith(".JPG"): # Si le fichier finit par .JPG
			formatted_filename = os.path.splitext(filename)[0] # On supprime l'extension .JPG du nom du fichier
			imgFilenames.append(formatted_filename) # On ajoute le nom formaté à notre liste

# Pour chaque chemin, dossiers et fichiers dans ./input_folder	
for path, dirs, files in os.walk(input_folder):
	for filename in files: # et pour chaque nom de fichier pour chaque fichier
		fullpath = os.path.join(path, filename) # on enregistre le chemin du fichier et son nom dans une variable de type str (important sinon erreur d'ouverture car chemin et nom de nature différente)
		
		# GESTION DES FICHIERS TEXTE
		if fullpath.endswith(".txt"): # Si le fichier finit par .txt
			
			# On ouvre le fichier une première fois pour lancer le script qui récupère l'URL et la transforme en qrcode
			with open(fullpath, 'r') as myfile:
				filename = os.path.basename(myfile.name) # On récupère le filename pour pouvoir appeler le qrcode de la même façon
				qrcodegenerator.extractURL(myfile, filename) # On appelle la fonction extractURL dans le fichier qrcodegenerator
			
			# On réouvre le fichier une seconde fois pour lancer la récupération du contenu global
			# C'est moche mais soit ça ne génère pas de qrcode soit ça ne génère pas le contenu textuel
			with open(fullpath, 'r') as myfile:
				contents = myfile.read() # On récupère le contenu
				filename = os.path.basename(myfile.name)
			
			formatted_filename = os.path.splitext(filename)[0] # On retire l'extension (.txt) du nom du fichier

			output_file = open(r'./output/'+formatted_filename+'.html', 'w') # On crée et ouvre le fichier avec le même nom formaté dans le dossier ./output

			# On ajoute les balises header pour link le CSS
			header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n"
			output_file.write(header)

			# On convertit le markdown en HTML
			html = markdown.markdown(contents)
			
			# On vérifie si le nom du fichier txt est identique à un des noms dans le tableau d'images
			current = formatted_filename
			boolean = current in imgFilenames #V ou F, current est dans la liste imgFilenames

			# On ouvre la balise body, on insère le HTML converti
			output_file.write("<body>\n")
			output_file.write(html)
			
			# On insère l'image s'il y en a une
			if boolean: # Si current est identique à une des strings dans imgFilenames (et donc si boolean == true)
				index = imgFilenames.index(current) # On récupère l'index 
				value = imgFilenames[index] # On récupère la valeur (str) qui correspond à l'emplacement de l'index
				value = "../input/" + value + ".JPG" # On recrée le chemin d'accès de l'image
				output_file.write('<img src="' + value + '"></img>\n') # On insère le chemin d'accès de l'image dans une balise img
			
			# On insère le QRcode depuis dossier input
			qrcode = "../input/" + formatted_filename + ".png" # On recrée le chemin d'accès de l'image
			output_file.write('<div class="qrcode">\n<img src="' + qrcode + '"></img>\n</div>') # On insère le chemin d'accès de l'image dans une balise img			
			
			#On referme notre balise body
			output_file.write("\n</body>")
			
			#Et on ferme le fichier
			output_file.close() 
		
			# On enregistre en jpg une capture du fichier html avec le css d'appliqué 
			imgkit.from_file('./output/'+formatted_filename+'.html', './images/'+formatted_filename+'.jpg')

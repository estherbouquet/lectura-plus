import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import os
import imgkit #à installer à la main via `sudo apt-get install wkhtmltopdf`

# On définit le dossier avec tous les fichiers importés
input_folder = './input'
imgFilenames = []

# Pour chaque chemin, dossiers et fichiers dans ce dossier
for path, dirs, files in os.walk(input_folder):
	for filename in files: # et pour chaque nom de fichier pour chaque fichier
		fullpath = os.path.join(path, filename) # on enregistre le chemin du fichier et son nom dans une variable de type str (important sinon erreur d'ouverture car chemin et nom de nature différente)
		
		if filename.endswith(".JPG"):
			formatted_filename = os.path.splitext(filename)[0]
			imgFilenames.append(formatted_filename)
	#print(len(imgFilenames))
	#print(imgFilenames)
	
for path, dirs, files in os.walk(input_folder):
	for filename in files: # et pour chaque nom de fichier pour chaque fichier
		fullpath = os.path.join(path, filename) # on enregistre le chemin du fichier et son nom dans une variable de type str (important sinon erreur d'ouverture car chemin et nom de nature différente)
			
		if fullpath.endswith(".txt"): # si le fichier finit par .txt
			# On ouvre le fichier
			with open(fullpath, 'r') as myfile:
				contents = myfile.read() # On récupère le contenu
				filename = os.path.basename(myfile.name) # On récupère le nom du fichier (sans le chemin d'accès)

			#print("txt"+filename) # debug
			formatted_filename = os.path.splitext(filename)[0] # On retire l'extension (.txt) du nom du fichier
			#print(formatted_filename) # debug

			output_file = open(r'./output/'+formatted_filename+'.html', 'w') # On crée le fichier avec le même nom dans le dossier ./output

			# On ajoute les balises header pour link le CSS
			header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n"
			output_file.write(header)

			# On convertit le markdown en HTML
			html = markdown.markdown(contents)
			
			# On vérifie si le nom du fichier txt est identique à un des noms dans le tableau d'images
			current = formatted_filename
			boolean = current in imgFilenames #V ou F, current est dans la liste imgFilenames
			#print(boolean)

			# On insère le HTML converti entre deux balises body
			output_file.write("<body>\n")
			output_file.write(html)
			if boolean: # si current est identique à une des strings dans imgFilenames
				index = imgFilenames.index(current) # on récupère l'index 
				value = imgFilenames[index] # et on récupère la valeur
				value = "../input/" + value + ".JPG" # et on recrée le chemin d'accès
				#print(index, value)
				output_file.write('<img src="' + value + '"></img>\n')
			output_file.write("\n</body>")
			output_file.close() #bien penser à fermer le fichier
		
			# On enregistre en jpg une capture du fichier html avec le css d'appliqué
			imgkit.from_file('./output/'+formatted_filename+'.html', './images/'+formatted_filename+'.jpg')
			#print('./output/'+formatted_filename+'.html') # debug

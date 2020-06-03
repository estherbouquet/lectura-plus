import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import os
import imgkit # à installer à la main via `sudo apt-get install wkhtmltopdf`

# importation des sous fichiers python dont on a besoin
import img_detection # on importe le fichier imgDetection.py, ce qui nous permet d'accéder à la fonction returnImgFound
import qrcodegenerator # on importe le fichier qrcodegenerator.py, ce qui nous permet d'accéder à la fonction extractURL

# On définit le dossier avec tous les fichiers importés
input_folder = './input'

# On stocke dans des variables les deux listes retournées (sous la forme d'un tuple) par la fonction returnImgFound du fichier imgDetection
JPGFilenames, jpgFilenames = img_detection.returnImgFound()
	
# GESTION DES FICHIERS TEXTES
for subdir, dirs, files in os.walk(input_folder):
	for filename in files:
		fullpath = subdir + os.sep + filename 

		if fullpath.endswith(".txt"):
			
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
			booleanJPG = current in JPGFilenames #V ou F, current est dans la liste imgFilenames
			booleanjpg = current in jpgFilenames
			# On ouvre la balise body, on insère le HTML converti
			output_file.write("<body>\n")
			output_file.write(html)
			
			# On insère l'image s'il y en a une
			if booleanJPG: # Si current est identique à une des strings dans imgFilenames (et donc si boolean == true)
				index = JPGFilenames.index(current) # On récupère l'index 
				value = JPGFilenames[index] # On récupère la valeur (str) qui correspond à l'emplacement de l'index
				value = '.'+subdir + "/" + value + ".JPG" # On recrée le chemin d'accès de l'image
				output_file.write('<img src="' + value + '"></img>\n') # On insère le chemin d'accès de l'image dans une balise img

			elif booleanjpg:
				index = jpgFilenames.index(current)
				value = jpgFilenames[index]
				value = '.'+subdir + "/" + value + ".jpg"
				output_file.write('<img src="' + value + '"></img>\n')
			# On insère le QRcode depuis dossier input
			qrcode = "../input/" + formatted_filename + ".png" # On recrée le chemin d'accès de l'image
			output_file.write('<div class="qrcode">\n<img src="' + qrcode + '"></img>\n</div>') # On insère le chemin d'accès de l'image dans une balise img			
			
			# On referme notre balise body
			output_file.write("\n</body>")
			
			# Et on ferme le fichier
			output_file.close() 
		
			# On enregistre en jpg une capture du fichier html avec le css d'appliqué 
			imgkit.from_file('./output/'+formatted_filename+'.html', './images/'+formatted_filename+'.jpg')

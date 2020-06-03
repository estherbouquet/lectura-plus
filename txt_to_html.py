import os
import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import img_detection

# Fonction qui convertit notre fichier .txt courant dans ./input/ avec du texte en markdown à l'intérieur,
# en fichier .html balisé dans ./output/
def layout(fullpath, input_folder, subdir):
	
	# A- On ouvre le fichier pour récupérer le contenu
	with open(fullpath, 'r') as myfile:
		contents = myfile.read() # on récupère le contenu dans la variable contents
		filename = os.path.basename(myfile.name) # on récupère le chemin d'accès au fichier

	formatted_filename = os.path.splitext(filename)[0] # on retire l'extension (.txt) du nom du fichier
				
	# B- On crée et ouvre un fichier .html avec le même nom formaté que le fichier .txt actuel dans le dossier ./output/
	output_file = open(r'./output/'+formatted_filename+'.html', 'w') # avec les droits d'écriture

	# C- On crée la balise head pour lier le CSS, nommer le fichier, déclarer le format des caractères en utf-8
	header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n"
	output_file.write(header) # et on l'écrit dans le fichier
	
	# D- On convertit le markdown de contents en balises html
	html = markdown.markdown(contents) 

	# E- On écrit l'ouverture de la balise body 
	output_file.write("<body>\n")
	
	output_file.write(html) # on insère le HTML converti
	output_file.write(img_detection.returnIfCorrespondingImgFor(formatted_filename, input_folder, subdir)) # on insère ce que retourne la fonction returnIfCorrespondingImgFor
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès du qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '"></img>\n</div>') # on insère le chemin d'accès du qrcode dans une balise img			
				
	# F- On écrit la fermeture de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close() 

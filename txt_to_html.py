import os
import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import img_detection
import update_markdown
import adding_graphic_lines
import horizontal_bloc
from image_ratio import ImageRatioCalculator
import add_footer

# Fonction qui convertit notre fichier .txt courant dans ./input/ avec du texte en markdown à l'intérieur,
# en fichier .html balisé dans ./output/
def layout(fullpath, input_folder, subdir):
	print("layout :" + fullpath)
	update_markdown.rearrangeMardownOrder(fullpath) # on reformate le markdown utilisé pour un autre plus lisible
	
	# A- On ouvre le fichier pour récupérer le contenu
	with open(fullpath, 'r') as myfile:

		contents = myfile.read() # on récupère le contenu dans la variable contents
		#print('le fichier contient : '+contents) # debug
		filename = os.path.basename(myfile.name) # on récupère le chemin d'accès au fichier

	formatted_filename = os.path.splitext(filename)[0] # on retire l'extension (.txt) du nom+chemin d'accès du fichier
				
	# B- On crée et ouvre un fichier .html avec le même nom formaté que le fichier .txt actuel dans le dossier ./output/
	output_file = open(r'./output/'+formatted_filename+'.html', 'w') # avec les droits d'écriture

	img_ratio_calculator = ImageRatioCalculator(formatted_filename)

	# C- On ajoute et/ou crée le contenu
	if img_ratio_calculator.horizontal_ratio(): # si true = si l'image est verticale plutôt qu'horizontale
		if formatted_filename.startswith("METEO"): # et si l'article commence par METEO
			header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet_meteo_h.css' rel='stylesheet'>\n</head>\n" # on charge stylesheet_meteo_h.css / black background & horizontal display
		else: # pour tous les articles qui ne commencent pas par METEO
			header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet_horizontale.css' rel='stylesheet'>\n</head>\n" # on charge stylesheet_horizontale.css / white background & h display
		
		output_file.write(header) # on écrit cette balise head
		
		
		output_file.write("<body>\n") # on append la balise body 

		html = markdown.markdown(contents) # on convertit notre markdown en div html
		html = horizontal_bloc.add(html) # on ajoute le bloc entete en mode horizontal

		output_file.write(html) # on écrit 
		output_file.write(img_detection.returnIfCorrespondingImgFor(formatted_filename, input_folder, subdir)) # on retourne le chemin vers l'image qui correspond au même filename
		output_file.write("</div>\n") # on ferme la balise enteteh qu'on ouvre dans horizontal_bloc.add() mais qu'on ne peut pas fermer au moment où on la crée
		
		add_footer.horizontal(formatted_filename, output_file) # on appelle la fonction horizontal du fichier add_footer qui vient ajouter les mentions, les logos, le qrcode et fermer le fichier
		
	else: # si img_ratio_calculator.horizontal_ratio() est faux, soit parce qu'il n'y a pas d'image, soit parce que celle-ci est horizontale
		if formatted_filename.startswith("METEO"): # et si l'article commence par météo
			header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet_meteo.css' rel='stylesheet'>\n</head>\n" # on charge stylesheet_meteo.css / black background & vertical display
		else: # pour les autres articles
			header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n" # on charge stylesheet.css / white background & v display

		output_file.write(header) # et on l'écrit dans le fichier                                                   	
		
		output_file.write("<body>\n")

		html = markdown.markdown(contents) 
		html = adding_graphic_lines.add(html)

		
		output_file.write(html) # on insère le HTML converti
		output_file.write(img_detection.returnIfCorrespondingImgFor(formatted_filename, input_folder, subdir)) # on insère ce que retourne la fonction returnIfCorrespondingImgFor	

		add_footer.vertical(formatted_filename, output_file)

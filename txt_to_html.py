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

	formatted_filename = os.path.splitext(filename)[0] # on retire l'extension (.txt) du nom+chemin d'accès du fichier
				
	# B- On crée et ouvre un fichier .html avec le même nom formaté que le fichier .txt actuel dans le dossier ./output/
	output_file = open(r'./output/'+formatted_filename+'.html', 'w') # avec les droits d'écriture

	# C- On crée la balise head pour lier le CSS, nommer le fichier, déclarer le format des caractères en utf-8
	if formatted_filename.startswith("METEO"):
		header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet_meteo.css' rel='stylesheet'>\n</head>\n"
		output_file.write(header) # et on l'écrit dans le fichier
	else:
		header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n"
		output_file.write(header) # et on l'écrit dans le fichier
	
	# D- On convertit le markdown de contents en balises html
	html = markdown.markdown(contents) 

	# E- On écrit l'ouverture de la balise body 
	output_file.write("<body>\n")
	output_file.write('<div class="logo">\n<img src=../assets/LogoL.png></img>\n</div>') # on insère le logo
	output_file.write(html) # on insère le HTML converti
	output_file.write(img_detection.returnIfCorrespondingImgFor(formatted_filename, input_folder, subdir)) # on insère ce que retourne la fonction returnIfCorrespondingImgFor
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '"></img>\n</div>') # on insère le chemin d'accès du qrcode dans une balise img			
	# on insère le texte de présentation
	output_file.write('<div class="presentation">\n<p>Un ticket de presse ancienne proposé par Lectura Plus, le site du patrimoine écrit et graphique en Auvergne-Rhône-Alpes.</p>\n</div>')
	output_file.write('<div class="presentation">\n<p>À lire dans la minute ! Pour plus de découvertes, rendez-vous sur www.lectura.plus</p>\n</div>')
	output_file.write('<div class="presentation italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')
	# et les mentions légales
	output_file.write('<div class="mentions">\n<p>Lectura PLus est un projet coopératif des Villes et Agglomérations d\'Annecy, Bourg-en-Bresse, Chambéry, Clermont-Ferrand, Grenoble, Lyon, Roanne, Saint-Étienne et Valence, réalisé avec le soutien de la DRAC Auvergne-Rhône-Alpes et coordonné par par Auvergne-Rhône-Alpes Livre et Lecture. Conçu par Léa Belzunces, Esther Bouquet et Déborah-Loïs Séry.</p>\n</div>')
	# et le bloc logos
	output_file.write('<div class="bloclogo">\n<img class="gauche" src=../assets/bloc-logos_Agence-horizontal-noir-seul.png></img>\n<img class="droite" src=../assets/PREF_region_Auvergne_Rhone_Alpes_N.png></img>\n</div>')
	
	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close() 

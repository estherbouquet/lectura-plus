import os
import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import img_detection
import update_markdown
import adding_graphic_lines

# Fonction qui convertit notre fichier .txt courant dans ./input/ avec du texte en markdown à l'intérieur,
# en fichier .html balisé dans ./output/
def layout(fullpath, input_folder, subdir):

	update_markdown.rearrangeMardownOrder(fullpath) # on reformate le markdown utilisé pour un autre plus lisible

	# A- On ouvre le fichier pour récupérer le contenu
	with open(fullpath, 'r') as myfile:

		contents = myfile.read() # on récupère le contenu dans la variable contents
		#print('le fichier contient : '+contents) # debug
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
		# créer la variable avec le tag et la date ici

	# insérer les lignes de +++ après nom du journal et après titre

	# D- On convertit le markdown de contents en balises html
	html = markdown.markdown(contents)
	html = adding_graphic_lines.add(html)
	#print(html)
	# E- On écrit l'ouverture de la balise body
	output_file.write("<body>\n")
	# on insère ici la variable tag
	output_file.write(html) # on insère le HTML converti

	output_file.write(img_detection.corresponding_image_for_filename(formatted_filename, input_folder, subdir)) # on insère ce que retourne la fonction returnIfCorrespondingImgFor

	# on insère le texte de présentation
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-barre-nb.png"></img>\n</div>')
	else:
		output_file.write('<div class="blocplus">\n<img src="../assets/element-barre.png"></img>\n</div>')

	output_file.write('<div class="ticket">\n<p>Un ticket de presse ancienne proposé par Lectura Plus, le site du patrimoine écrit et graphique en Auvergne-Rhône-Alpes.<br>À lire dans la minute ! Pour plus de découvertes, rendez-vous sur <u>www.lectura.plus</u></p>\n</div>')
	output_file.write('<div class="italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')

	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
	else:
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>') # ligne + + + + +

	output_file.write('<div class="logoL">\n<img src=../assets/LogoL.png></img>\n</div>') # on insère le logo

	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
	else:
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>') # ligne + + + + +

	# et les mentions légales
	output_file.write('<div class="mentions">\n<p>Lectura Plus est un projet coopératif des Villes et Agglomérations d\'Annecy, Bourg-en-Bresse, Chambéry, Clermont-Ferrand, Grenoble, Lyon, Roanne, Saint-Étienne et Valence, réalisé avec le soutien de la DRAC Auvergne-Rhône-Alpes et coordonné par Auvergne-Rhône-Alpes Livre et Lecture.</p>\n</div>')
	output_file.write('<div class="mentions">\n<p>Un projet imaginé et coordonné par Alizé Buisse et Priscille Legros, Auvergne-Rhône-Alpes Livre et Lecture. Dispositif numérique conçu par Léa Belzunces et Esther Bouquet. Conception graphique menée par Déborah-Loïs Séry. Fabrication artisanale par Guillaume Buisson, Atelier Regards.</p>\n</div>')

	# et le bloc logos
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
	else:
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>') # ligne + + + + +

	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="bloclogo">\n<img src="../assets/blog-logo-complet-nb.jpg"></img>\n</div>')
	else:
		output_file.write('<div class="bloclogo">\n<img src="../assets/blog-logo-complet.jpg"></img>\n</div>')

	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
	else:
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>') # ligne + + + + +


	# et le QRcode
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '"></img>\n</div>') # on insère le chemin d'accès du qrcode dans une balise img

	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")

	# G- On ferme le fichier .html
	output_file.close()

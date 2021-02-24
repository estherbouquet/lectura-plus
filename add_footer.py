def vertical(formatted_filename, output_file):	
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-barre-nb.png">\n</div>')
	else:	
		output_file.write('<div class="blocplus">\n<img src="../assets/element-barre.png">\n</div>')
		
	output_file.write('<div class="ticket">\n<p>Un ticket de presse ancienne proposé par Lectura Plus, le site du patrimoine écrit et graphique en Auvergne-Rhône-Alpes.<br>À lire dans la minute ! Pour plus de découvertes, rendez-vous sur <u>www.lectura.plus</u></p>\n</div>')
	output_file.write('<div class="italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')
	
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png">\n</div>')
	else: 
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>') # ligne + + + + +
		
	output_file.write('<div class="logoL">\n<img src="../assets/LogoL.png">\n</div>') # on insère le logo
	
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png">\n</div>')
	else: 
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>') # ligne + + + + +
	
	# et les mentions légales
	output_file.write('<div class="mentions">\n<p>Lectura Plus est un projet coopératif des Villes et Agglomérations d\'Annecy, Bourg-en-Bresse, Chambéry, Clermont-Ferrand, Grenoble, Lyon, Roanne, Saint-Étienne et Valence, réalisé avec le soutien de la DRAC Auvergne-Rhône-Alpes et coordonné par Auvergne-Rhône-Alpes Livre et Lecture.</p>\n</div>')
	output_file.write('<div class="mentions">\n<p>Un projet imaginé et coordonné par Alizé Buisse et Priscille Legros, Auvergne-Rhône-Alpes Livre et Lecture. Dispositif numérique conçu par Léa Belzunces et Esther Bouquet. Conception graphique menée par Déborah-Loïs Séry. Fabrication artisanale par Guillaume Buisson, Atelier Regards.</p>\n</div>')

	# et le bloc logos
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png">\n</div>')
	else: 
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>') # ligne + + + + +
		
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="bloclogo">\n<img src="../assets/blog-logo-complet-nb.jpg">\n</div>')
	else:
		output_file.write('<div class="bloclogo">\n<img src="../assets/blog-logo-complet.jpg">\n</div>')
	
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png">\n</div>')
	else: 
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>') # ligne + + + + +
	
	
	# et le QRcode
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '">\n</div>') # on insère le chemin d'accès du qrcode dans une balise img
		
	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close() 

def horizontal (formatted_filename, output_file):	

	output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>')
		
	#output_file.write('<div class="rotate">\n')
	#output_file.write('<div class="bloc1">\n')
	#output_file.write('<div class="ticket">\n<p>Un ticket de presse ancienne proposé par Lectura Plus, le site du patrimoine écrit et graphique en Auvergne-Rhône-Alpes.<br>À lire dans la minute ! Pour plus de découvertes, rendez-vous sur <u>www.lectura.plus</u></p>\n</div>')
	#output_file.write('<div class="italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')
	
	#output_file.write('<div class="mentions">\n<p>Lectura Plus est un projet coopératif des Villes et Agglomérations d\'Annecy, Bourg-en-Bresse, Chambéry, Clermont-Ferrand, Grenoble, Lyon, Roanne, Saint-Étienne et Valence, réalisé avec le soutien de la DRAC Auvergne-Rhône-Alpes et coordonné par Auvergne-Rhône-Alpes Livre et Lecture.</p>\n</div>\n</div>\n')
	#output_file.write('<div class="bloc2">\n')
	#output_file.write('<div class="mentions">\n<p>Un projet imaginé et coordonné par Alizé Buisse et Priscille Legros, Auvergne-Rhône-Alpes Livre et Lecture. Dispositif numérique conçu par Léa Belzunces et Esther Bouquet. Conception graphique menée par Déborah-Loïs Séry. Fabrication artisanale par Guillaume Buisson, Atelier Regards.</p>\n</div>')	
	#output_file.write('<div class="blocplus">\n<img src="../assets/element-barre.png">\n</div>')	
	#output_file.write('<div class="logoL">\n<img src="../assets/LogoL.png">\n</div>\n</div>') # on insère le logo
	#output_file.write("</div>")
	output_file.write('<div class="footer">\n<img src="../assets/bloc-footer-ok.jpg">\n</div>')
	output_file.write('<div class="blocplus special">\n<img src="../assets/element-plus-ok.png">\n</div>') # ligne + + + + + 
	output_file.write('<div class="blocplus special2">\n<img src="../assets/blog-logo-complet-horizontal.jpg">\n</div>') # ligne + + + + +
	output_file.write('<div class="bloclogo">\n<img src="../assets/element-plus-ok.png">\n</div>')
		
	
	# et le QRcode
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '">\n</div>') # on insère le chemin d'accès du qrcode dans une balise img
		
	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close()

def vertical(formatted_filename, output_file):	
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-barre-nb.png">\n</div>')
	else:	
		output_file.write('<div class="blocplus">\n<img src="../assets/element-barre.png">\n</div>')
		
	output_file.write('<div class="ticket">\n<p>Un ticket de presse ancienne proposé par Auvergne-Rhône-Alpes livre et lecture.<br>Pour plus de découvertes, rendez-vous sur les pages Auvergne-Rhône-Alpes de Gallica :<br><u>https://gallica.bnf.fr/selections/fr/html/presse-locale-ancienne-en-auvergne-rhone-alpes</u></p>\n</div>')
	output_file.write('<div class="italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')
	
	if formatted_filename.startswith("METEO"):
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-nb.png">\n</div>')
	else: 
		output_file.write('<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>') # ligne + + + + +
	
	# et les mentions légales
	output_file.write('<div class="mentions">\n<p>L\'Exprimante, distributeur de presse ancienne (1807-1945), est un outil de compréhension des modes de vie et de l\'activité des territoires. Un dispositif de médiation innovant et un projet coopératif Lectura Plus conçu par les bibliothèques des Villes et Agglomérations d\'Annecy, Bourg-en-Bresse, Chambéry, Clermont-Ferrand, Grenoble, Lyon, Roanne, Saint-Etienne et Valence, réalisé avec le soutien de la DRAC Auvergne-Rhône-Alpes et coordonné par Auvergne-Rhône-Alpes livre et lecture.</p>\n</div>')
	output_file.write('<div class="mentions">\n<p>Dispositif numérique : Léa Belzunces et Esther Bouquet. Conception graphique : Déborah-Loïs Séry. Fabrication artisanale : Guillaume Buisson, Atelier Regards.</p>\n</div>')

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
		
	output_file.write('<div class="footer">\n<img src="../assets/bloc-footer-ok.jpg">\n</div>')
	output_file.write('<div class="blocplus special">\n<img src="../assets/element-plus-ok.png">\n</div>') # ligne + + + + + 
		
	
	# et le QRcode
	qrcode = "../input/" + formatted_filename + ".png" # on recrée le chemin d'accès vers le qrcode depuis ./input/
	output_file.write('<div class="qrcode">\n<img src="' + qrcode + '">\n</div>') # on insère le chemin d'accès du qrcode dans une balise img
		
	# F- On écrit la fin de notre balise body
	output_file.write("\n</body>")
				
	# G- On ferme le fichier .html
	output_file.close()


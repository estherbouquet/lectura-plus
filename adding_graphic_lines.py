#trouver la fin de la div entete et ajouter les plus
#trouver la fin de h6 et ajouter le plus
# si il y a un h2 on ajoute le plus apres la fin du h2 sinon après la fin du h1


def add(contentInHtml):
	#print(contentInHtml) #debug - print bien une str avec balises html
	if 'METEO' in contentInHtml:
		contentInHtml = contentInHtml.replace('METEO', 'MÉTÉO')
		contentInHtml = contentInHtml.replace('</div>', '</div>\n<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
		contentInHtml = contentInHtml.replace('</h6>', '</h6>\n<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
		if '<h2>' in contentInHtml:
			contentInHtml = contentInHtml.replace('</h2>', '</h2>\n<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
			#print("found h2")
		else:
			contentInHtml = contentInHtml.replace('</h1>', '</h1>\n<div class="blocplus">\n<img src="../assets/element-plus-nb.png"></img>\n</div>')
			#print("only h1, no h2")		
	else:		
		contentInHtml = contentInHtml.replace('</div>', '</div>\n<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>')
		contentInHtml = contentInHtml.replace('</h6>', '</h6>\n<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>')
		if '<h2>' in contentInHtml:
			contentInHtml = contentInHtml.replace('</h2>', '</h2>\n<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>')
			#print("found h2")
		else:
			contentInHtml = contentInHtml.replace('</h1>', '</h1>\n<div class="blocplus">\n<img src="../assets/element-plus-ok.png"></img>\n</div>')
			#print("only h1, no h2")
	return(contentInHtml)

def add(contentInHtml):
	#print(contentInHtml) #debug - print bien une str avec balises html
	contentInHtml = contentInHtml.replace('<div class="entete">', '<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>\n<div class="blocEnteteh">\n<div class="entete">')
	contentInHtml = contentInHtml.replace('</h6>', '</h6>\n<div class="blocplus">\n<img src="../assets/element-barre.png">\n</div>')
	contentInHtml = contentInHtml.replace('</h4>', '</h4>\n<div class="img-h">\n')
	if '<h2>' in contentInHtml:
		contentInHtml = contentInHtml.replace('</h2>', '</h2>\n</div>\n<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>')
	elif '<h1>' in contentInHtml:
		contentInHtml = contentInHtml.replace('</h1>', '</h1>\n</div>\n<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>')
	else: 
		contentInHtml = contentInHtml.replace('<img src="../assets/element-barre.png">\n</div>', '<img src="../assets/element-barre.png">\n</div>\n</div>\n<div class="blocplus">\n<img src="../assets/element-plus-ok.png">\n</div>')
		contentInHtml = contentInHtml.replace('<h6>', '<h1>')
		contentInHtml = contentInHtml.replace('</h6>', '</h1>')

	return(contentInHtml)

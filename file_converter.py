import os
import imgkit # à installer à la main via `sudo apt-get install wkhtmltopdf`

# Importation des sous fichiers python dont on a besoin :
import img_detection # on importe le fichier imgDetection.py, ce qui nous permet d'accéder à la fonction findImg
import qrcodegenerator # on importe le fichier qrcodegenerator.py, ce qui nous permet d'accéder à la fonction extractURL
import txt_to_html # on importe le fichier txt_to_html.py, ce qui nous permet d'accéder à la fonction layout

# On définit le dossier où sont les fichiers (textes et images) importés
input_folder = './input'

# A- On s'occupe des fichiers jpg et JPG 
img_detection.findImg(input_folder) # fonction findImg qui détecte + stocke dans des listes les images trouvées dans le dossier ./input/ + subdir

# B- On s'occupe des fichiers .txt
for subdir, dirs, files in os.walk(input_folder): # Pour chaque chemin, dossiers et fichiers dans ./input_folder
	for filename in files: # et pour chaque nom de fichier pour chaque fichier
		fullpath = subdir + os.sep + filename # on enregistre le chemin du fichier, son nom et son extension dans une variable de type str 

		if fullpath.endswith(".txt"): # Si le fichier finit par .txt
			
			# 1- On extraie l'URL pour générer un QRCode
			with open(fullpath, 'r') as myfile: # on ouvre le fichier
				filename = os.path.basename(myfile.name) # on récupère le filename pour pouvoir appeler le qrcode de la même façon
				qrcodegenerator.extractURL(myfile, filename) # fonction extractURL qui transforme l'url en qrcode et l'enregistre en .png
			
			# 2- On convertit 'input/filename.txt' > 'output/filename.html'
			txt_to_html.layout(fullpath, input_folder, subdir)

# C- On s'occupe ensuite de convertir /output/*.html en ./images/*.jpg
for subdir, dirs, files in os.walk('./output'): # Pour chaque chemin, dossiers et fichiers dans ./output/
	for filename in files: # et pour chaque nom de fichier
		
		outputfile = subdir + os.sep + filename # on aggrège le chemin d'accès du fichier dans ./output/ avec son nom et extension
		jpgfile = './images/' + os.path.splitext(filename)[0] + '.jpg' # on retire .html du filename pour mettre .jpg et on ajoute le chemin vers ./images/
		
		imgkit.from_file(outputfile, jpgfile) # on convertit outputfile en jpgfile
		#imgkit.from_file('./output/'+filename+'.html', './images/'+filename+'.jpg')

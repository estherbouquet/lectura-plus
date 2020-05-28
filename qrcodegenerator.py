import pyqrcode 
import os

def createQrCode(urlstr, filenameURL):
	url = pyqrcode.create(urlstr) # On crée un qrcode avec l'url d'encodée
	url.png('./input/'+filenameURL+'.png', scale=5) # On l'enregistre dans input sous nomformaté.png
	#print(url.terminal(quiet_zone=1)) # debug pour afficher le qrcode dans terminal

def extractURL(myfile, filename):# On récupère comme argument le fichier et le nom du fichier
	formatted_filename = os.path.splitext(filename)[0] # On formate le nom du fichier pour pouvoir nommer notre qrcode de la même façon avec extension différente
	#print(formatted_filename)
	line = myfile.readline() # On stocke ligne par ligne myfile dans line
	count = 1 # compteur pour passer de ligne en ligne
	while line: # tant qu'il y a des lignes
		line = myfile.readline() # On les lit
		count +=1 # On incrémente de +1
		if line.startswith("####"): # Si on détecte une ligne qui commence par 4#,
			theURL = line.replace('####', '') # On supprime les #### de cette ligne
			#print(theURL)
			createQrCode(theURL, formatted_filename) # Et on envoie l'url extraite + nom du fichier à la fonction createQrCode
			

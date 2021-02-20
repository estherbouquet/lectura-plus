import re
import os

# POUR EXTRAIRE LA DATE	DE LA PREMIERE LIGNE (avec virgule et parenthèse) donc cracra
def extractDate(receivedFile, fileData):
	#print("data reçue : "+fileData)
	#On cherche sur la deuxième ligne du fichier, le motif ', date ('
	with open(receivedFile) as fin:
		for i, line in enumerate(fin):
			if i==1:
				#print(line)
				motif = ", (.*?) \(" # On cherche le motif de la date (compris entre ',' et (
				date = re.search(motif, fileData).group(0) # On sélectionne tout le motif
				#print(date) #debug
				return(date)

def createHeader(currentFile, dateFromFile):
	#print("> path of the file we are working with : "+currentFile)
	#print("> extracted date from this file : "+dateFromFile)
	
	motiftag = "./input/(.*?)-" # On cherche le motif du tag compris entre './input/' et '-' qui le sépare de la date
	tag = re.search(motiftag, currentFile).group(1) # On sélectionne uniquement la string sans les délimitateurs qu'il y a autour grâce au 1
	#print("tag : "+tag) #debug
	tag = tag.replace('PETITESANNONCES', 'PETITES ANNONCES')
	tag = tag.replace('FAITDIVERS', 'FAIT DIVERS') # Si le tag est FAITDIVERS, on remplace par "fait divers"
	#print(tag) #ça marche !!
	
	motifdate = ", (.*?) \(" # idem que pour le tag
	date = re.search(motifdate, dateFromFile).group(1)
	date = date.replace(',', '')
	date = date.replace('1er', '1<sup>er</sup>') #er en exposant si '1er' détecté
	#print("date : "+date) #debug
	
	divEntete = '<div class="entete">\n<p class="tag">'+tag+'</p>\n<p class="date">'+date+'</p>\n</div>'
	#print(divEntete)
	return(divEntete)

# POUR REMETTRE LES BONNES BALISES
def rearrangeMardownOrder(myfile):			
	fin = open(myfile, 'r') # On ouvre le fichier en lecture
	data = fin.read() # On copie le contenu lu dans la variable data
	fin.close() # On ferme le fichier
	
	fin = open(myfile, 'w') # On réouvre ce fichier avec les droits d'écriture
	
	fin.write('\n'+data) # On insert une ligne vide au début du document et le contenu de la variable data
	fin.close() # On ferme le fichier
	
	fin = open(myfile, 'r') # On le réréouvre 
	data = fin.read() # On le relit (avec la nouvelle ligne en haut du coup)
	
	# On stocke dans data les nouveaux changements de markdown sans que ça change le texte du fichier initial
	
	data = data.replace('\n### ', '\n') # on change h3 en p
	data = data.replace('\n###### ', '\n### ') # on change h6 en h3
	data = data.replace('\n# ', '\n###### ') # on change h1 en h6 (titre du journal)
	data = data.replace('\n## ', '\n# ') # on change h2 en h1
	data = data.replace('\n##### ', '\n## ') # on change h5 en h2
	data = data.replace('_', '') # on supprime parce que erreur sinon

	# POUR ENLEVER LA DATE LÀ OÙ ELLE EST INITIALEMENT (càd, après nom du jour sur ligne 2)
	extractedDate = extractDate(myfile, data) # On vient récupérer la date retournée par extractDate (et qui est avec virgule et parenthèse)
	data = data.replace(extractedDate, '<br>(') # On fait disparaître la date du document texte en la replaçant par un retour à la ligne  
	#Si on print(data) ici, la date n'apparaît plus youpi !
	
	#POUR CREER DIV AVEC TAG + DATE
	# ON APPELLE NOTRE SUPER METHODE ICI
	header = createHeader(myfile, extractedDate)
	
	fin.close() # On referme le fichier

	fin = open(myfile, 'w') # On l'ouvre une dernière fois avec les privilèges d'écriture
	fin.write(header+data) # On  écrit toutes les modifications contenues dans data
	fin.close() # On ferme, ce qui enregistre

#rearrangeMardownOrder('/home/pi/Documents/lectura-plus/articles/ALIMENTATION-18860115-ARROSOIR-p1-la-republique-est-morte.txt')

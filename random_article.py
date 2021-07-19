import os
import random
from datetime import date

today = date.today() # on crée la date d'aujourd'hui
monthday = today.strftime("%m%d") # et on l'enregistre sous la forme 'MMJJ' pour correspondre au format du nom des articles meteo (AAAAMMJJ)

# On définit le dossier où sont les articles imprimables (transformés en jpg)
folder = './images'

# On crée deux listes qui contiendront nos articles
printableArticles = [] # tous les articles sauf ceux commençant par './images/METEO'
meteoArticles = [] # tous les articles commençant par './images/METEO'

# Fonction qui ajoute les articles présents dans ./images dans la liste qui convient
def findExistingArticles():
	for subdir, dirs, files in os.walk(folder): 
		for filename in files: 
			fullpath = subdir + os.sep + filename # On sauvegarde le fichier avec son chemin d'accès 
		
			if fullpath.startswith("./images/METEO"): # Si le fichier commence par METEO
				meteoArticles.append(fullpath) # alors on l'enregistre dans la liste meteoArticles
			else: # Si le fichier ne commence pas par METEO
				printableArticles.append(fullpath) # On ajoute tous les autres articles trouvés à la liste printableArticles
	
	
# Fonction qui sélectionne un article aléatoirement 
# et qui le renvoie comme étant le "résultat" de la fonction lorsque celle-ci est appelée
def selectRandomArticle(): 
	
	findExistingArticles()
	
	# Pour gérer quand on retourne un article météo ou un article normal, on ouvre le fichier countdown.txt
	countdown = open("countdown.txt") 

	# et on le lit
	for line in countdown:
		count = int(line) # on récupère le chiffre (qui est en str) et on le transforme en int pour le sauvegarder dans count
		
		# Si la division (count / 5) a un reste = 0, alors :
		if (count % 10 == 0):  
			for article in meteoArticles: # pour chaque article météo dans la liste
				# debug - - -
				#print(monthday) # on vérifie la valeur de monthday 
				#print(article) # et la valeur d'article pour voir si monthday est bien comprise ou bien PAS comprise par la condition
				# - - - - - - 
				if monthday in article: # On vérifie si le nom de l'article contient la date d'auj
					print("count % n = 0 et il existe un article météo pour aujourd'hui"+article) # debug
					return article # si oui, alors on retourne cet article météo du jour à imprimer 
					
			else: # Si aucun des articles dans la liste meteoArticles ne contient monthday, alors on imprime un article général
				lengthPrintableArticles = len(printableArticles)-1 
				randomIndex = random.randint(0, lengthPrintableArticles) 
				selectedArticle = printableArticles[randomIndex] 
				print("count % n = 0 mais il n'existe pas d'article météo pour aujourd'hui. voici un article plus général : "+selectedArticle)
				return selectedArticle # retourne un article plus général

		else: # Si la division (count / 5) a un reste > 0, alors : 
			lengthPrintableArticles = len(printableArticles)-1 # On cherche la taille maximale de notre liste (-1 sinon, erreur out of range)
			randomIndex = random.randint(0, lengthPrintableArticles) # on crée un nombre aléatoire entre 0 et la taille de la liste
			selectedArticle = printableArticles[randomIndex] # et on utilise ce nombre aléatoire comme index pour récupérer un article
			print("count % n != 0 donc voici un article général : "+selectedArticle)
			return selectedArticle # on retourne un article général
	countdown.close()

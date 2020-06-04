from escpos.printer import Usb # import Usb class
import os
import random
from datetime import date # import de l'objet date dans la bibliothèque datetime

today = date.today() # on crée la date d'aujourd'hui
monthday = today.strftime("%m%d") # et on l'enregistre sous la forme 'moisjour' <> 'MMJJ' pour correspondre au format des articles meteo

# On définit le dossier où sont les articles imprimables (aka, mis en page et transformés en jpg)
folder = './images'

# On crée deux listes qui contiendront nos articles
printableArticles = [] # tous les articles sauf ceux commençant par './images/METEO'
meteoArticles = [] # tous les articles commençant par './images/METEO'

# Fonction qui sélectionne un article aléatoirement
def selectRandomArticle(): 
	for subdir, dirs, files in os.walk(folder): 
		for filename in files: 
			fullpath = subdir + os.sep + filename # On sauvegarde le fichier avec son chemin d'accès 
			
			if fullpath.startswith("./images/METEO"): # Si le fichier commence par METEO
				meteoArticles.append(fullpath) # alors on l'enregistre dans la liste meteoArticles
			else: 
				printableArticles.append(fullpath) # On ajoute tous les autres articles trouvés à la liste printableArticles
	
	# Pour gérer quand on return un article météo ou un article normal, on ouvre le fichier countdown.txt
	countdown = open("countdown.txt") 

	for line in countdown: # pour chaque ligne
		count = int(line) # on récupère le chiffre (qui est en str) et on le transforme en int pour le sauvegarder dans count
		
		# Si count est équivalent à une valeur arbitraire (-> à changer dans le futur)
		if count == 6: 
			for article in meteoArticles: # pour chaque article météo dans la liste
				# debug :
				print(monthday) # on vérifie la valeur de monthday 
				print(article) # et la valeur d'article pour voir si monthday est bien compris ou bien PAS compris par la condition
				
				if monthday in article: # Cn vérifie si le nom de l'article contient la date d'auj
					print("count == n et il existe un article météo pour aujourd'hui"+article) # debug
					return article # si oui, alors on retourne cet article météo du jour à imprimer 
					
			else: # Si aucun des articles dans la liste meteoArticles ne contient monthday, alors on imprime un article général
				lengthPrintableArticles = len(printableArticles)-1 
				randomIndex = random.randint(0, lengthPrintableArticles) 
				selectedArticle = printableArticles[randomIndex] 
				print("count == n mais il n'existe pas d'article météo pour aujourd'hui. voici un article plus général : "+selectedArticle)
				return selectedArticle # retourne un article plus général

		else: # Si count n'est pas équivalent à cette valeur
			lengthPrintableArticles = len(printableArticles)-1 # On cherche la taille maximale de notre liste (-1 sinon, erreur out of range)
			randomIndex = random.randint(0, lengthPrintableArticles) # on crée un nombre aléatoire entre 0 et la taille de la liste
			selectedArticle = printableArticles[randomIndex] # et on utilise ce nombre aléatoire comme index pour récupérer un article
			print("count != n donc voici un article général : "+selectedArticle)
			return selectedArticle # on retourne un article général


def printFile():
	
	p = Usb(0x04b8, 0x0e28, 0) # vendor and product ID allow us to communicate with the printer

	# RANDOM PRINTING
	
	article = selectRandomArticle()
	p.image(article)
	p.cut() # function for cutting paper

	# COUNTING
	# (for every x printings, we want a special coupon)

	limit = 10 # the number of prints is setup here

	countdown = open("countdown.txt") # open the file "countdown.txt" and store it in countdown variable

	for line in countdown: # for each line in countdown
		count = int(line) # we transform the number stored as a string into a int
		count = count +1 # we increase it by 1
		countdown = open("countdown.txt", "w+") # we open the file with writing permissions
		if count > limit: # if count is > 49
			countdown.write(str(0)) # we go back to 0
			p.text("youpi") # we print the coupon
			p.cut() #a and cut it
		else: # otherwise
			countdown.write(str(count)) # we write our var "count" increased by 1 as a string
	countdown.close() # we close the file


	# KEEPING TRACK/DEBUG
	countdown = open("countdown.txt") # we open "countdown.txt"
	read_file = countdown.read() # we read it
	print(read_file) # we print what is inside
	countdown.close() # we close the file
	

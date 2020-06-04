from escpos.printer import Usb # import Usb class
import os
import random

# On définit le dossier où sont les articles imprimables (aka, mis en page et transformés en jpg)
folder = './images'
printableArticles = []

def selectRandomArticle():
	for subdir, dirs, files in os.walk(folder): 
		for filename in files: 
			fullpath = subdir + os.sep + filename  
			printableArticles.append(fullpath) # On ajoute les articles trouvés à la liste printableArticles

	lengthPrintableArticles = len(printableArticles)-1 # On cherche la taille maximale de notre liste (-1 sinon, erreur out of range)
	randomIndex = random.randint(0, lengthPrintableArticles)
	selectedArticle = printableArticles[randomIndex]

	return selectedArticle

def printFile():
	
	p = Usb(0x04b8, 0x0e28, 0) # vendor and product ID allow us to communicate with the printer
	
	# REGULAR PRINTING
	
	#p.text("hello human, i wish u a nice day\n") # function for printing text
	#p.image("./images/ALIMENTATION-18920827-ALPESILLUSTREES-p7-liqueur-a-la-polka.jpg")
	#p.cut() # function for cutting paper

	# RANDOM PRINTING
	
	article = selectRandomArticle()
	print(article)
	p.image(article)
	p.cut() # function for cutting paper

	# COUNTING
	# (for every x printings, we want a special coupon)

	limit = 4 # the number of prints is setup here

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

printFile()

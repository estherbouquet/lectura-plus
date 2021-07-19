from escpos.printer import Usb # import Usb class
import os
import random_article
import check
from PIL import Image

# the number of prints before it prints a coupon is setup here
limit = 19 
# vendor and product ID allow us to communicate with the printer
p = Usb(0x04b8, 0x0e28, 0) 


#Function that keeps track of the number of prints in countdown.txt
def counting():
	countdown = open("countdown.txt") # open the file "countdown.txt" and store it in countdown variable

	for line in countdown: # for each line in countdown
		count = int(line) # we transform the number stored as a string into a int
		count = count +1 # we increase it by 1
		countdown = open("countdown.txt", "w+") # we open the file with writing permissions
		if count > limit: # if count is > 49
			countdown.write(str(0)) # we go back to 0
			#p.text("youpi") # we print the coupon
			#p.cut() #a and cut it
		else: # otherwise
			countdown.write(str(count)) # we write our var "count" increased by 1 as a string
	countdown.close() # we close the file


# Function that prints a selected article when it is called;
# uses random_article.py and its selectRandomArticle function to pick a random article
def printFile():
	# On vérifie si countdown est vide ou non et s'il l'est, on le remet à 0
	check.fileSize()
	
	# RANDOM PRINTING
	article = random_article.selectRandomArticle()
	article= Image.open(article)
	article = article.rotate(180)
	p.image(article) # article is the fullpath of the selected article
	p.cut()
	#p.image("/home/pi/Documents/lectura-plus/assets/marge-ticket.jpg")


	# COUNTING
	# (for every x printings, we want a special coupon)
	counting()

	# KEEPING TRACK/DEBUG
	countdown = open("countdown.txt") # we open "countdown.txt"
	read_file = countdown.read() # we read it
	print("countdown: "+read_file) # we print what is inside
	countdown.close() # we close the file


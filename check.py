import os

def fileSize():
	countfile = "countdown.txt"
	if os.stat(countfile).st_size == 0:
		print ("empty")
		count = open("countdown.txt", "w+")
		count.write(str(0))
		count.close()	
		print("counting n'est plus vide")
	else:
		print("counting n'est pas vide, keep going")
	

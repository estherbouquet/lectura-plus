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
	data = data.replace('\n## ', '\n# ') #on change h2 en h1
	data = data.replace('\n##### ', '\n## ') #on change h5 en h2
	
	fin.close() # On referme le fichier

	fin = open(myfile, 'w') # On l'ouvre une dernière fois avec les privilèges d'écriture
	fin.write(data) # On  écrit toutes les modifications contenues dans data
	fin.close() # On ferme, ce qui enregistre

#rearrangeMardownOrder('/home/pi/Documents/lectura-plus/articles/ALIMENTATION-18860115-ARROSOIR-p1-la-republique-est-morte.txt')

import os

dossier= '/home/pi/Documents/lectura-plus/input'

for f in os.listdir(dossier):
	os.rename(os.path.join(dossier, f), os.path.join(dossier, f).replace(' ', '-'))


import os, glob
import subprocess
import time

keepGoing = True

while keepGoing:
	drive_list = os.listdir('/media/pi/')
	if 'AJOUT' in drive_list:
		#if len(drive_list) > 0:
		print('cle ajout detectee')
		time.sleep(3) #on attend 3 secondes avant de lancer la suite du programme sinon il va trop vite pour détecter le dossier
		subprocess.call('./copy_from_usb.sh', shell=True)
		"""
		si ajout est toujours détecté
		keepgoing = false
		break
"""
		break
	elif 'SUPPR' in drive_list:
		#if len(drive_list) > 0:
		print('cle suppr detectee')
		time.sleep(3)
		subprocess.call('./delete_from_usb.sh', shell=True)
		break

if ajout
	et if keepgoing = false
		keepGoing = true

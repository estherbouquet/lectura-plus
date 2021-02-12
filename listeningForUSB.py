import os, glob
import subprocess

while True:
	drive_list = os.listdir('/media/pi/')
	if 'AJOUT' in drive_list:
	#if len(drive_list) > 0:
		print('cle ajout detectee')
		subprocess.call('./copy_from_usb.sh', shell=True)
		break
	elif 'SUPPR' in drive_list:
		#if len(drive_list) > 0:
		print('cle suppr detectee')
		subprocess.call('./delete_from_usb.sh', shell=True)
		break
	else:	
		print('USB non detectee')

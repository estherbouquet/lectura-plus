import os, glob
import subprocess

while True:
	drive_list = os.listdir('/media/pi/')
	if 'KEVCHA' in drive_list:
	#if len(drive_list) > 0:
		print('cle usb detectee')
		subprocess.call('./copy_from_usb.sh', shell=True)
		break
	else:
		print('USB non detectee')

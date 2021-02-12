import RPi.GPIO as GPIO # Importe communication sur les pins GPIO
from time import sleep # Permet d'éteindre la led au bout de x temps

# On dit au raspberry qu'on utilise le numéros des pins telles que GPIOXX pour communiquer
# schéma : https://cdn-learn.adafruit.com/assets/assets/000/031/833/original/raspberry_pi_gpio-diagram.png?1461025067
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

# Initialisation de la pin GPIO24 (LED verte)
GPIO.setup(24, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

# Initialisation de la pin GPIOXX (LED bleue)
#GPIO.setup(XX, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

# Initialisation de la pin GPIOXX (LED rouge)
#GPIO.setup(XY, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

def tranferEnded(): # F en morse
	GPIO.output(24, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	GPIO.output(24, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	GPIO.output(24, GPIO.HIGH) # Alllume la LED
	sleep(1) # Eteint la LED 	
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	GPIO.output(24, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	GPIO.cleanup()
	
def turnOnGreen():
	GPIO.output(24, GPIO.HIGH) # Alllume la LED

def turnOffGreen():
	GPIO.output(24, GPIO.LOW)
	GPIO.cleanup() # Nettoie les ports utilisés 
	

def pushedButtonDetected():
	for i in range(2):
		GPIO.output(XX, GPIO.HIGH) # Alllume la LED
		sleep(0.2) # Eteint la LED 	
		GPIO.output(XX, GPIO.LOW)
		sleep(0.2)
	GPIO.cleanup()

def turnOnBlue():
	GPIO.output(XX, GPIO.HIGH) # Alllume la LED

def turnOffBlue():
	GPIO.output(XX, GPIO.LOW)
	GPIO.cleanup() # Nettoie les ports utilisés 

def errName():
	for i in range(2):
		GPIO.output(XY, GPIO.HIGH)
		sleep(1)
		GPIO.output(XY, GPIO.LOW)
		sleep(0.5)
	 
	GPIO.cleanup() # Nettoie les ports utilisés 
	
def errDirMissing(): #dossier articles manquant sur clé usb AJOUT
	for i in range(8):
		GPIO.output(XY, GPIO.HIGH) # Alllume la LED
		sleep(0.1) # Eteint la LED 	
		GPIO.output(XY, GPIO.LOW)
		sleep(0.1)

	GPIO.cleanup() 
	
def errFileMissing(): #fichier suppression.txt manquant sur clé usb SUPPR
	for i in range(4):
		GPIO.output(24, GPIO.HIGH) # Alllume la LED
		sleep(0.1) # Eteint la LED 	
		GPIO.output(24, GPIO.LOW)
		sleep(0.1)
		GPIO.output(24, GPIO.HIGH) # Alllume la LED
		sleep(0.5) # Eteint la LED 	
		GPIO.output(24, GPIO.LOW)
		sleep(0.1)

	GPIO.cleanup() 


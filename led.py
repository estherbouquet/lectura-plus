import RPi.GPIO as GPIO # Importe communication sur les pins GPIO
from time import sleep # Permet d'éteindre la led au bout de x temps

# On dit au raspberry qu'on utilise le numéros des pins telles que GPIOXX pour communiquer
# schéma : https://cdn-learn.adafruit.com/assets/assets/000/031/833/original/raspberry_pi_gpio-diagram.png?1461025067
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

# Initialisation de la pin GPIO24 (LED verte)
GPIO.setup(21, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

# Initialisation de la pin GPIOXX (LED bleue)
GPIO.setup(16, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

# Initialisation de la pin GPIOXX (LED rouge)
GPIO.setup(25, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

# Initialisation de la pin GPIOXX (LED yellow)
GPIO.setup(12, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

def tranferEnded(): # F en morse
	GPIO.output(21, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(21, GPIO.LOW)
	sleep(0.2)
	GPIO.output(21, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(21, GPIO.LOW)
	sleep(0.2)
	GPIO.output(21, GPIO.HIGH) # Alllume la LED
	sleep(1) # Eteint la LED 	
	GPIO.output(21, GPIO.LOW)
	sleep(0.2)
	GPIO.output(21, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(21, GPIO.LOW)
	sleep(0.2)
	GPIO.cleanup()
	
def turnOnGreen():
	GPIO.output(21, GPIO.HIGH) # Alllume la LED

def turnOffGreen():
	GPIO.output(21, GPIO.LOW)
	#GPIO.cleanup() # Nettoie les ports utilisés 
	

def pushedButtonDetected():
	for i in range(2):
		GPIO.output(16, GPIO.HIGH) # Alllume la LED
		sleep(0.2) # Eteint la LED 	
		GPIO.output(16, GPIO.LOW)
		sleep(0.2)
	GPIO.cleanup()

def turnOnBlue():
	GPIO.output(16, GPIO.HIGH) # Alllume la LED

def turnOffBlue():
	GPIO.output(16, GPIO.LOW)
	#GPIO.cleanup() # Nettoie les ports utilisés 

def errName():
	for i in range(2):
		GPIO.output(25, GPIO.HIGH)
		sleep(1)
		GPIO.output(25, GPIO.LOW)
		sleep(0.5)
	 
	GPIO.cleanup() # Nettoie les ports utilisés 
	
def errDirMissing(): #dossier articles manquant sur clé usb AJOUT
	for i in range(8):
		GPIO.output(25, GPIO.HIGH) # Alllume la LED
		sleep(0.1) # Eteint la LED 	
		GPIO.output(25, GPIO.LOW)
		sleep(0.1)

	GPIO.cleanup() 
	
def errFileMissing(): #fichier suppression.txt manquant sur clé usb SUPPR
	for i in range(4):
		GPIO.output(25, GPIO.HIGH) # Alllume la LED
		sleep(0.1) # Eteint la LED 	
		GPIO.output(25, GPIO.LOW)
		sleep(0.1)
		GPIO.output(25, GPIO.HIGH) # Alllume la LED
		sleep(0.5) # Eteint la LED 	
		GPIO.output(25, GPIO.LOW)
		sleep(0.1)

	GPIO.cleanup()

def turnOnRed():
	GPIO.output(25, GPIO.HIGH) # Alllume la LED

def turnOffRed():
	GPIO.output(25, GPIO.LOW)
	#GPIO.cleanup() # Nettoie les ports utilisés 


def dirImagesDeleted():
	turnOnRed()
	sleep(0.2)
	turnOnYellow()
	sleep(0.2)
	turnOnBlue()
	sleep(0.2)
	turnOnGreen()
	sleep(1)
	turnOffGreen()
	turnOffBlue()
	turnOffYellow()
	turnOffRed()
	GPIO.cleanup()
	
def cleanLed():
	GPIO.cleanup()	
	
def turnOnYellow():
	GPIO.output(12, GPIO.HIGH) # Alllume la LED

def turnOffYellow():
	GPIO.output(12, GPIO.LOW)
	#GPIO.cleanup() # Nettoie les ports utilisés 

'''
def turnOn():
	GPIO.output(24, GPIO.HIGH) # Alllume la LED

def blink():
	GPIO.output(24, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	GPIO.output(24, GPIO.HIGH) # Alllume la LED
	sleep(0.2) # Eteint la LED 	
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)

def turnOff():
	GPIO.output(24, GPIO.LOW)
	GPIO.cleanup() # Nettoie les ports utilisés 

def problem():
	GPIO.output(24, GPIO.HIGH)
	sleep(0.2)
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	
	GPIO.output(24, GPIO.HIGH)
	sleep(0.2)
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	GPIO.output(24, GPIO.HIGH)
	sleep(0.2)
	GPIO.output(24, GPIO.LOW)
	sleep(0.2)
	 
	GPIO.cleanup() # Nettoie les ports utilisés 
'''

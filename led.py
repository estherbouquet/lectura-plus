import RPi.GPIO as GPIO # Importe communication sur les pins GPIO
from time import sleep # Permet d'éteindre la led au bout de x temps

# On dit au raspberry qu'on utilise le numéros des pins telles que GPIOXX pour communiquer
# schéma : https://cdn-learn.adafruit.com/assets/assets/000/031/833/original/raspberry_pi_gpio-diagram.png?1461025067
GPIO.setmode(GPIO.BCM) 

# Initialisation de la pin GPIO24 (LED)
GPIO.setup(24, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

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

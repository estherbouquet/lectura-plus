import RPi.GPIO as GPIO # Importe communication sur les pins GPIO
import time # Permet d'éteindre la led au bout de x temps
import print # Importe le fichier print.py qui est normalement dans le même dossier
import led

# On dit au raspberry qu'on utilise le numéros des pins telles que GPIOXX pour communiquer
# schéma : https://cdn-learn.adafruit.com/assets/assets/000/031/833/original/raspberry_pi_gpio-diagram.png?1461025067
GPIO.setmode(GPIO.BCM) 
# (possibilité de communiquer via le numéro des pins directement avec)
#GPIO.setmode(GPIO.BOARD)

# Initialisation de la pin GPIO23 (bouton) et GPIO24 (LED).
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO.IN -> on écoute sur la pin (INPUT) | pull_up_down=GPIO.PUD_UP -> le raspberry gère ici le pull up pour éviter de lire un input avec des interférences entre 0 et 1
GPIO.setup(24, GPIO.OUT) # GPIO.OUT -> on envoie sur la pin (OUTPUT), ce qui allumera la LED

try: # Essaie d'exécuter ce code...
	while True:
		button_state = GPIO.input(23) # On lit le statut de la pin 23 et le met dans une variable (soit 1 soit 0)
		if button_state == False: 
			#print('button pressed')
			led.blink()
			print.printFile() # Lance la fonction dans le fichier print.py qui lance l'impression
		else:
			GPIO.output(24, False) # Garde la LED éteinte
				
except: # ... et si tu rencontres une erreur 
	GPIO.cleanup() # Nettoie les ports utilisés 

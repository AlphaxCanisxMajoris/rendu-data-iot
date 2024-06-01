from machine import Pin#importer partiellement le module machine pour avoir accès aux pins GPIO.
import time#importer le module de temps. Cela nous permettra d’utiliser des tâches liées au temps.
 
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)#ici, nous définissons la broche du capteur (=GP22) comme une broche d’entrée. Pour éviter une entrée “flottante”, nous utilisons une résistance de tirage interne.
n = 0
 
print('Starting up the PIR Module')
time.sleep(1)#On attend 1 seconde pour être certain que le capteur soit stabilisé.
print('Ready')
 
while True:#est une boucle à l’infinie (jusqu’à ce que nous interrompons le programme).
     if pir.value() == 1:#si la broche PIR est haute (le capteur a détecté un mouvement)
          n = n+1
          print('Motion Detected ',n)
     time.sleep(1)#On attend 1 seconde avant de poursuivre la boucle
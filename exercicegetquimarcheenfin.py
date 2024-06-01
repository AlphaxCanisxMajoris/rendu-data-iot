from machine import Pin, PWM
import utime
import network
import urequests
import ujson
import random

#Configuration du WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#Définition des couleurs avec PWM
rouge = PWM(Pin(17, mode=Pin.OUT))
rouge.freq(1_000)
rouge.duty_u16(0)

vert = PWM(Pin(18, mode=Pin.OUT))
vert.freq(1_000)
vert.duty_u16(0)

bleu = PWM(Pin(16, mode=Pin.OUT))
bleu.freq(1_000)
bleu.duty_u16(0)

# Informations du réseau WiFi
ssid = 'Sirius'
password = 'chartres528'
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Connexion en cours...")
    utime.sleep(1)

print("Connecté au WiFi")

#URL de l'API pour récupérer les informations des personnages
url = "https://hp-api.lainocs.fr/characters"

#Dictionnaire des couleurs des maisons
houses = {"Gryffindor": (500, 30000, 500),
    "Slytherin": (30000, 1000 , 1000),
    "Hufflepuff": (int((227*30000)/255), 20000, 1000),
    "Ravenclaw": (500, 500, 50000),
    "": (30000, 30000, 30000)#pas de maison
}

#Boucle principale pour récupérer et traiter les données
while True:
    try:
        print("Récupération des données...")
        response = urequests.get(url)#Requête GET à l'API
        characters = response.json()#Convertit la réponse JSON en un objet Python
        response.close()

        if characters:
            character = random.choice(characters)
            name = character.get("name")
            house = character.get("house", "")

            print(f"Nom: {name}, Maison: {house}")

            colors = houses.get(house, (30000, 30000, 30000)) #Récupère les couleurs
            rouge.duty_u16(colors[0])
            vert.duty_u16(colors[1])
            bleu.duty_u16(colors[2])

        utime.sleep(1)
    except Exception as e:
        print("Erreur:", e)
        utime.sleep(1)
   
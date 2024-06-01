from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 18 # declaration d'une variable pinNumber à 18
pinNumber2 = 21
pinNumber3 = 27
led = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on précise que c'est une pin de sortie de courant (OUT)

led2 = Pin(pinNumber2, mode=Pin.OUT)
led3 = Pin(pinNumber3, mode=Pin.OUT)


try:
    while True:          # boucle infini
        utime.sleep(0.5)
        led.toggle()#changement d'état de la led
        utime.sleep(0.5)#temps
        led.toggle()
        led2.toggle()
        utime.sleep(0.5)
        led2.toggle()
        led3.toggle()
        utime.sleep(0.5)
        led3.toggle()
except KeyboardInterupt :
    led.off()
    led2.off()
    led3.off()



    #led.on()        allume la led 
    #led.off()       eteind la led

import RPi.GPIO as gpio
import time
TRIG = 12
ECHO = 16




def distance(measure):
    gpio.setmode(gpio.BOARD)
    gpio.setup(TRIG, gpio.OUT)
    gpio.setup(ECHO, gpio.IN)
    
    gpio.output(TRIG, False)

    gpio.output(TRIG, True) 
    time.sleep(0.00001) 
    gpio.output(TRIG, False)
    
    sig = 0
    nosig = 0 
    while gpio.input(ECHO) == 0:
	nosig = time.time()
        

    while gpio.input(ECHO) == 1:
	sig = time.time()
   
    if nosig != None and sig != None:
        tl = sig - nosig

    distance = tl * 17150
    distance = round(distance, 2)
    gpio.cleanup()
    return distance



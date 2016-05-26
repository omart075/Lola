import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import pygame
import sonar


pygame.init()
pygame.display.set_mode([100,100])

def init():

    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
def forward(t):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(t)
    gpio.cleanup()
def reverse(t):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(t)
    gpio.cleanup()

def rightTurn(t):
    gpio.output(7, False)
    gpio.output(11,True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(t)
    gpio.cleanup()

def leftTurn(t):
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(t)
    gpio.cleanup()

def getChar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)

    termios.tcsetattr(fd, termios.TCSADRAIN,old_settings)
    return ch

def update():
  
	#wtf????
    distance = sonar.distance('cm')
    print distance
    for event in pygame.event.get():
	if event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_w:
	        pass
		    #init()
		    #forward(0.03)	
     

   
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_w] and distance > 30:
        init()
        forward(0.03)
    if keystate[pygame.K_s]:
        init()
        reverse(0.03)
    if keystate[pygame.K_d]:
        init()
        rightTurn(0.03)
    if keystate[pygame.K_a]:
	init()
	leftTurn(0.03)
    if keystate[pygame.K_q]:
        sys.exit()




#def key_input(event):
    
#    print 'Key:', event.char
#    key_press = event.char
#    if key_press.lower() == 'w':
#        init()
#        forward(0.030)
#
#    elif key_press.lower() == 's':
#        init()
#        reverse(0.030)
   # elif key_press.lower() == 'd':
  #      init()
 #       rightTurn()
 #   elif key_press.lower() == 'a':
#	init()
 #       leftTurn()
 #   elif key_press.lower() == 'q':
 #       gpio.cleanup()
 #       sys.exit(1)   

#command = tk.Tk()
#command.bind('<KeyPress>', key_input)
#command.mainloop()



#forward()
#time.sleep(1)
#reverse()
#time.sleep(1)
#rightTurn()
#time.sleep(1)
while True:
    update()


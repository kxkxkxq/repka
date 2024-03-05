import RPi.GPIO as G
import time 

G.setmode(G.BCM) 
G.setup(25, G.OUT)

G.output(25, 1)
time.sleep(1)
G.output(25, 0) 



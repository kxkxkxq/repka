import RPi.GPIO as G
import time 

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 0, 0, 0, 0, 0, 1, 0]

G.setmode(G.BCM)
G.setup(dac, G.OUT)

G.output(dac, number)
time.sleep(10)
G.output(dac, 0)
G.output(dac, G.OUT)

G.cleanup()
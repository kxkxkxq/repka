import RPi.GPIO as G
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]
G.setmode(G.BCM)
G.setup(leds, G.OUT)

for i in range(3):
    for j in range(8):
        G.output(leds[j], 1)
        time.sleep(0.1)
        G.output(leds[j], 0)
G.output(leds, G.OUT)
G.cleanup()        
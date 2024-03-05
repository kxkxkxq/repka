import RPi.GPIO as G
import time

G.setwarnings(False)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

G.setmode(G.BCM)
G.setup(leds, G.OUT)
G.setup(aux, G.IN)

while True:
    for i in range(8):
        G.output(leds[i], G.input(aux[i]))

G.output(leds, 0)
G.cleanup()
G

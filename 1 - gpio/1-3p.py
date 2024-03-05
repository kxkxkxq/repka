import RPi.GPIO as G

G.setmode(G.BCM)

G.setup(20, G.IN)
G.setup(24,G.OUT)


G.output(24, G.input(20))

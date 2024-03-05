import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)

PIN = 20
FREQ = 2

IO.setup(PIN, IO.OUT)

for i in range(100):
    IO.output(PIN, 0)
    time.sleep(0.5 / FREQ)
    
    IO.output(PIN, 1)
    time.sleep(0.5 / FREQ)
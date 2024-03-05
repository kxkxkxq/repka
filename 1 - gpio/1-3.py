import RPi.GPIO as IO

IO.setmode(IO.BCM)

IN_PIN  = 20
OUT_PIN = 21

IO.setup(IN_PIN, IO.IN)
IO.setup(OUT_PIN, IO.OUT)

IO.output(OUT_PIN, IO.input(IN_PIN))
import RPi.GPIO as G
import time 

dac = [8, 11, 7, 1, 0, 5, 12, 6]
G.setwarnings(False)
G.setmode(G.BCM)
G.setup(dac, G.OUT)

def func(num):
    d = [0 , 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while num:
        if(num & 1):
            d[i] = 1
        else:
            d[i] = 0
        num >>= 1
        i = i + 1
    d.reverse()
    return d

t = int(input())
num = 0
flag = 1


try:
    while True:
       

        print((num / 256) * 3.3)
        if num < 0:
            print("num < 0")
        if num > 255:
            print("num > 255")
        if 0 <= num <= 255:        
            G.output(dac, func(num))
            if num == 255:
                flag = -1
            if num == 0:
                flag = 1 
            num = num + flag 

            time.sleep(t/1000)       

        if num == "q": break
finally:
    G.output(dac, 0)
    G.cleanup()
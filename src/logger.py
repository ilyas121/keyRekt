import keyboard
import time

STOP_TIME = 10

def printKey(keyEvent):
    print(keyEvent)

recorded = keyboard.hook(printKey)

a = time.time()
b= time.time()
while b - a < STOP_TIME:
    b = time.time()

import keyboard
import time
import os
from wordMatch import match

TIME_THRESHOLD = 0.3
lastTimeUp = -1
traces = []
wordsOut = []
word = ""
def cleanKeyName(keyEventStr):
    newStr = keyEventStr[13:]
    newStr = newStr[1:]
    newStr = newStr[:-1]
    return newStr

def logKey(keyEvent):
    global lastTimeUp
    global word
    keyTime = keyEvent.time
    keyName = cleanKeyName(str(keyEvent))
    direction = keyName.split(" ")[1]
    if keyName.split(" ")[0] == "space":
        traces.append(word)
        print(word)
        word = ""
    if direction == "up":
        word += keyName.split(" ")[0]
    lastTimeUp = keyTime

recorded = keyboard.hook(logKey)

a = time.time()
b = time.time()

while b - a < 60:
    b = time.time()
    if lastTimeUp == -1:
        pass
    elif (time.time() - lastTimeUp) >= TIME_THRESHOLD:
        if word != "":
            if word[0] == '-':
                word = word[2:]
            traces.append(word)
            toPrint = match(word)
            if toPrint == 'None':
            	print(word)
            else:
            	print(toPrint)
            word = ""

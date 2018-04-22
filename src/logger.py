import keyboard
import time
from wordMatch import match

TIME_THRESHOLD = 0.3
lastTimeUp = -1
traces = []
wordsOut = []
word = "-1"
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
    # print(str(keyTime) + " " + str(keyName))
    direction = keyName.split(" ")[1]
    if direction == "up":
        # print("UPPPP")
        word += keyName.split(" ")[0]
    lastTimeUp = keyTime

recorded = keyboard.hook(logKey)

a = time.time()
b = time.time()

while (b - a) < 20:
    b = time.time()
    # print(time.time() - lastTimeUp)
    if lastTimeUp == -1:
        pass
    elif (time.time() - lastTimeUp) >= TIME_THRESHOLD:
        # print("ALLLIVE")
        if word != "":
            if word[0] == '-':
                word = word[2:]
            traces.append(word)
            wordsOut.append(match(word))
            word = ""


print(word)
print(traces)
print(wordsOut)

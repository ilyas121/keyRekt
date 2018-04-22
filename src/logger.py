import keyboard
import time

TIME_THRESHOLD = 1
lastTimeUp = -1
words = []
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
    print(str(keyTime) + " " + str(keyName))
    direction = keyName.split(" ")[1]
    if direction == "up":
        print("UPPPP")
        lastTimeUp = keyTime
        word += keyName.split(" ")[0]

recorded = keyboard.hook(logKey)

a = time.time()
b = time.time()

while (b - a) < 10:
    global words
    global word
    b = time.time()
    print(time.time() - lastTimeUp)
    if lastTimeUp == -1:
        print("the first")
    elif (time.time() - lastTimeUp) >= TIME_THRESHOLD:
        print("ALLLIVE")
        if word != "":
            words.append(word)
            word = ""


print(word)
print(words)

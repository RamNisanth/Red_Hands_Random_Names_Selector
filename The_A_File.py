import pyttsx3
import random
import time

dictionary = {1:"Pradeep",2:"Vineela",3:"Varun",4:"sai kiran",5:"Nisanth",6:"pavan",7:"Meg",8:"sowmya",9:"None"}
list1 = []

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
speak("Lets Start the Game, press any key to proceed! ")
input()

while(True):
    list1.clear()
    while(len(list1)<8):
        i = random.randrange(1, 9, 1)
        if i not in list1:
            list1.append(i)
    for j in range(8):
        mytext = dictionary[list1[j]]
        speak(mytext)
        time.sleep(1)
    speak("Next Game")
    time.sleep(4)
  
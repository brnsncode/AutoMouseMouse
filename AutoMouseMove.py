import pyautogui
import random
import time

def mousefunction(co1, co2):
    print("Beginning mouse movement")
    print("Moving to coordinates:", co1, co2)
    pyautogui.moveTo(co1, co2, duration = 1) 
    time.sleep(getRandomTime()) 

def getRandomCoordinates():
    x = random.randint(1,1080)
    return x

def getRandomTime():
    t = random.randint(60, 500)
    return t

while(1):
        mousefunction(getRandomCoordinates(), getRandomCoordinates())


from PIL import Image
import os
import time
import pyautogui
import pandas as pd
from datetime import datetime

def findImg(name):
    img = pyautogui.locateOnScreen('AddLocation/'+name, confidence=0.9)
    while img is None :
        print('cannot find '+name+' on screen')
        time.sleep(0.5)
        img = pyautogui.locateOnScreen('AddLocation/'+name, confidence=0.9)
    return img

SalesData = ['UCX-215','UCX-216','UCX-217','UCX-221','UCX-222','UCX-223','UCX-224','UCX-225','UCX-226','UCX-227']
SalesData = ['UCX-215']
for data in SalesData :
    print(data)
    findImg("CheckAX.png")
    
    time.sleep(0.5)
    general = findImg("general.png")
    pyautogui.moveTo(general[0]+10, general[1]+10)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write("TZCF")
    pyautogui.hotkey('tab')
    pyautogui.write("ZCF")
    time.sleep(0.5)
    m = findImg("m.png")
    pyautogui.moveTo(m[0]+80, m[1]+10)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    pyautogui.write(data)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('backspace')
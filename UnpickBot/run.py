from PIL import Image
import os
import time
import pyautogui
import pandas as pd
from datetime import datetime

dataRowLenght = 50
i = 0
while i < dataRowLenght :
    function = pyautogui.locateOnScreen('input/function.png', confidence=0.9)
    while function is None :
        print('cannot find function')
        time.sleep(1)
        function = pyautogui.locateOnScreen('input/function.png', confidence=0.9)

    # click function Button
    pyautogui.moveTo(function[0]+30, function[1]+10)
    pyautogui.click()
    time.sleep(1)

    unpick = pyautogui.locateOnScreen('input/unpick.png', confidence=0.9)
    while unpick is None :
        print('cannot find function')
        time.sleep(1)
        unpick = pyautogui.locateOnScreen('input/unpick.png', confidence=0.9)

    # click function Button
    pyautogui.moveTo(unpick[0]+30, unpick[1]+10)
    pyautogui.click()
    time.sleep(1)


    page = pyautogui.locateOnScreen('input/page.png', confidence=0.9)
    while page is None :
        print('cannot find page')
        time.sleep(1)
        page = pyautogui.locateOnScreen('input/page.png', confidence=0.9)


    unpickQuantity = pyautogui.locateOnScreen('input/unpickQuantity.png', confidence=0.9)
    while unpickQuantity is None :
        print('cannot find unpickQuantity')
        time.sleep(1)
        unpickQuantity = pyautogui.locateOnScreen('input/unpickQuantity.png', confidence=0.9)
    # click function Button
    pyautogui.moveTo(unpickQuantity[0]+140, unpickQuantity[1]+10)
    pyautogui.click()
    time.sleep(1)

    OK = pyautogui.locateOnScreen('input/OK.png', confidence=0.9)
    while OK is None :
        print('cannot find OK')
        time.sleep(1)
        OK = pyautogui.locateOnScreen('input/OK.png', confidence=0.9)
    # click function Button
    pyautogui.moveTo(OK[0]+20, OK[1]+10)
    pyautogui.click()
    time.sleep(1)

    page = pyautogui.locateOnScreen('input/page.png', confidence=0.9)
    while page is not None :
        print('loading')
        time.sleep(1)
        page = pyautogui.locateOnScreen('input/page.png', confidence=0.9)

    i = i + 1
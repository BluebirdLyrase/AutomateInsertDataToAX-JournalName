from PIL import Image
import os
import time
import pyautogui
import pandas as pd
from datetime import datetime

dataFile = pd.read_csv('input/data.csv',header=None,names=['colA'])


#try:
for data in dataFile['colA'] :
    Search = pyautogui.locateOnScreen('input/Select.png', confidence=0.9)
    while Search is None :
        print('cannot find Select')
        time.sleep(1)
        Search = pyautogui.locateOnScreen('input/Select.png', confidence=0.9)
    
    # click Search Button
    pyautogui.moveTo(Search[0]+30, Search[1]+10)
    pyautogui.click()
    time.sleep(1)

    SelectPage = pyautogui.locateOnScreen('input/SelectPage.png', confidence=0.9)
    while SelectPage is None :
        print('waiting for AX')
        time.sleep(1)
        SelectPage = pyautogui.locateOnScreen('input/SelectPage.png', confidence=0.9)

    Relation = pyautogui.locateOnScreen('input/Relation.png', confidence=0.9)
    while Relation is None :
        print('cannot find Relation')
        time.sleep(1)
        Relation = pyautogui.locateOnScreen('input/Relation.png', confidence=0.9)
    
    # click Search Button
    pyautogui.moveTo(Relation[0]+30, Relation[1]+180)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.press('backspace') 
    pyautogui.write(data)
    time.sleep(1)

    SelectBtn = pyautogui.locateOnScreen('input/SelectBtn.png', confidence=0.9)
    while SelectBtn is None :
        print('cannot find SelectBtn')
        time.sleep(1)
        SelectBtn = pyautogui.locateOnScreen('input/SelectBtn.png', confidence=0.9)
    pyautogui.moveTo(SelectBtn[0]+30, SelectBtn[1]+0)
    pyautogui.click()
    time.sleep(1)

    No = pyautogui.locateOnScreen('input/No.png', confidence=0.9)
    while No is None :
        print('cannot find NoBtn')
        time.sleep(1)
        No = pyautogui.locateOnScreen('input/No.png', confidence=0.9)
    pyautogui.moveTo(No[0]+30, No[1]+0)
    time.sleep(3)
    pyautogui.click()
#except:
#    print('Error')
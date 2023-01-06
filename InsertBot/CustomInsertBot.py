import pyautogui
import time
import pandas as pd

time.sleep(5)
dataRowLenght = 2
dataColumnLenght = 8
jCondition = True
#jCondition = j!=3 and j!=6 and j!=7

i = 0
while i < dataRowLenght :

    pyautogui.hotkey('Ctrl','n')
    #pyautogui.hotkey('alt','tab')
    #time.sleep(1)

    j = 0
    while j < dataColumnLenght :
        time.sleep(0.5)
        pyautogui.hotkey('alt','tab') 
        time.sleep(0.5)
        pyautogui.hotkey('Ctrl','c')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        pyautogui.hotkey('alt','tab')
        time.sleep(0.5)
        if(jCondition):
            print(j)
            pyautogui.hotkey('Ctrl','v')
        time.sleep(0.5)
        pyautogui.hotkey('tab')
        time.sleep(0.5)
        j = j + 1
   
    pyautogui.hotkey('alt','tab') 
    time.sleep(0.2)
    pyautogui.hotkey('Enter')
    time.sleep(0.2)
    pyautogui.hotkey('Enter')
    time.sleep(0.2)

    k = 0

    while j < dataColumnLenght : 
        pyautogui.press('left') 
        k = k + 1
    time.sleep(0.5)
    pyautogui.hotkey('alt','tab') 
    time.sleep(0.5)
    i = i + 1
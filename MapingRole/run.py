from PIL import Image
import os
import time
import pyautogui
import win32gui
import winsound

i = 0
dataLenght = 2


def wait() :
    x = win32gui.GetCursorInfo()
    print(x[1])
    while x[1] == 3671547 :
        x = win32gui.GetCursorInfo()
        print(x[1])
        time.sleep(1)

time.sleep(4)

while i < dataLenght :
    havechild = False
    pyautogui.press('right')
    time.sleep(1)

    wait()

    SetChild = pyautogui.locateOnScreen('input/SetChild.png', confidence=0.9)
    count = 1
    while SetChild is None and count < 3:
        print('cannot find SetChild')
        time.sleep(1)
        SetChild = pyautogui.locateOnScreen('input/SetChild.png', confidence=0.9) 
        count = count+1
        
    FullControl = pyautogui.locateOnScreen('input/FullControl.png', confidence=0.9)

    while FullControl is None:
        print('cannot find FullControl')
        time.sleep(1)
        FullControl = pyautogui.locateOnScreen('input/FullControl.png', confidence=0.9)    
    pyautogui.moveTo(FullControl[0]+10, FullControl[1]+10)
    pyautogui.click()
    time.sleep(3)

    if((SetChild is not None)):
        havechild = True
        pyautogui.moveTo(SetChild[0]+10, SetChild[1]+10)
        pyautogui.click()
        wait()
    time.sleep(1)

    pyautogui.moveTo(FullControl[0]-60, FullControl[1])
    pyautogui.click()
    time.sleep(1)

    if(havechild) :
        pyautogui.press('left')
        time.sleep(1)
    
    pyautogui.press('down')
    i = i+1

duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)

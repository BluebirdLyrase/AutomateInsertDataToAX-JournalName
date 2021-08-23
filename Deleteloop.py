import pyautogui
import time
import pandas as pd

i=0
time.sleep(5)
while i < 50 :
    pyautogui.hotkey('ALT','F9')
    # time.sleep(1)
    pyautogui.press('left') 
    # time.sleep(1)
    pyautogui.press('Enter') 
    # time.sleep(1)
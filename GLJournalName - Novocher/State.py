import pyautogui
import time
import pandas as pd

time.sleep(10)

i = 0
while i < 77 :
    pyautogui.hotkey('Ctrl','c')
    time.sleep(1)
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.hotkey('Ctrl','n')
    time.sleep(1)
    pyautogui.hotkey('Ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('Ctrl','c')
    time.sleep(1)
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('Ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    pyautogui.press('left') 
    time.sleep(1)
    i = i + 1
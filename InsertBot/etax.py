import pyautogui
import time
import pandas as pd
   
df = pd.read_csv('input/e-tax.csv')
print('finish reading data')
time.sleep(5)
w = 0.3
# pyautogui.hotkey('alt','tab')
for ind in df.index:
    pyautogui.hotkey('ctrl','n')
    time.sleep(w)
    pyautogui.write('Admin')
    time.sleep(w)
    pyautogui.hotkey('tab')
    time.sleep(w)
    pyautogui.write('2/18/2021')
    time.sleep(w)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(w)
    pyautogui.write('06:25:47')
    time.sleep(w)
    pyautogui.hotkey('tab')
    time.sleep(w)
    pyautogui.write('None')
    time.sleep(w)
    pyautogui.hotkey('tab')
    time.sleep(w)
    pyautogui.hotkey('tab')
    time.sleep(w)
    pyautogui.write(df['salesid'][ind])
    time.sleep(w)
    pyautogui.hotkey('tab')
    time.sleep(w)
    pyautogui.write((df['Invoiceid'][ind]))
    time.sleep(0.3)
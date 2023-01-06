import pyautogui
import time
import pandas as pd
   
df = pd.read_csv('input/E-receipt.csv')
print('finish reading data')
time.sleep(5)
# pyautogui.hotkey('alt','tab')
for ind in df.index:
    pyautogui.hotkey('ctrl','n')
    time.sleep(0.3)    
    pyautogui.hotkey('tab')
    pyautogui.write('Group')
    pyautogui.hotkey('tab')
    time.sleep(0.3)
    group = pyautogui.locateOnScreen('input/group.png', confidence=0.9)    
    while group is None:
        print('cannot find group')
        time.sleep(1)
        group = pyautogui.locateOnScreen('input/group.png', confidence=0.9)
    pyautogui.moveTo(group[0]+20, group[1]+10)    
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.hotkey('Enter')
    pyautogui.write('Listprice')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.write(df['item'][ind])
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.write(str(df['price'][ind]))
    pyautogui.hotkey('tab')
    pyautogui.write('12/6/2021')
    time.sleep(0.3)

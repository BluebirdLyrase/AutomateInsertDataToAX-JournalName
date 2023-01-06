import pyautogui
import time
i = 0
while True :

    code = pyautogui.locateOnScreen('input/code.png', confidence=0.9)
    if(i > 15) :
        while code is None:
            print('cannot find All')
            time.sleep(1)
            code = pyautogui.locateOnScreen('input/code.png', confidence=0.9) 
        pyautogui.moveTo(code[0]+20, code[1]+10) 
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        i = 0  
    All = pyautogui.locateOnScreen('input/All.png', confidence=0.9)    
    while All is None:
        print('cannot find All')
        time.sleep(1)
        All = pyautogui.locateOnScreen('input/All.png', confidence=0.9)    
    pyautogui.moveTo(All[0]+20, All[1]+10)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('Group')
    time.sleep(1)
    pyautogui.moveTo(All[0]+100, All[1]+10)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('Listprice')
    i = i + 1
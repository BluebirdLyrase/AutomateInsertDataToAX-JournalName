
from PIL import Image
import os
import time
import pyautogui
import win32gui
import winsound

def wait() :
    x = win32gui.GetCursorInfo()
    print(x[1])
    while x[1] == 3671547 or x[1] == 221708881 or x[1] == 781190799 :
        x = win32gui.GetCursorInfo()
        print(x[1])
        time.sleep(1)

time.sleep(3)
wait()

duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
import keyboard
import pyautogui
import time

isClicking = False

def setClicker():
    global isClicking

    if isClicking:
        isClicking = False
        print('Clicker is not working...')
    else:
        isClicking = True
        print('Clicker is working...')



keyboard.add_hotkey('X + C', setClicker)

while True:
    if isClicking:
        pyautogui.click()
        time.sleep(900)
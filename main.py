import pyautogui
from time import sleep
from global_hotkeys import *

def ClickButtons(name, c = 0.9):
    for btn in pyautogui.locateAllOnScreen('img/' + name + '.png', confidence = c):

        if (work == False):
            break
            
        pyautogui.moveTo(btn)
        pyautogui.click()
        sleep(1)

def ClickButton(name):

    if (work == False):
        return False

    print('Clicking ' + name)
    btn = pyautogui.locateOnScreen('img/' + name + '.png', confidence = 0.9)
    if btn == None:
        return False
    else:
        pyautogui.moveTo(btn)
        pyautogui.click()
        return True

work = True

def CloseProgram():
    print('Closing program...')
    global work
    work = False

def RegisterHotkeyForClose():
    #idk if there any way to create one hotkey instead of array
    hotkeys = [ 
    [["shift", "t"], None, CloseProgram],
    ]

    register_hotkeys(hotkeys)
    start_checking_hotkeys()

if __name__ == '__main__':
    print('FOE auto help working')

    RegisterHotkeyForClose()

    ClickButton('home')
    ClickButton('back')
    sleep(2) # sleep here need for wait loading buttons

    for _ in range(1, 15):
        ClickButtons('btn')
        ClickButton('next')

    ClickButton('clan')
    ClickButton('back')
    sleep(2)

    for _ in range(1, 15):
        ClickButtons('btn')
        ClickButton('next')

    ClickButton('friends')
    ClickButton('back')
    sleep(2)

    for _ in range(1, 15):
        ClickButtons('btn')
        ClickButtons('tavern')
        ClickButton('next')
    
    print('FOE auto help ended!')
    
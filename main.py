import pyautogui
from time import sleep

def ClickHelpButtons():
    availableButton = True
    while availableButton == True:
        sleep(1)

        btn = pyautogui.locateOnScreen('img/btn.png', confidence = 0.7)

        if btn == None:
            availableButton = False
        else:
            pyautogui.moveTo(btn)
            pyautogui.click()

def ClickTavernButtons():
    availableButton = True
    while availableButton == True:
        sleep(1)

        btn = pyautogui.locateOnScreen('img/tavern.png', confidence = 0.7)

        if btn == None:
            availableButton = False
        else:
            pyautogui.moveTo(btn)
            pyautogui.click()

def ClickButton(name):

    print('Clicking ' + name)
    btn = pyautogui.locateOnScreen('img/' + name + '.png', confidence = 0.9)
    if (btn == None):
        return False
    else:
        pyautogui.moveTo(btn)
        pyautogui.click()
        return True

if __name__ == '__main__':
    print('FOE auto help working')

    ClickButton('home')
    ClickButton('back')

    while ClickButton('next') == True:
        ClickHelpButtons()

    ClickButton('friends')
    ClickButton('back')

    while ClickButton('next') == True:
        ClickHelpButtons()
        ClickTavernButtons()

    ClickButton('clan')
    ClickButton('back')

    while ClickButton('next') == True:
        ClickHelpButtons()
        ClickTavernButtons()
    
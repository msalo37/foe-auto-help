import pyautogui
from time import sleep

def ClickButtons(name):
    availableButton = True
    while availableButton == True:
        sleep(1)

        btn = pyautogui.locateOnScreen('img/' + name + '.png', confidence = 0.7)

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
        ClickButtons('btn')

    ClickButton('friends')
    ClickButton('back')

    while ClickButton('next') == True:
        ClickButtons('btn')
        ClickButtons('tavern')

    ClickButton('clan')
    ClickButton('back')

    while ClickButton('next') == True:
        ClickButtons('btn')

    print('FOE auto help ended!')
    
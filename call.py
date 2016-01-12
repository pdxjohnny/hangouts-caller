import sys
import time
import pyautogui

TYPE_INTERVAL = 0.02

def sign_in(email, password):
    # Go to google hangouts
    location = pyautogui.locateOnScreen('firefox-search.png')
    if location is None:
        assert False, 'Could not find address bar'
    pyautogui.moveTo(location[0] - (location[2] * 2), location[1] + (location[3] / 2))
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('https://hangouts.google.com/', interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(2)
    # Sign in
    location = pyautogui.locateOnScreen('google-sign-in.png')
    if location is None:
        print'Could not find sign in'
        return
    pyautogui.moveTo(location[0] + (location[2] / 2), location[1] + (location[3] / 2))
    pyautogui.click()
    time.sleep(2)
    pyautogui.typewrite(email, interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite(password, interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(1)

def callnumber(number):
    # Go to phone
    location = pyautogui.locateOnScreen('hangouts-search.png')
    if location is None:
        assert False, 'Could not find hangouts search'
    pyautogui.moveTo(location[0] + (location[2] * 2), location[1] + (location[3] / 2))
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(number, interval=TYPE_INTERVAL) # type with quarter-second pause in between each key
    pyautogui.press('enter')
    time.sleep(1)
    location = pyautogui.locateOnScreen('call-button.png')
    if location is None:
        assert False, 'Could not find call button'
    pyautogui.moveTo(location[0] + (location[2] / 2), location[1] + (location[3] / 2))
    pyautogui.click()
    # pyautogui.typewrite('https://hangouts.google.com/') # type with quarter-second pause in between each key
    # pyautogui.press('enter')
    # time.sleep(5)
    # screenWidth, screenHeight = pyautogui.size()
    # currentMouseX, currentMouseY = pyautogui.position()
    # pyautogui.moveTo(100, 300)
    # pyautogui.click()
    # pyautogui.moveTo(200, 300)
    # pyautogui.click()
    # pyautogui.typewrite(number) # type with quarter-second pause in between each key
    # pyautogui.moveRel(None, 10) # move mouse 10 pixels down
    # pyautogui.doubleClick()
    # pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad) # use tweening/easing function to move mouse over 2 seconds.
    # pyautogui.press('esc')
    # pyautogui.keyDown('shift')
    # pyautogui.typewrite(['left', 'left', 'left', 'left', 'left', 'left'])
    # pyautogui.keyUp('shift')
    # pyautogui.hotkey('ctrl', 'c')

def main():
    sign_in(sys.argv[1], sys.argv[2])
    time.sleep(2)
    callnumber(sys.argv[3])

if __name__ == '__main__':
    main()

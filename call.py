import sys
import time
import pyautogui

TYPE_INTERVAL = 0.05

def navigate(url):
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

def allow_plugin_always():
    location = pyautogui.locateOnScreen('allow-plugin.png')
    if location is None:
        print'Could not find plugin button'
        return
    button_center = (location[0] + (location[2] / 2), \
        location[1] + (location[3] / 2))
    pyautogui.moveTo(button_center[0], button_center[1])
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(button_center[0] + 220, button_center[1] + 110)
    pyautogui.click()

def click_sign_in():
    # Sign in
    location = pyautogui.locateOnScreen('google-sign-in.png')
    if location is None:
        print'Could not find sign in'
        return
    pyautogui.moveTo(location[0] + (location[2] / 2), location[1] + (location[3] / 2))
    pyautogui.click()

def sign_in(email, password):
    pyautogui.typewrite(email, interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite(password, interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(1)

def callnumber(number):
    pyautogui.typewrite(number, interval=TYPE_INTERVAL) # type with quarter-second pause in between each key
    pyautogui.press('enter')
    time.sleep(1)
    location = pyautogui.locateOnScreen('call-button.png')
    if location is None:
        assert False, 'Could not find call button'
    pyautogui.moveTo(location[0] + (location[2] / 2), location[1] + (location[3] / 2))
    pyautogui.click()

def main():
    sign_in(sys.argv[1], sys.argv[2])
    time.sleep(10)
    allow_plugin_always()
    time.sleep(5)
    pyautogui.moveRel(0, 20)
    pyautogui.click()
    time.sleep(1)
    callnumber(sys.argv[3])

if __name__ == '__main__':
    main()

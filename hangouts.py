import sys
import time
import thread
import pyautogui
import subprocess

import states

TYPE_INTERVAL = 0.05

def notify_browser_started(connection):
    '''
    Sleeps for a while to ensure the browser will be set up. Then notifys caller
    object that it is ready to login.
    '''
    # Sleep
    time.sleep(10)
    # Notify that we are ready to login.
    connection.set_state(states.LOGIN)

def start_browser(connection):
    '''
    Starts firefox at hangouts.google.com then returns the process handle. It
    also starts a thread that will notify the main thread via the websocket. It
    sends a message which is echoed back to the socket. Which tells it the
    browser is ready for use.
    '''
    # Argumments for starting the browser
    args = [
        '/usr/bin/firefox',
        'https://accounts.google.com/ServiceLogin?continue=https://hangouts.google.com'
    ]
    # Start the browser
    process = subprocess.Popen(args)
    # Notify when startup is complete
    thread.start_new_thread(notify_browser_started, (connection,))
    # Return a handle on the browser process
    return process

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
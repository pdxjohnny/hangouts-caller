import os
import sys
import time
import shutil
import thread
import pyautogui
import subprocess

import states

TYPE_INTERVAL = 0.05
DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(DIR, 'images')

def image(name):
    return os.path.join(IMAGE_DIR, name)

def notify_browser_started(connection):
    '''
    Sleeps for a while to ensure the browser will be set up. Then notifys caller
    object that it is ready to login.
    '''
    # Sleep
    time.sleep(30)
    # Notify that we are ready to login.
    connection.set_state(states.LOGIN)

def start_browser(connection):
    '''
    Starts firefox at hangouts.google.com then returns the process handle. It
    also starts a thread that will notify the main thread via the websocket. It
    sends a message which is echoed back to the socket. Which tells it the
    browser is ready for use.
    '''
    # Remove all firefox settings so we get a clean start
    path_to = os.path.expanduser(os.path.join('~', '.mozilla'))
    try:
        shutil.rmtree(path_to)
    except:
        # If we can't remove it its because its not there so dont worry
        pass
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

def allow_plugin_always():
    location = pyautogui.locateOnScreen(image('allow-plugin.png'))
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
    time.sleep(2)

def sign_in(email, password):
    pyautogui.typewrite(email, interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite(password, interval=TYPE_INTERVAL)
    pyautogui.press('enter')
    time.sleep(3)

def callsetup():
    # Hangouts rotates through a few lines of text in its search bar
    # any of them coudl be displayed so check them all and click if found
    search_bar_options = [
        image('hangouts-search.png'), \
        image('hangouts-search-2.png')
    ]
    for option in search_bar_options:
        location = pyautogui.locateOnScreen(option)
        if location is None:
            print'Could not find ' + option + ' input area'
            continue
        location_x, location_y = pyautogui.center(location)
        pyautogui.click(location_x, location_y)
    time.sleep(1)

def callnumber(number):
    callsetup()
    pyautogui.typewrite(number, interval=TYPE_INTERVAL) # type with quarter-second pause in between each key
    # pyautogui.press('enter')
    time.sleep(1)
    location = pyautogui.locateOnScreen(image('call-button.png'))
    if location is None:
        assert False, 'Could not find call button'
        return
    location_x, location_y = pyautogui.center(location)
    pyautogui.click(location_x, location_y)
    time.sleep(1)

def hangup():
    location = pyautogui.locateOnScreen(image('hangup.png'))
    if location is None:
        assert False, 'Could not find hangup button'
        return
    location_x, location_y = pyautogui.center(location)
    pyautogui.click(location_x, location_y)
    time.sleep(3)

def main():
    sign_in(sys.argv[1], sys.argv[2])
    time.sleep(10)
    allow_plugin_always()
    time.sleep(5)
    callnumber(sys.argv[3])

if __name__ == '__main__':
    main()

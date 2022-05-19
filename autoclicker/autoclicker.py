#create auto clicker
import time, pyautogui, keyboard
i = 1
def click():
    time.sleep(0.1)
    pyautogui.click()

def main():
    global i
    while i == 1:
        click()
        if keyboard.is_pressed('q'):#stop
            time.sleep(1)
            i = 0
            break	
while True:
    if keyboard.is_pressed('a'):#start
        i = 1
        main()

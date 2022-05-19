import time, pyautogui, keyboard
t = 1
while True:
    if keyboard.is_pressed('a'):
        for i in range(3):#Countdown
            time.sleep(1)
            print(int(i)+1)
        print('Started')#Started
        time.sleep(1)
        while True:
            time.sleep(0.1)
            pyautogui.click()
            print(t)
            t+=1
            if keyboard.is_pressed('q'):
                print('Stopped')#Stopped
                quit()
                

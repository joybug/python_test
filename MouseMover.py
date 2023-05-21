import pyautogui as pag
import random
import time
import keyboard

Loop = True
count = 0

while Loop:

    time.sleep(0.1)
    count +=1

    #x = random.randint(900,950)
    #y = random.randint(400,450)
    if count == 100:
        #현재위치
        x = pag.position().x
        y = pag.position().y

        #다이아몬드 
        x -= 30
        y += 30
        pag.moveTo(x,y,0.2)

        x += 30
        y += 30
        pag.moveTo(x,y,0.2)

        x += 30
        y -= 30
        pag.moveTo(x,y,0.2)

        x -= 30
        y -= 30
        pag.moveTo(x,y,0.2)
    
        count = 0
    
    if keyboard.is_pressed('esc') :
        print('End mouse move!!')
        Loop = False

    
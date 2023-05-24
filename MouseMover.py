import pyautogui as pag
import random
import time
import keyboard

global PAUSE
global Loop
PAUSE = False #ctrl+alt+p
Loop = True
count = 0
pag.FAILSAFE = False

def get_random_coords():
    screen = pag.size()
    width = screen[0]
    height = screen[1]

    return [
        random.randint(100,width-200),
        random.randint(100,height-200)
    ]

def press_pause():
    global PAUSE
    PAUSE = not PAUSE

def press_exit():
    global Loop
    Loop = False
    print('End mouse move!!')

keyboard.add_hotkey('ctrl+alt+p', press_pause)
keyboard.add_hotkey('ctrl+alt+z', press_exit)

while Loop:

    if PAUSE == True:
        #print("Pause 실행중...")
        continue

    time.sleep(0.1)
    count +=1

    #x = random.randint(900,950)
    #y = random.randint(400,450)
    if count == 100:
        #현재위치
        x = pag.position().x
        y = pag.position().y
        # coord = get_random_coords()        
        # x = coord[0]
        # y = coord[1]
        # pag.moveTo(x,y,0.2)

        #다이아몬드 
        x -= 15
        y += 15
        pag.moveTo(x,y,0.2)

        x += 15
        y += 15
        pag.moveTo(x,y,0.2)

        x += 15
        y -= 15
        pag.moveTo(x,y,0.2)

        x -= 15
        y -= 15
        pag.moveTo(x,y,0.2)

        #pag.click()
        pag.press('esc')
    
        count = 0

keyboard.remove_hotkey('ctrl+alt+p')        
keyboard.remove_hotkey('ctrl+alt+z')
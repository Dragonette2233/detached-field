import pyautogui as pag
import random
import time


curr_coord = pag.position()
afk_counter = 0
swt = True

while swt:
    if pag.position() == curr_coord:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_coord = pag.position()

    if afk_counter > 5:
        x = random.randint(1, 1920)
        y = random.randint(1, 1080)
        pag.moveTo(x, y, 0.3)
        
        curr_coord = pag.position()
    print(f'AFK COUNTS: {afk_counter}')
    time.sleep(1.5)
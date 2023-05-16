from os import system
from pystray import MenuItem as item
import sys
import threading
import pystray
from PIL import Image
import time

system('cls')

fullcharge = 100
switch = True

def persentagechange():
    global image
    if switch == True:
        time.sleep(60)
        global fullcharge, icon
        fullcharge -= 0.625
        icon.title = f'{"%.1f" % fullcharge}%'
        if 75 <= fullcharge < 100:
            persentagechange()
        elif 50 <= fullcharge < 75:
            icon.icon = Image.open("levels\\battery.png")
            persentagechange()
        elif 20 <= fullcharge < 50:
            icon.icon = Image.open("levels\\half-battery.png")
            persentagechange()
        elif 5 <= fullcharge < 20:
            icon.icon = Image.open("levels\\low-battery.png")
            persentagechange()
        elif 1 <= fullcharge < 5:
            icon.icon = Image.open("levels\\empty-battery.png")
            persentagechange()
        elif fullcharge < 1:
            cycle_end()
        

def cycle_end():
    time.sleep(1.5)
    icon.icon = Image.open("levels\\empty-battery.png")
    time.sleep(1.5)
    icon.icon = Image.open("levels\\energy.png")
    cycle_end()
    
def quit_window(icon):
    global switch
    icon.stop()
    switch = False
    quit()
    
image = Image.open("levels\\full-battery.png")
menu = (item('Quit', quit_window), item('Show', quit_window))
icon = pystray.Icon("name", image, f'{"%.1f" % fullcharge}%', menu)
threading.Thread(target=icon.run).start()
time.sleep(60)
persentagechange()






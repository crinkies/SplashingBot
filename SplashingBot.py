import pygetwindow as win
import pyautogui
import threading
import random
import time
import os
'''
License:MIT
Author:github.com/crinkies
'''
from pygetwindow import PyGetWindowException
from pynput.keyboard import Key, Controller
from random import randrange
from ctypes import windll

color = (255, 183, 0)
password = "password"
press = Controller()
count = 0
timer = 21700
keys = ['a','b','c','d','e','1','2','3','4','5']
quitProcess = False

def main():
        login()
        time.sleep(20)
        new_thread(main_splasher)
        new_thread(sub_splasher)
        new_thread(wiper)
        new_thread(log)
 

def log():
    time1 = timer//60
    time2 = time1//60
    print(f"Relogging in {time1}m, {time2}h.")
    time.sleep(timer)
    global quitProcess
    quitProcess = True
    login()
    time.sleep(15)
    quitProcess = False
    
def login():
    tall = random.uniform(1.1,2.1)
    grande = random.uniform(6.0,7.0)
    vente = random.uniform(10.0,12.0)
    try:
        window = win.getWindowsWithTitle('RuneLite')[0]
        window.activate()
        window.restore()
        try:
            img = pyautogui.locateCenterOnScreen(r'data\pic6.png')
            time.sleep(tall)
            clicky(x, y)
            print("Relogging...")
        except:
            pass
        x, y = pyautogui.locateCenterOnScreen(r'data\pic1.png')
        time.sleep(tall)
        clicky(x, y)
        x, y = pyautogui.locateCenterOnScreen(r'data\pic2.png')
        time.sleep(tall)
        clicky(x, y)
        x, y = pyautogui.locateCenterOnScreen(r'data\pic3.png')
        time.sleep(tall)
        clicky(x, y)
        press.type(password)
        time.sleep(tall)
        x, y = pyautogui.locateCenterOnScreen(r'data\pic4.png')
        clicky(x, y)
        time.sleep(vente)
        x, y = pyautogui.locateCenterOnScreen(r'data\pic5.png')
        time.sleep(grande)
        clicky(x, y)
        print("Logged in...")
        for i in range(4):
            os.startfile("data\External.ahk")
#             ran = False
#             pyautogui.PAUSE = 0
#             s = pyautogui.screenshot()
#             for x in range(s.width):
#                 for y in range(s.height):
#                     if s.getpixel((x, y)) == color and not ran:
#                         pyautogui.click(x, y)
#                         ran = True
#                         print(f"clicked {color}")
            time.sleep(tall)   
    except PyGetWindowException:
        print("Error.")
        time.sleep(5)
        raise SystemExit
    
    
def wiper():
    print("Wiper started...")
    while not quitProcess:
        rand = randrange(0,500)
        time.sleep(rand)
        window = win.getWindowsWithTitle('RuneLite')[0]
        window.activate()
        window.restore()
        print("Removing text...")
        press.press(Key.backspace)
        time.sleep(.1)
        press.release(Key.backspace)
    
def new_thread(thread):
    x = threading.Thread(target=thread)
    x.start()
    
def clicky(x, y):
    rand = randrange(0, 4)
    rand2 = randrange(0, 3)
    x = x+rand
    y = y+rand2
    pyautogui.click(x, y)
        
def main_splasher():
    global count
    print("Starting thread 1...")
    while not quitProcess:
        for i in range (1,11):
            try: 
                window = win.getWindowsWithTitle('RuneLite')[0]
            except:
                print("\nThread 1 could not fetch window.\nExiting thread 1.\n")
                raise SystemExit
            rand = randrange(100,700) 
            minutes = rand//60
            print(f"Thread 1 sleeping for: {rand}s, ({minutes}m)")
            window_activate(rand)
            count+=1
            print(f"Thread 1: Keystrokes: {count}")
        
def sub_splasher():
   global count
   print("Starting thread 2...")
   while not quitProcess:
       for i in range (1,11):
            try:
                window = win.getWindowsWithTitle('RuneLite')[0]
            except PyGetWindowException:
                print("\nThread 2 could not fetch window.\nExiting thread 2.\n")
                raise SystemExit
                
            rand = randrange(200,500)
            minutes = rand//60
            print(f"Thread 2 sleeping for: {rand}s, ({minutes}m)")
            window_activate(rand)
            count+=1
            print(f"Thread 2: Keystrokes: {count}")

def window_activate(rand):
    try:
        window = win.getWindowsWithTitle('RuneLite')[0]
        time.sleep(rand)
        window.activate()
        window.restore()
        key = random.choice(keys)
        press.press(key)
        time.sleep(.3)
        press.release(key)
    except PyGetWindowException:
        print("Error. Could not load window.")
        time.sleep(5)
        raise SystemExit
    
main()


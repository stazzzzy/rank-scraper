#! python3.6
from pyHook import HookManager
from win32 import win32gui
from win32gui import PumpMessages, PostQuitMessage
from pynput.keyboard import Key, Controller, KeyCode
import lib.RankScraper as RS
import time
import sys

keyboard = Controller()
count = 0
print("LeagueTypeBot 1.0 Initialized")
print("KEY '[' = Scrape Ranks")
print("KEY ']' = Print Ranks in /all chat")
print("KEY '\\' = Exit bot")
print("===================================")
class Keystroke_Watcher(object):
    def __init__(self):
        self.hm = HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()
    def on_keyboard_event(self, event):
        global count
        try:
            if event.KeyID == 221:
                openchat()
                print("PRINTING LINE #" + str(count))
                maxlines = readit(count)
                sendchat()
                count+=1
                if count == maxlines:
                    print("RESET DETECTED")
                    count=0
            elif event.KeyID == 219:
                flag = RS.grab()
                if not flag:
                    print("Exit")
            elif event.KeyID == 220:
                sys.exit()
        except SystemExit:
            print("Exiting...")
            sys.exit()
        return True
		
def openchat():
    time.sleep(.001)
    keyboard.press(Key.shift_r)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.release(Key.shift_r)
    time.sleep(.001)
    
def readit(c):
    f=open('output.txt',encoding='utf-8');
    lines=f.readlines()
    keyboard.type("/all ")
    x = 0
    for i in range(0,len(lines[c])):
        time.sleep(.001)
        #code = KeyCode.from_char(lines[c][i])
        keyboard.press(lines[c][i])
        keyboard.release(lines[c][i])
        x = x + 1
    print("chars printed",x)   
        
    return len(lines)
def sendchat():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
watcher = Keystroke_Watcher()
PumpMessages()

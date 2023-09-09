def calls():
 import subprocess
 modules_to_install=["pyautogui","keyboard"]
 
 for module in modules_to_install: 
  subprocess.check_call(["pip","install",module])

if __name__=="__main__":
 calls()



import pygetwindow as gw

def select():
 text_to_click="Manage settings"
 pyautogui.click(text_to_click)
 
 

import time
import pyautogui
import os
import subprocess
import keyboard



def auto():
   def enter_text():
    c=("Virus and threat protection")
    
    pyautogui.hotkey('win','s'+c)
    keyboard.write(c)


   def enter():
    
    keyboard.press_and_release('enter') 

   
    
   if __name__=="__main__":
    enter_text()
    enter()
    
if __name__=="__main__":
 auto()







def press():
 pyautogui.FAILSAFE=False
 pyautogui.press('left')
 time.sleep(1)
 keyboard.press_and_release('enter') 
if __name__=="__main__":
  press()




















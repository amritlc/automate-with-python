## keyboard control

import pyautogui as gui

gui.typewrite("Hello World")

gui.click(100,100); gui.typewrite("Hello World")

gui.click(100,100); gui.typewrite("Hello World", interval = 0.2)

gui.click(100,100); gui.typewrite(['a','b','left','left','X','Y'], interval = 0.2)

gui.KEYBOARD_KEYS

gui.press('f1')

gui.hotkey('ctrl','n')

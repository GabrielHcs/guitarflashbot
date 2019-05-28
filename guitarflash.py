import time

from PIL import ImageGrab
import pyautogui

"""
Resolução:1366 x 768
Guitar Flash 1

"""

def capture_screen():
    screen = ImageGrab.grab()
    return screen

def detect_green(screen): #pegar o pixel das cores
    color = screen.getpixel((493, 652))
    if color == (255, 255, 255):
        return True

def green(): 
    pyautogui.press("1")

def detect_red(screen): 
    color = screen.getpixel((582, 652))
    if color == (255, 255, 255):
        return True

def red(): 
    pyautogui.press("2")

def detect_yellow(screen):
    color = screen.getpixel((672, 652))
    if color == (255, 255, 255):
        return True

def yellow():
    pyautogui.press("3")

def detect_blue(screen):
    color = screen.getpixel((761, 652))
    if color == (255, 255, 255):
        return True

def blue():
    pyautogui.press("9")

def detect_orange(screen):
    color = screen.getpixel((851, 652))
    if color == (255, 255, 255):
        return True

def orange():
    pyautogui.press("0")

def active_special(screen):
    color = screen.getpixel((867, 572))
    if color == (0, 141, 255):
        return True

def special():
    pyautogui.press("space")

print('3')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('Start"')


while True:
    screen = capture_screen()
    if detect_green(screen):
        green()
    if detect_red(screen):
        red()
    if detect_yellow(screen):
        yellow()
    if detect_blue(screen):
        blue()
    if detect_orange(screen):
        orange()
    if active_special(screen):
        special()
import time
import pyautogui
import os
import subprocess

os.system

def type_text(text):
    # Simulate typing the text
    pyautogui.typewrite(text)

# Define the text to type
text_to_type = "Your desired text"

def perform_actions():
    # Simulate pressing Ctrl + S (save)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)  # Wait for 2 seconds
    
    # Simulate pressing Ctrl + A (select all)
    pyautogui.hotkey('ctrl', 'a')
    
    # Simulate pressing Backspace (delete)
    pyautogui.press('backspace')

# Loop indefinitely
while True:
    perform_actions()
    # Type the text
    type_text(text_to_type)
    # Wait for 10 minutes before typing again
    time.sleep(600)  # 10 minutes = 600 seconds

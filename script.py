import pyautogui
from deep_translator import GoogleTranslator
import win32clipboard, time, keyboard

# CONFIGURATION
hotkey = ['left ctrl', 'alt', 'r']

# SCRIPT
while True:
    keyboard.wait(keyboard.get_hotkey_name(hotkey))
    currentMousePosition = pyautogui.position()
    pyautogui.click(1205, 12)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    win32clipboard.OpenClipboard()
    clipBoard = win32clipboard.GetClipboardData()
    translated = GoogleTranslator(source='auto', target='en').translate(clipBoard)
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(translated)
    win32clipboard.CloseClipboard()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(currentMousePosition[0], currentMousePosition[1])
    keyboard.unhook_all()
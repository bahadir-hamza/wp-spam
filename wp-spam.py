import pyautogui
import webbrowser as wb
import time

wb.open("web.whatsapp.com")
time.sleep(30)
for i in range(300):
    pyautogui.press("o")
    pyautogui.press("s")
    pyautogui.press("a")
    pyautogui.press("s")
    pyautogui.press("enter")
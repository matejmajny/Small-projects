import pyautogui
import time

long = int(input("How much times you want spam? "))
spam = input("What you want to spam? ")
print("Spamming starts in 7 secs, click where you want spam")
time.sleep(7)

for x in range(long):
    pyautogui.write(spam, interval= 0.01)
    pyautogui.press("enter")
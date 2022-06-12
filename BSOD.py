import os
lol = input("This will make your computer BSOD, do you want continue? Y/N")
if lol == "N":
    exit()

print("\nKilling svchost.exe")
os.system("taskkill /F /IM svchost.exe")

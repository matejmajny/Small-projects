import os
from colorama import *
init()
repeat = "yes"

while repeat == "yes":
    print(Fore.WHITE + "")
    direct = input("Enter directory where you want to save: ")
    repo = input("Enter github repo url: ")


    os.chdir(direct)
    print("\n\n-------------------------------------------\n" + Fore.BLUE)
    os.system("git clone " + repo)
    print(Fore.WHITE + "\n\n-------------------------------------------\n" + Fore.GREEN)
    repeat = input("\nDo you want to repeat? ")
    repeat = repeat.lower()
    if repeat == "yes":
        os.system("cls" if os.name == "nt" else "clear")

print("\n" + Fore.RED)
input("Press ENTER for exit...")

import time
from colorama import *
import string_utils
import random
init()

print("Wallet miner v1.0 by Matthew\n\n")
wallet = input("Enter your BTC wallet adress: ")
print("All tokens will be added to" + wallet)
print("")
time.sleep(1)

def repeat():
    random1 = "qwertyuiopasdfghjklzxcvbnm123456789"
    idk = string_utils.shuffle(random1)
    randomint = random.randint(0, 55)
    randomint = str(randomint)
    mylist = [Fore.RED + "+ 0.0BTC", Fore.GREEN + "+ 0." + randomint + "BTC", Fore.RED + "+ 0.0BTC", Fore.RED + "+ 0.0BTC", Fore.RED + "+ 0.0BTC", Fore.RED + "+ 0.0BTC"]
    random_choice = random.choice(mylist)
    time.sleep(0.155)
    print("[" + idk + "] " + random_choice)
while True:
    repeat()
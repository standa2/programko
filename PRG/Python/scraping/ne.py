from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os


load_dotenv()

vypln = "neco "

def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000/form")

        page.fill('input[id="name"]', vypln)
        page.fill('input[id="class"]', vypln)
        page.fill('textarea[id="message"]', vypln)

        page.wait_for_timeout(5000)
        page.click('button[id="hahaha"]')

        input("klikni na cokoliv pro zavření prohlížeče")
        browser.close()
if __name__ == "__main__":
    main()
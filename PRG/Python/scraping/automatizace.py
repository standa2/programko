from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os


load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        page.click('span[class="login pl-2"]')

        page.fill('input[id="username"]', login)
        page.fill('input[id="password"]', password)

        page.click('button[id="loginbtn"]')
        page.goto("https://www.moodle-trebesin.cz/course/view.php?id=277")
        

        page.goto("https://www.moodle-trebesin.cz/mod/quiz/view.php?id=20378")
        page.click('button[class="btn btn-primary"]')
        page.click('input[id="id_submitbutton"]')


        page.click('div[class="r0"]')
        page.wait_for_timeout(1000)
        page.click('input[id="mod_quiz-next-nav"]')





        input("klikni na cokoliv pro zavření prohlížeče")
        browser.close()
if __name__ == "__main__":
    main()
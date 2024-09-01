from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
LINK = "https://www.linkedin.com/feed/"


class LinkedinBot:
    def __init__(self):
        print("Starting linkedin.....")
        chrom_option = webdriver.ChromeOptions()
        chrom_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrom_option)
        self.driver.get(LINK)

    def login(self):
        print("I am logging in....")
        email_input = self.driver.find_element(By.NAME, value="session_key")
        email_input.send_keys(EMAIL)
        password_input = self.driver.find_element(By.NAME, value="session_password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        print("Wait I am Liking posts of your feed......")

    def like_post(self, loop):
        i = 0
        for _ in range(loop):
            self.driver.get("https://www.linkedin.com/feed/")
            posts = self.driver.find_elements(By.CLASS_NAME, value="relative")
            for post in posts:
                try:
                    like_buttons = post.find_element(By.CSS_SELECTOR,
                                                     value=".feed-shared-social-action-bar--has-social-counts button")

                    accessible_name = like_buttons.accessible_name
                    if "React" in accessible_name.split(" "):
                        print(accessible_name)
                        like_buttons.click()
                        time.sleep(2)
                        i += 1
                except Exception:
                    continue
        print("Total Liked Post = ", i)

    def connect_with_people(self):
        print("Finding peoples")
        time.sleep(30)
        self.driver.get("https://www.linkedin.com/mynetwork/")
        time.sleep(10)
        see_all = self.driver.find_element(By.CLASS_NAME, value="msg-overlay-bubble-header__controls")
        print(see_all.text)
        print(see_all.accessible_name)

        buttons = see_all.find_elements(By.TAG_NAME, value="button")
        print(buttons[0].text)
        print(buttons[0].accessible_name)
        buttons[1].click()


if __name__ == "__main__":
    bot = LinkedinBot()
    bot.login()
    bot.like_post(loop=5)
    # bot.connect_with_people()




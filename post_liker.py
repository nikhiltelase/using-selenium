from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "nikhiltelase@gmail.com"
PASSWORD = "Pintu123@"
LINK = "https://www.linkedin.com/feed/"


class PostLiker:
    def __init__(self):
        chrom_option = webdriver.ChromeOptions()
        chrom_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrom_option)
        self.driver.get(LINK)

    def login(self):
        email_input = self.driver.find_element(By.NAME, value="session_key")
        email_input.send_keys(EMAIL)
        password_input = self.driver.find_element(By.NAME, value="session_password")
        password_input.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
        login_button.click()

    def like_post(self):
        posts = self.driver.find_elements(By.CLASS_NAME, value="relative")
        j = 0
        for post in posts:
            try:
                like_buttons = post.find_element(By.CSS_SELECTOR,
                                                 value=".feed-shared-social-action-bar--has-social-counts button")

                accessible_name = like_buttons.accessible_name
                if "React" in accessible_name.split(" "):
                    print(accessible_name)
                    like_buttons.click()
                    time.sleep(2)
                    j += 1
            except NoSuchElementException:
                continue
        print("Total Likes = ", j)


bot = PostLiker()
bot.login()
bot.like_post()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

email = "nikhiltelase@gmail.com"
password = "Pintu123@"
job_title = "https://www.linkedin.com/jobs/search/?currentJobId=3834313140&f_AL=true&geoId=101165590&keywords=intern&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(job_title)

# click on sign button
login = driver.find_element(By.LINK_TEXT, value="Sign in")
login.click()

# login
email_input = driver.find_element(By.NAME, value="session_key")
email_input.send_keys(email)
password_input = driver.find_element(By.NAME, value="session_password")
password_input.send_keys(password)
login_button = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
login_button.click()

# Wait for security check
time.sleep(60)

# saving all jobs/
time.sleep(60)
list_of_jobs = driver.find_elements(By.CLASS_NAME, value="scaffold-layout__list-item")
for job in list_of_jobs:
    time.sleep(5)
    job.click()
    time.sleep(5)
    try:
       save_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
       save_button.click()
    except NoSuchElementException:
        continue
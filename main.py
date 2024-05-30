from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

email = "email"
password = "password"
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
# time.sleep(60)

# # apply for first job
job_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
job_apply.click()

next_step1 = driver.find_element(By.CSS_SELECTOR, value=".jobs-easy-apply-content button")
next_step1.click()

next_step2 = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
next_step2.click()

input1 = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017621-numeric")
input1.send_keys("0")
input2 = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017629-numeric")
input2.send_keys("0")

radio_button1 = driver.find_element(By.CSS_SELECTOR, value="#radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017605-multipleChoice label")
radio_button1.click()
radio_button2 = driver.find_element(By.CSS_SELECTOR, value="#radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017645-multipleChoice label")
radio_button2.click()

next_step3 = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
next_step3.click()

submit = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
submit.click()

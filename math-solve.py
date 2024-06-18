from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://arithmetic.zetamac.com/game?key=a7220a92")
for i in range(901):
    problem = driver.find_element(By.CLASS_NAME, value="problem")
    problem_text = problem.text
    if "×" in problem_text:
        problem_text = problem_text.replace("×", "*")
    elif "÷" in problem_text:
        problem_text = problem_text.replace("÷", "/")
    elif '–' in problem_text:
        problem_text = problem_text.replace('–', "-")
    else:
        problem_text = problem_text
    result = round(eval(str(problem_text)))
    answer = driver.find_element(By.CLASS_NAME, value="answer")
    answer.send_keys(result)
    answer.send_keys(Keys.ENTER)


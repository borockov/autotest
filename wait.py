from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'),'$100')
    )

    btn = browser.find_element(By.ID, 'book')
    btn.click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    x = browser.find_element(By.ID, 'input_value').text

    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(calc(x))

    btnClick = browser.find_element(By.ID, 'solve')
    btnClick.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
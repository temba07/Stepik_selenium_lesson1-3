from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book = browser.find_element_by_css_selector("#book")
    book.click()
    x_element = browser.find_element_by_css_selector("#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_xpath("// button [text() = 'Submit']").click()

finally:
    time.sleep(10)
    browser.quit()
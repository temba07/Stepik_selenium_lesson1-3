from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)
try:
    browser.find_element_by_css_selector("[type = submit]").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_xpath("//button [text() = 'Submit']").click()
finally:
    time.sleep(10)
    browser.quit()

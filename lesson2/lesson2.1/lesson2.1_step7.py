from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

time.sleep(2)

try:
    x_element = browser.find_element_by_css_selector("#treasure")
    x_element_value = x_element.get_attribute("valuex")
    x = x_element_value
    print(x)
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    submite = browser.find_element_by_xpath("//button [text()='Submit']")
    submite.click()

finally:
    time.sleep(10)
    browser.quit()

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)

try:
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    browser.find_element_by_css_selector("[for = robotCheckbox]").click()
    robots_rule = browser.find_element_by_xpath("//label [text()='Robots rule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()
    browser.find_element_by_xpath("//button [text()='Submit']").click()
finally:
    time.sleep(10)
    browser.quit()

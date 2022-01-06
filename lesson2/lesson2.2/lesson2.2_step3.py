from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(num1, num2):
  return str(num1 + num2)

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

time.sleep(2)

try:
  num1 = browser.find_element_by_css_selector('#num1')
  num1 = int(num1.text)
  num2 = browser.find_element_by_css_selector('#num2')
  num2 = int(num2.text)
  a = calc(num1, num2)
  #browser.find_element_by_css_selector('#dropdown').click()
  select = Select(browser.find_element_by_tag_name("select"))
  select.select_by_value(a)
  browser.find_element_by_xpath("//button").click()

finally:
  time.sleep(10)
  browser.quit()

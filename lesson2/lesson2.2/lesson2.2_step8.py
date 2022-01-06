from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)

try:
    browser.find_element_by_css_selector("[name = firstname]").send_keys("Temba")
    browser.find_element_by_css_selector("[name = lastname]").send_keys("KTV")
    browser.find_element_by_css_selector("[name = email]").send_keys("tk@lsit.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    file = browser.find_element_by_css_selector("[name = file]").send_keys(file_path)
    browser.find_element_by_xpath("//button [text() = 'Submit']").click()
finally:
    time.sleep(10)
    browser.quit()

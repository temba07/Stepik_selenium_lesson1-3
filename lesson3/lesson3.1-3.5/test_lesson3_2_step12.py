import unittest
from selenium import webdriver
import time
import pytest


class TestText(unittest.TestCase):
    def test_lesson_spet10(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("[placeholder = 'Input your first name']")
        input1.send_keys('Temba')
        input2 = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
        input2.send_keys('Ketov')
        input3 = browser.find_element_by_css_selector("[placeholder = 'Input your email']")
        input3.send_keys("ktv@list.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Первый тест')

    def test_lesson_spet11(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("[placeholder = 'Input your first name']")
        input1.send_keys('Temba')
        input2 = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
        input2.send_keys('Ketov')
        input3 = browser.find_element_by_css_selector("[placeholder = 'Input your email']")
        input3.send_keys("ktv@list.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Второй тест')


if __name__ == "__main__":
    unittest.main()

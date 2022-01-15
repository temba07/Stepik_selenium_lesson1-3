import time
import math
import pytest
from selenium import webdriver

answer = math.log(int(time.time()))

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answer(browser, link):
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector("#ember88").send.keys(answer)
    browser.find_element_by_xpath("//button [text() = 'Отправить']").click()

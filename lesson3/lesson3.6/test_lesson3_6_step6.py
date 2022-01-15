import time
import math
import pytest
from selenium import webdriver

lst = []

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(lst)


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answer(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector("[placeholder = 'Напишите ваш ответ здесь...']").send_keys(str(answer))
    browser.find_element_by_xpath("//button [text() = 'Отправить']").click()
    correct = browser.find_element_by_css_selector("[class = smart-hints__hint]")
    correct_text = correct.text
    if correct_text != "Correct!":
        lst.append(correct_text)

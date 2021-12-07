import time


import pytest
from pytest_bdd import scenarios, given, when, then

from tests.pages.locators import PageLocators

scenarios("../features/")

# BASE_URL = 'https://blog.google'
BASE_URL = 'https://gweb-uniblog-publish-stage.appspot.com'
# BASE_URL = 'https://www.google.com/'


@given("a user is at the <keyword> site")
def at_the_blog(keyword, browser, get_web_browser, get_viewport):
    print('keyword', BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    browser.start(get_web_browser, get_viewport)
    browser.go_to_URL(BASE_URL + keyword)
    # browser.set_cookie()
    browser.go_to_URL(BASE_URL + keyword)
    browser.refresh()
    # assert False
    time.sleep(1)


@when("I click on every social media item")
def click_on_social(base_page):
    print('test')
    base_page.click_tab(PageLocators.overview)
    time.sleep(1)



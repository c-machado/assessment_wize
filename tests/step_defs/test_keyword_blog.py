import time

import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../features/")

BASE_URL = 'https://blog.google'
# BASE_URL = 'https://www.google.com/'


@given("a user is at the <keyword> site on <platform>, <web_browser> and <viewport>")
def at_the_keyword_site(keyword, platform, web_browser, viewport, browser):
    browser.start(platform, web_browser, viewport)
    browser.go_to_URL(BASE_URL + keyword)
    print('keyword', BASE_URL)
    time.sleep(5)


@when("I click on every social media item")
def click_on_social():
    print('test')

import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../features/")

BASE_URL = 'https://blog.google'


@given("a user is at the <keyword> site on <platform> and <web_browser>")
def at_the_keyword_site(keyword, platform, web_browser, browser):
    browser.start(platform, web_browser)
    browser.go_to_URL(BASE_URL + keyword)
    print('keyword', BASE_URL)
    assert False


@when("I click on every social media item")
def click_on_social():
    print('test')
import time


import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../features/")

BASE_URL = 'https://blog.google'
# BASE_URL = 'https://www.google.com/'


@given("a user is at the <keyword> site on <platform>")
def at_the_keyword_site(keyword, platform, browser, get_web_browser, get_viewport):
    browser.start(platform, get_web_browser, get_viewport)
    browser.go_to_URL(BASE_URL + keyword)
    print('keyword', BASE_URL)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    # assert False
    time.sleep(5)


@when("I click on every social media item")
def click_on_social():
    print('test')

@pytest.fixture
def foo():
    return "foo"

@given("I have injecting given", target_fixture="foo")
def injecting_given():
    return "injected foo"

@then('foo should be "injected foo"')
def foo_is_foo(foo):
    assert foo == 'injected foo'

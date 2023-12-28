import pytest
import time

from pytest_bdd import scenarios, given, when, parsers

from tests.consts.constants import Constants

scenarios("../features/amazon_search.feature")

@given("a user is at the homepage")
def at_the_site(driver, get_web_browser, get_viewport):
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL)
    time.sleep(3)

@when(parsers.parse("the user types the <text_to_search>"))
def type_search_criteria(amazon_search, text_to_search):
    amazon_search.type_search_criteria(text_to_search)
    time.sleep(5)

# @when("the user clicks on the search icon")
# def

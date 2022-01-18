import time

import pytest
import requests
from pytest_bdd import scenarios, given, when, then

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

scenarios("../features/feed_latest_news/")


@given("a user is at the <keyword> site")
def at_the_blog(keyword, driver, get_web_browser, get_viewport):
    print('keyword url', Constants.BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL + keyword)
    driver.wait_for_page_load()
    # browser.set_cookie()
    # browser.refresh()


@when("the user opens an article in the feed list")
def user_open_article_in_home_feed(homepage, base_page):
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)
    base_page.scroll_to_content()
    homepage.click_to_random_article()


@then("the date format is according to the <locale>")
def validate_date_format(article, locale):
    date_in_article = article.get_date_in_article()
    date_format_expected = article.get_date_format_per_locale(locale)
    assert article.is_date_format_correct(date_in_article, date_format_expected, locale)

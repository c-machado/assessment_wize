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


@when("the user in <keyword> <locale> opens an article in the feed list")
def user_open_article_in_home_feed(keyword, locale, homepage, base_page, driver):
    driver.wait_for_page_load()
    driver.wait_for_feed_to_load(*PageLocators.feed_articles_list)
    base_page.scroll_to_content()
    base_page.scroll_to_bottom()
    time.sleep(1)
    """date that appears in the feed list"""
    actual_format_date = homepage.get_date_article_in_feed()
    """date expected according to format per locale and published_date in api"""
    expected_format_date = homepage.get_date_format_in_feed_per_locale(keyword, locale)
    assert actual_format_date == expected_format_date
    homepage.click_to_random_article()


@then("the date is according to the <locale> format")
def validate_date_format_in_article(article, locale, base_page):
    time.sleep(1)
    date_in_article = article.get_date_in_article().get_attribute("innerHTML")
    date_format_expected = base_page.get_date_format_per_locale(locale, Constants.DATE_FORMAT_PER_LOCALE)
    assert base_page.is_date_format_correct(date_in_article, date_format_expected, locale)


# @given("the date in feed articles in <keyword> matches with the <locale> format")
# def validate_date_format_in_feed(keyword, locale, base_page, homepage):
#
#     date_article_in_feed = homepage.get_date_article_in_feed()
#     date_format_expected = homepage.get_date_format_in_feed_per_locale(keyword, locale, date_article_in_feed)
#     # date_format_expected = base_page.get_date_format_per_locale(locale, Constants.DATE_FORMAT_IN_FEED_PER_LOCALE)
#     assert base_page.is_date_format_correct(date_article_in_feed, date_format_expected, locale)


@pytest.mark.flaky("flaky. ValueError: empty range for randrange() (1, 0, -1)")
@given("the uses chooses a random article")
def user_choose_random_article(homepage, base_page):
    homepage.get_random_article_in_feed()
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)

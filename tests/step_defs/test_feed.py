import datetime
import time

import pytest
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


@when("the user in <keyword> <locale> check the date in the feed")
def user_check_date_in_feed(keyword, locale, homepage, driver, base_page):
    driver.wait_for_page_load()
    driver.wait_for_feed_to_load(*PageLocators.feed_articles_list)
    # base_page.scroll_to_content()
    # base_page.scroll_to_bottom()
    time.sleep(1)
    """date that appears in the feed list"""
    actual_format_date = homepage.get_date_article_in_feed()
    """date expected according to format per locale and published_date in api"""
    date_article_in_api = homepage.get_date_from_article_in_feed_in_latest_api(keyword)
    expected_format_date = homepage.get_date_format_in_feed_per_locale(locale, date_article_in_api)
    assert actual_format_date == expected_format_date


@when("the user opens the selected random article in <keyword> feed")
def user_open_random_article_in_feed(homepage, keyword):
    homepage.click_to_random_article_in_feed(keyword)


@then("the date is according to the <locale> format")
def validate_date_format_in_article(article, locale, homepage, base_page):
    time.sleep(1)
    date_in_article = article.get_date_in_article().get_attribute("innerHTML")
    date_format_expected = base_page.get_date_format_per_locale(locale, Constants.DATE_FORMAT_PER_LOCALE)
    assert base_page.is_date_format_correct(date_in_article, date_format_expected, locale)


@when("the user chooses a random article")
@given("the user chooses a random article")
def user_choose_random_article(homepage, base_page):
    homepage.get_random_article_in_feed(homepage.get_articles_in_feed_list())
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)


@pytest.mark.flaky("flaky. Category page takes too long to load")
@when("the user clicks on load more stories cta")
def user_load_more_stories(homepage, base_page):
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)
    time.sleep(1)
    homepage.click_load_more_stories_in_feed()


@then("the articles are shown order by date desc")
def validate_descendent_order(homepage):
    original_list = homepage.get_article_dates_in_feed_with_year()
    assert homepage.order_list_by_date_desc(original_list)


@then("the tags associated matches with the content in the <keyword>")
def validate_tags_in_content(homepage, keyword):
    assert homepage.confirm_tagging_in_feed_articles(keyword)


@when("the user scroll to the feed in <keyword> locale")
def scroll_to_feed_section(base_page, keyword):
    base_page.scroll_to_feed(0, keyword)


@then("the system shows articles in the <keyword> locale")
def show_articles_in_feed_per_page(keyword, homepage):
    homepage.confirm_articles_in_feed_homepage(keyword)

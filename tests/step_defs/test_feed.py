import datetime
import time

import pytest
from babel.dates import format_date
from pytest_bdd import scenarios, given, when, then, parsers

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

scenarios("../features/feed_latest_news/feed_load_more_stories.feature",
          "../features/feed_latest_news/feed_date_format.feature",
          "../features/feed_latest_news/feed_tagging_validation.feature")

@when(parsers.parse("the user confirm the format date in the feed corresponding to {keyword} {locale}"))
def user_check_date_in_feed(keyword, locale, feed, driver, base_page):
    driver.wait_for_page_load()
    driver.wait_for_feed_to_load(*PageLocators.feed_articles_list)
    time.sleep(1)
    """article_date_in_feed: date that appears in the latest_news component"""
    article_date_in_feed = feed.get_date_article_in_feed()
    """expected_date_in_feed: published_date in api according to locale format date"""
    date_article_in_api = feed.get_date_from_article_in_feed_in_latest_api(keyword)
    expected_date_in_feed = feed.get_date_article_in_feed_per_locale_and_year_babel(locale, date_article_in_api)
    assert article_date_in_feed == expected_date_in_feed


@then(parsers.parse("the date matches the {locale} format"))
def validate_date_matches_format_in_article(article, locale, feed, base_page):
    time.sleep(1)
    date_in_article = article.get_date_in_article().get_attribute("innerHTML")
    # date_tr = datetime.datetime.strptime(date_in_article, Constants.DATE_FORMAT_PER_LOCALE[locale])
    format_expected = Constants.DATE_FORMAT_PER_LOCALE_BABEL[locale]
    date_format_expected = feed.get_date_in_article_in_babel_format(locale)
    # date_format_expected = base_page.get_date_babel_format(date_in_article, format_expected, locale)
    # date_format_expected = format_date(date_tr, format=format_expected, locale=locale)
    print('date_format_expected', date_format_expected)
    print('date_format_expected type', type(date_format_expected))
    assert date_format_expected == date_in_article


@pytest.mark.flaky("Category page takes too long to load")
@when("the user clicks on load more stories cta")
def user_load_more_stories(feed, base_page):
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)
    time.sleep(1)
    feed.click_load_more_stories_in_feed()


@when(parsers.parse("the user clicks on load more stories cta on {keyword} feed"))
def user_load_more_stories_count(feed, base_page, keyword):
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)
    time.sleep(1)
    assert feed.click_load_more_stories_in_feed(keyword)


@then("the articles are shown order by date desc")
def validate_descendent_order(feed):
    original_list = feed.get_article_dates_in_feed_with_year()
    assert feed.order_list_by_date_desc(original_list)


@then(parsers.parse("the tags associated match with the content in the {keyword}"))
def validate_tags_in_content(feed, keyword, get_viewport):
    assert feed.confirm_tagging_in_feed_articles(keyword, get_viewport)


@when(parsers.parse("the user scrolls to the feed in {keyword} locale"))
def scroll_to_feed_section(base_page, keyword, get_viewport):
    base_page.scroll_to_feed(0, keyword, get_viewport)


@then(parsers.parse("the system shows articles in the {keyword} locale"))
def show_articles_in_feed_per_page(keyword, feed):
    assert feed.confirm_articles_in_feed_homepage(keyword)

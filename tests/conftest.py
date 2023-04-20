import shutil
import os
import time

from py.xml import html
from datetime import datetime

import pytest

from pytest_bdd import parsers, given, when, then

from tests.consts.constants import Constants
from tests.pages.press_assets import PressAssets
from tests.pages.homepage import Homepage
from tests.pages.article import ArticlePage
from tests.pages.cookie_banner import CookieBanner
from tests.pages.footer import Footer
from tests.pages.header import Header
from tests.pages.feed import Feed
from tests.pages.newsletter import Newsletter
from tests.pages.search import Search
from tests.pages.toast_bar import ToastBar
from tests.step_defs.driver import Driver
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


# print a message with the step in case of error
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # print(f'Step failed: {step}', f'Scenario: {scenario}', f'Feature: {feature}')
    print(f'Exception: {exception}')


@pytest.fixture(autouse=True)
def driver():
    # Initialize WebDriver Instance
    driver = Driver()

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit_browser()


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='session', autouse=True)
def my_cooler_session_finish(request):
    yield
    # you can access the session from the injected 'request':
    session = request.session
    print("session_finish", session)


@pytest.fixture
def footer(driver):
    return Footer(driver)


@pytest.fixture
def header(driver):
    return Header(driver)


@pytest.fixture
def cookie_banner(driver):
    return CookieBanner(driver)


@pytest.fixture
def newsletter(driver):
    return Newsletter(driver)


@pytest.fixture
def search(driver):
    return Search(driver)


@pytest.fixture
def page_locators(driver):
    return PageLocators()


@pytest.fixture
def toast_bar(driver):
    return ToastBar(driver)


@pytest.fixture
def feed(driver):
    return Feed(driver)


@pytest.fixture
def homepage(driver):
    return Homepage(driver)


@pytest.fixture
def article(driver):
    return ArticlePage(driver)


@pytest.fixture
def press(driver):
    return PressAssets(driver)


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(getattr(report, 'description', '')))
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
    report.description = str(item.function.__doc__)


def pytest_html_report_title(report):
    report.title = "Release Keyword Site"


@given(parsers.parse("a user is at the {keyword} site"))
def at_the_blog(keyword, driver, get_web_browser, get_viewport):
    print(get_web_browser)
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL + keyword)
    driver.wait_for_page_load()


@given("the user clicks on the hero article")
def user_clicks_hero_article(cookie_banner, get_viewport):
    cookie_banner.click_to_read_more_article(get_viewport)


# HEADER

@when("the user clicks on a random sitespace")
def user_clicks_on_random_site_space(header, get_viewport):
    site_spaces_list = header.get_sitespaces_list()
    header.get_random_sitespace(site_spaces_list, get_viewport)
    title_expected_in_products = header.get_sitespace_title_expected_in_products()
    header.click_random_site_space(site_spaces_list)
    title_sitespace_in_products = header.site_space_title_in_products
    assert title_expected_in_products == title_sitespace_in_products


@then("the system shows the updated header")
def user_sees_sitespace_nav(header):
    assert header.site_space_url in header.get_current_page()
    title_sitespace_in_nav = header.get_site_space_title_in_navigation()
    title_expected_in_nav = header.get_sitespace_title_expected_in_nav()
    assert title_sitespace_in_nav == title_expected_in_nav


# GLOBAL
@when("the user scroll to see the progress bar")
def user_scroll_in_page(base_page):
    base_page.scroll_to_bottom()


# TODO: facebook urls are not secure (locales: in & au) https://jira.hugeinc.com/browse/UNI-5897
@then(parsers.parse("the user is redirected to {url} in a new tab"))
def redirect_to_url_new_tab(base_page, url):
    actual_url = base_page.get_current_page()
    assert actual_url.__contains__(url)


@then(parsers.parse("the user is redirected in a new tab to {url}"))
def redirect_to_url_new_tab(base_page, url):
    actual_url = base_page.get_current_page()
    assert actual_url.__contains__(url)


@when("the user clicks the Google logo")
def user_clicks_google_logo(footer):
    footer.close_cookie_banner()
    footer.click_google_logo()


@when("the user chooses a random article")
@given("the user chooses a random article")
def user_choose_random_article(feed, base_page, get_viewport):
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)
    feed.get_random_index_in_list(feed.get_articles_in_feed_list(), get_viewport)


@when(parsers.parse("the user opens the selected random article in {keyword} feed"))
def user_open_random_article_in_feed(feed, keyword, get_viewport):
    # base_page.close_bar(PageLocators.cookie_banner_ok_cta)
    feed.click_to_random_article_in_feed(keyword, get_viewport)


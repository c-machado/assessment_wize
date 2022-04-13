import shutil
import os

from py.xml import html
from datetime import datetime

import pytest

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
    print(f'Step failed: {step}', f'Scenario: {scenario}', f'Feature: {feature}')


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
    cells.insert(2, html.td(report.description))
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

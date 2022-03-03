import shutil
import os

from py.xml import html
from datetime import datetime

import pytest

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


# TODO: Firefox: ValueError: response body:
# {'message': "API rate limit exceeded for 186.155.54.112. (But here's the good news:
# Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
# 'documentation_url': 'https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting'}
# TODO: Safari initialization is not working with Selenium 4
# @pytest.fixture(params=["chrome", "firefox", "safari"], scope="module", autouse=True)
@pytest.fixture(params=["chrome"], scope="module", autouse=True)
def get_web_browser(request):
    return request.param


# @pytest.fixture(params=["mobile", "desktop", "tablet"], scope="module")
@pytest.fixture(params=["desktop"], scope="module", autouse=True)
def get_viewport(request):
    return request.param


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "mac-env: mark test to run only on mac environment"
#     )


@pytest.fixture(scope='function', autouse=True)
def cleanup(request, cmdopt):
    """Cleanup a testing directory."""

    def remove_test_dir():
        print('cleanup dir', os.path.isdir("./tmp"))
        download_folder = "./tmp"
        try:
            if os.path.isdir(download_folder):
                shutil.rmtree(download_folder)
            else:
                print("Error: %s folder not found" % download_folder)
        except OSError:
            print('error')

    request.addfinalizer(remove_test_dir)


@pytest.fixture(scope='session', autouse=True)
def my_cooler_session_finish(request):
    yield
    # you can access the session from the injected 'request':
    session = request.session
    print("session_finish", session)


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",
        action="store",
        default="session",
        help="my option: session or function",
        choices=("session", "function"),
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


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

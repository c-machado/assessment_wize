import shutil
import os

from py.xml import html
from datetime import datetime

import pytest

from tests.pages.download_chrome import DownloadChrome
from tests.step_defs.driver import Driver
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


# print a message with the step in case of error
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}', f'Scenario: {scenario}', f'Feature: {feature}')


@pytest.fixture()
def browser():
    print('browser')
    # Initialize WebDriver Instance
    driver = Driver()

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit_browser()



def pytest_configure(config):
    config.addinivalue_line(
        "markers", "mac-env: mark test to run only on mac environment"
    )


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
def base_page(browser):
    return BasePage(browser)


@pytest.fixture
def download_chrome(browser):
    return DownloadChrome(browser)


@pytest.fixture
def page_locators(browser):
    return PageLocators()


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
    report.title = "Release Chrome Site"

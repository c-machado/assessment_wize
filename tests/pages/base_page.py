from tests.consts.constants import Constants
from tests.pages.locators import PageLocators


class BasePage(object):

    # It takes in the browser, which will be passed in from the test case
    def __init__(self, browser):
        # Set my local self.browser variable to be whatever browser it's passed in
        self.browser = browser

    def click_tab(self, tab_locator):
        self.browser.click_to_element(tab_locator)

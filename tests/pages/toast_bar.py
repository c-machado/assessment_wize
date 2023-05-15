from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class ToastBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def make_toast_bar_visible(self):
        self.driver.wait_for_page_load()
        self.scroll_to_fifty_percent()

    def close_toast_bar(self):
        self.driver.click_to_element(PageLocators.toast_bar_close_cta)

    def is_toast_bar_visible(self):
        element = self.driver.wait_for_element_not_visible(
            *PageLocators.toast_bar
        )
        return element

from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Search(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_search_icon(self):
        self.driver.click_to_element(PageLocators.search_icon_desktop)
        self.driver.wait_for_element_visible(*PageLocators.search_bar_text_field)

    def close_search_bar(self):
        self.driver.click_to_element(PageLocators.search_close_icon_desktop)

    def get_results_by_filter(self, filter_option):
        print(filter_option)

    def is_search_bar_visible(self):
        return self.driver.find_element(*PageLocators.search_bar_text_field).is_displayed()

    def is_search_bar_collapsed(self):
        if not self.is_search_bar_visible():
            return True

    def type_search_criteria(self, search_criteria):
        self.driver.find_element(*PageLocators.search_bar_text_field).send_keys(search_criteria)

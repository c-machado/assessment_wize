from tests.pages.locators import PageLocators

class searchAmazon:

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    def type_search_criteria(self, text_to_search):
        search_bar = self.driver.find_element(PageLocators.amazon_search_field)
        search_bar.send_keys(text_to_search)

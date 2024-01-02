from tests.pages.locators import PageLocators


class Home:

    def __init__(self, driver):
        self.driver = driver

    def add_an_item_to_cart(self):
        self.driver.click_to_element(PageLocators.add_item_cta)

    def is_remove_btn_visible(self):
        return self.driver.find_element(*PageLocators.remove_item_cta).is_displayed()

    def remove_item(self):
        self.driver.click_to_element(PageLocators.remove_item_cta)

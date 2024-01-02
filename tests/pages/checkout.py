from tests.pages.locators import PageLocators


class CheckoutSauce:

    def __init__(self, driver):
        self.driver = driver

    def confirm_item_title(self):
        return self.driver.find_element(*PageLocators.item_title).get_attribute("innerHTML")

    def confirm_item_description(self):
        return self.driver.find_element(*PageLocators.item_description).get_attribute("innerHTML")

    def confirm_quantity(self):
        return self.driver.find_element(*PageLocators.item_quantity).get_attribute("innerHTML")


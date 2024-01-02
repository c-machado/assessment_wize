import time
import logging


from tests.pages.locators import PageLocators

class Checkout:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def fill_out_user(self, name):
        self.logger.info('%s name in example: ', name)
        input_name = self.driver.find_element(*PageLocators.checkout_username)
        input_name.send_keys(name)

    def click_to_choose_country(self, country):
        from selenium.webdriver.common.by import By
        languages = self.driver.get_select_options(PageLocators.checkout_country)
        for lang in languages.options:
            if lang.get_attribute("innerHTML") == country:
                country_value = lang.get_attribute("value")
                self.driver.find_element(By.CSS_SELECTOR, '#billing_country option[value=' + '% s' % country_value + ']').click()



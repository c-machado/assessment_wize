from tests.consts.constants import Constants
from tests.pages.locators import PageLocators


class Login:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self):
        username_field = self.driver.find_element(*PageLocators.username_login)
        username_field.send_keys(Constants.USERNAME)

    def enter_password(self):
        password_field = self.driver.find_element(*PageLocators.password_login)
        password_field.send_keys(Constants.PASSWORD)

    def click_to_login(self):
        self.driver.click_to_element(PageLocators.cta_login)

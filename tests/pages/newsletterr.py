import time

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Newsletter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def confirm_newsletter_subscription(self):
        return self.driver.find_element(*PageLocators.newsletter_subscribed_msg)

    def close_newsletter_modal(self):
        self.driver.click_to_element(PageLocators.newsletter_close_icon)

    def enter_first_name(self):
        first_name = self.driver.find_element(*PageLocators.newsletter_first_name_field)
        first_name.send_keys(Constants.NEWSLETTER_FIRST_NAME)

    def enter_email(self):
        email = self.driver.find_element(*PageLocators.newsletter_email_field)
        email.send_keys(Constants.NEWSLETTER_EMAIL)

    def modal_not_visible(self):
        self.driver.wait_for_element_not_visible(PageLocators.newsletter_modal)

    # TODO: check what is valid to confirm the success modal is visible
    def submit_newsletter_form(self):
        self.driver.click_to_element(PageLocators.newsletter_subscribe_cta)
        time.sleep(1)
        self.driver.wait_for_element_visible(PageLocators.newsletter_success_modal)

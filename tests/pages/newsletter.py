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

    def confirm_newsletter_sticky_subscription(self):
        return self.driver.find_element(
            *PageLocators.newsletter_sticky_subscribed_msg
        )

    def confirm_newsletter_homepage_subscription(self):
        return self.driver.find_element(
            *PageLocators.newsletter_homepage_subscribed_msg
        )

    def close_newsletter_modal(self):
        self.driver.click_to_element(PageLocators.newsletter_close_icon)

    def enter_email(self, email):
        email_field = self.driver.find_element(
            *PageLocators.newsletter_email_field
        )
        email_field.send_keys(email)

    def enter_email_in_sticky(self, email):
        time.sleep(1)
        email_field = self.driver.find_element(
            *PageLocators.newsletter_sticky_email_field
        )
        email_field.send_keys(email)

    def get_email_message_error(self):
        email_error = self.driver.find_element(
            *PageLocators.newsletter_error_email
        ).get_attribute('innerHTML')
        return email_error

    def get_email_message_error_in_sticky(self):
        email_error = self.driver.find_element(
            *PageLocators.newsletter_sticky_error_email
        ).get_attribute('innerHTML')
        return email_error

    def modal_not_visible(self):
        self.driver.wait_for_element_not_visible(PageLocators.newsletter_modal)

    # TODO: check what is valid to confirm the success modal is visible
    def submit_newsletter_form(self):
        self.driver.click_to_element(PageLocators.newsletter_subscribe_cta)
        time.sleep(1)
        self.driver.wait_for_element_visible(
            PageLocators.newsletter_success_modal
        )

    def submit_newsletter_sticky_form(self):
        self.driver.click_to_element(
            PageLocators.newsletter_sticky_subscribe_cta
        )
        time.sleep(1)

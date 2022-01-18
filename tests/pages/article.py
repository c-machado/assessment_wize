import time
import random

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class ArticlePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_date_in_article(self):
        return self.driver.find_element(*PageLocators.article_published_at)

    @staticmethod
    def get_date_format_per_locale(locale):
        for locale_format, date_format in Constants.DATE_FORMAT_PER_LOCALE.items():
            if locale_format == locale:
                return date_format

    # TODO: Install a new locale on MAC, so India can be tested with the corresponding label en_IN,
    # meanwhile it will be tested with en_GB which is basically the same format than en_IN
    def is_date_format_correct(self, date, date_format, locale_string):
        date_string = date.get_attribute("innerHTML")
        print('date_string', date.get_attribute("innerHTML"))
        print('date_format', date_format)
        from datetime import datetime
        self.set_locale(locale_string)
        print('date locale updated: ', datetime.strptime(date_string, date_format))
        try:
            is_format_expected = bool(datetime.strptime(date_string, date_format))
        except ValueError:  # wrong date format
            is_format_expected = False
        print("Does date match format? : " + str(is_format_expected))
        return is_format_expected

    @staticmethod
    def set_locale(locale_string):
        import locale
        locale.setlocale(locale.LC_ALL, locale_string)
        loc = locale.getlocale()
        print(loc)



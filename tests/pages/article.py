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






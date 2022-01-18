import time
import random

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_articles_in_feed_list(self):
        articles_list = self.driver.find_elements(*PageLocators.feed_articles_list)
        return articles_list

    def get_random_article_in_feed(self):
        random_article = random.randint(1, len(self.get_articles_in_feed_list())-1)
        return random_article

    def click_to_random_article(self):
        article_list = self.get_articles_in_feed_list()
        random_article = self.get_random_article_in_feed()
        print('random_article:', random_article)
        for article in range(1, len(article_list)):
            if article == random_article:
                print('article in article list: ', article_list[article].get_attribute("innerHTML"))
                self.driver.wait_for_element_visible(article_list[article])
                article_list[article].click()


from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class Homepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.random_article = 0

    def click_to_read_more_article(self):
        self.driver.click_to_element(PageLocators.article_read_more_cta)

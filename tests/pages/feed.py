import logging
import datetime
import time

from tests.consts import api_const
from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.base_page_api import BasePageAPI
from tests.pages.locators import PageLocators


class Feed(BasePage, BasePageAPI):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.random_article = 0
        self.logger = logging.getLogger(__name__)

    def get_articles_in_feed_list(self):
        self.driver.wait_for_page_load()
        self.driver.wait_for_feed_to_load(*PageLocators.feed_articles_list)
        # time.sleep(1)
        articles_list = self.driver.find_elements(*PageLocators.feed_articles_list)
        return articles_list

    def get_article_dates_in_feed_list(self):
        """:return list of strings with the article dates in the feed """
        article_dates = self.driver.find_elements(*PageLocators.feed_article_dates_list)
        article_dates_in_feed = []
        for article_date in article_dates:
            article_dates_in_feed.append(article_date.get_attribute("innerHTML"))
        return article_dates_in_feed

    def get_article_dates_in_feed_with_year(self):
        article_dates_list = self.driver.find_elements(*PageLocators.feed_article_dates_list)
        dates_with_year_list = []
        for date in article_dates_list:
            date_with_year = date.get_attribute("outerHTML").split('datetime="')[1]
            dates_with_year_list.append(date_with_year[0:10])
        return dates_with_year_list

    def get_article_titles_in_feed(self):
        article_titles_list = self.driver.find_elements(*PageLocators.feed_article_titles_list)
        titles_list = []
        for article_title in article_titles_list:
            if self.contains_ampersand_char(article_title.get_attribute("innerHTML")):
                titles_list.append(self.replace_ampersand_char(article_title.get_attribute("innerHTML")))
            else:
                titles_list.append(article_title.get_attribute("innerHTML"))
            self.logger.info('%s article_title.get_attribute("innerHTML")', article_title.get_attribute("innerHTML"))
        return titles_list

    def get_date_article_in_feed(self):
        """To capture the date shown in an article in the feed"""
        """:return e.g. Jan 20 / Dec 2021"""
        article_date_list = self.get_article_dates_in_feed_list()
        for article_date_index in range(0, len(article_date_list)):
            self.logger.info('%s article_date_index', article_date_index)
            self.logger.info('%s actual_article_date_in_feed_to_return', article_date_list[article_date_index])
            if article_date_index == self.random_article:
                self.logger.info('%s article_date_index', article_date_index)
                self.logger.info('%s actual_article_date_in_feed_to_return', article_date_list[article_date_index])
                return article_date_list[article_date_index]

    def get_date_first_article_in_feed(self, keyword_url):
        self.go_back_previous_page()
        self.close_bar(PageLocators.cookie_banner_ok_cta)
        date_in_first_article = self.get_article_dates_in_latest_api(keyword_url)[0]
        self.logger.info('%s date_in_api', date_in_first_article)
        self.logger.info(date_in_first_article)
        return date_in_first_article

    def get_date_from_article_in_feed_in_latest_api(self, keyword_url):
        """:return published date from the current random article in API format"""
        """we need to navigate different new category pages, since the first article in the api is not showed in the 
        feed as in the other pages"""
        article_dates_in_api = self.get_article_dates_in_latest_api(keyword_url)
        start_range = 0
        if self.is_category_page_horizontal(keyword_url):
            start_range = 1
        random_temp = start_range + self.random_article
        for index in range(start_range, len(article_dates_in_api)):
            self.logger.info('%s index api', index)
            self.logger.info('%s date expected in api format:', article_dates_in_api[index])
            if index == random_temp:
                self.logger.info('%s random temp', random_temp)
                self.logger.info('%s index api', index)
                self.logger.info('%s date expected in api format:', article_dates_in_api[index])
                return article_dates_in_api[index]

    def get_date_format_in_feed_per_locale(self, locale, date):
        """:return date in API in corresponding format based on the locale and year"""
        """To capture the format that applies based on the current random article"""
        """It should be Month Day (if the year is the same as the current one)"""
        """It should be Month Year (if the year is the previous tp the current one)"""
        # date_article_in_api = self.get_date_from_article_in_feed_in_latest_api(keyword_url)
        year_current_article = self.get_year_in_given_date(date, Constants.DATE_FORMAT_IN_API)
        current_year = datetime.datetime.now().year
        if current_year == year_current_article:
            return self.get_format_current_year(locale, Constants.DATE_FORMAT_IN_FEED_PER_LOCALE, date)
        elif year_current_article < current_year:
            return self.get_format_previous_year(locale, Constants.DATE_FORMAT_IN_FEED_PAST_YEAR_PER_LOCALE, date)

    def click_to_random_article_in_feed(self, keyword):
        time.sleep(1)
        article_list = self.get_articles_in_feed_list()
        print('random_article in click article_index:', self.random_article, 'len(article_list)', len(article_list))
        for article_index in range(0, len(article_list)):
            print('article_index', article_index)
            if article_index == self.random_article:
                print('article_index', article_index)
                self.driver.wait_for_feed_to_load(*PageLocators.feed_articles_list)
                self.driver.wait_for_element_visible(article_list[article_index])
                self.driver.wait_for_element_clickable(article_list[article_index])
                time.sleep(2)
                self.scroll_to_feed(self.random_article, keyword)
                article_list[article_index].click()
                # time.sleep(1)

    def click_load_more_stories_in_feed(self):
        self.driver.wait_for_feed_to_load(*PageLocators.feed_articles_list)
        self.scroll_to_bottom()
        if len(self.get_articles_in_feed_list()) > 6:
            self.driver.click_to_element(PageLocators.feed_load_more)

    def close_toast_banner(self):
        self.close_bar(PageLocators.toast_bar_close_cta)

    def confirm_articles_in_feed_homepage(self, keyword_url):
        headlines_in_feed = self.get_article_titles_in_feed()
        headlines_in_api = self.get_article_titles_in_latest_api(keyword_url)
        if headlines_in_api == headlines_in_feed:
            return True
        else:
            return False

    # TODO: sometimes this test is failing in mobile because the toast bar is appearing in the category pages,
    #  we need to confirm if that what is expected
    def confirm_tagging_in_feed_articles(self, keyword_url):
        """:return True if the article randomly selected contains a valid tag according to the current category page"""
        primary_tags_articles_in_feed = self.get_article_tags_in_latest_api(keyword_url)
        # primary_tags_articles_in_feed = self.get_tag_articles_in_feed()
        self.scroll_to_feed(self.random_article, keyword_url)
        article_tag_in_feed = primary_tags_articles_in_feed[self.random_article]
        # print('RANDOM in tag', self.random_article, 'TAG IN FEED:', article_tag_in_feed)
        tags_per_cat_page = self.get_primary_tags(keyword_url)
        # print('tags_per_cat_page', tags_per_cat_page)
        secondary_tags = self.get_secondary_tags(keyword_url)
        # print('secondary_tags', secondary_tags)
        tags_intersection = set(secondary_tags) & set(tags_per_cat_page)
        # print('tags_intersection', tags_intersection)
        if article_tag_in_feed in tags_per_cat_page:
            # print('match 1 article_tag_in_feed', article_tag_in_feed, 'tags_per_cat_page', tags_per_cat_page)
            return True
        elif tags_intersection:
            # print('match 2 tag that matches', tags_intersection)
            return True
        elif tags_per_cat_page in secondary_tags:
            # print('match 3 tag that matches tags_per_cat_page', tags_per_cat_page, 'secondary_tags', secondary_tags)
            return True
        else:
            return False

    def get_primary_tags(self, keyword_url):
        api_url = self.get_api_url(keyword_url, api_const.LATEST_FEED)
        self.logger.info('%s api_url', api_url)
        primary_tags = self.get_tags_in_api_url(api_url)
        self.logger.info('%s primary_tags', primary_tags)
        return primary_tags

    def get_secondary_tags(self, keyword_url):
        from tests.pages.article import ArticlePage
        articles_in_feed = self.get_articles_in_feed_list()
        self.scroll_to_feed(self.random_article, keyword_url)
        articles_in_feed[self.random_article].click()
        secondary_tags = ArticlePage(self.driver).get_secondary_tags_in_article_api_format()
        self.logger.info('%s secondary_tags', secondary_tags)
        return secondary_tags

    def get_tag_articles_in_feed(self):
        tags_list = self.driver.find_elements(*PageLocators.search_eyebrow_articles_in_feed)
        tags = []
        print(len(tags_list))
        for index, element in enumerate(tags_list):
            tag_eyebrow = self.remove_html_tags(element.get_attribute("innerHTML"))
            tag_eyebrow_principal = tag_eyebrow.split("/ ")[1]
            self.logger.info('%s tag before replacing space', tag_eyebrow_principal)
            tag_eyebrow_principal = self.replace_space(tag_eyebrow_principal.lower())
            self.logger.info('%s tag after replacing space', tag_eyebrow_principal)
            tags.append(tag_eyebrow_principal)
        return tags

    def get_articles_indexes_matching_sitespace_tag(self, eyebrow_in_articles, sitespace):
        """:return: a list of indexes of the articles that has the same tag from the site space"""
        articles_indexes_with_sitespace_tag = []
        print(len(eyebrow_in_articles))
        for index, element in enumerate(eyebrow_in_articles):
            tag_eyebrow = self.remove_html_tags(element.get_attribute("innerHTML"))
            tag_eyebrow_principal = tag_eyebrow.split("/ ")[1]
            if sitespace == tag_eyebrow_principal:
                articles_indexes_with_sitespace_tag.append(index)
        return articles_indexes_with_sitespace_tag

    def get_eyebrows_in_feed_site_space_page(self):
        return self.driver.find_elements(*PageLocators.search_eyebrow_articles_in_feed)

    def click_on_sitespace_element(self, index, keyword):
        self.close_bar(PageLocators.cookie_banner_ok_cta)
        self.scroll_to_feed(index, keyword)
        index += 1
        from selenium.webdriver.common.by import By
        self.driver.find_element(By.CSS_SELECTOR, '.feed-article.ng-scope:nth-child(' + "% s" % index + ')').click()

import datetime
import time
import logging
import requests

from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class ArticlePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click_to_mute_video(self):
        self.driver.click_to_element(PageLocators.article_mute_video)

    def click_to_pause_video(self):
        self.driver.click_to_element(PageLocators.article_pause_video)

    def click_to_play_video(self, video_type):
        self.driver.wait_for_page_load()
        time.sleep(3)
        if video_type == 'hero':
            self.driver.click_to_element(PageLocators.article_play_hero_video)
            self.driver.switch_to_iframe(PageLocators.article_video_hero_frame)
        elif video_type == 'body':
            self.driver.click_to_element(PageLocators.article_play_embed_video)
            self.driver.switch_to_iframe(PageLocators.article_video_body_frame)
        time.sleep(3)

    def click_to_see_subtitles(self):
        self.driver.click_to_element(PageLocators.article_see_subtitles)

    def close_cookie_banner(self):
        self.close_bar(PageLocators.cookie_banner_ok_cta)

    def confirm_internal_status(self):
        urls = self.get_urls_params()
        for internal_link in urls.values():
            response = requests.get(internal_link[0])
            if response != 404:
                self.logger.info(response)
                self.logger.info(internal_link)
            assert response.status_code != 404

    def get_current_time_video(self):
        current_time = self.driver.find_element(
            *PageLocators.article_current_time
        )
        time_formatted = current_time.get_attribute('innerHTML').split(':')[1]
        return int(time_formatted)

    def get_date_in_article(self):
        return self.driver.find_element(*PageLocators.article_published_at)

    def get_secondary_tags_in_article_api_format(self):
        secondary_tags_list = self.driver.find_elements(
            *PageLocators.article_secondary_tags
        )
        tags_in_article = []
        for element in secondary_tags_list:
            tag_string = element.get_attribute('innerHTML')
            tag = self.replace_space(tag_string)
            tags_in_article.append(tag.lower())
        return tags_in_article

    def get_primary_tag_in_article(self):
        return self.driver.find_element(
            *PageLocators.article_primary_tag
        ).get_attribute('innerHTML')

    def get_urls_params(self):
        elements = self.driver.find_elements(*PageLocators.article_inline_links)
        urls_dict = {}
        index = 0
        for element in elements:
            index += 1
            print('href', element.get_attribute('href'))
            print('target', element.get_attribute('target'))
            if (
                element.get_attribute('href') is not None
                and element.get_attribute('target') is None
                or element.get_attribute('target') == ''
            ):
                urls_dict.setdefault(index, []).append(
                    element.get_attribute('href')
                )
            elif (
                element.get_attribute('href') is not None
                and element.get_attribute('target') is not None
            ):
                urls_dict.setdefault(index, []).append(
                    element.get_attribute('href')
                )
                urls_dict.setdefault(index, []).append(
                    element.get_attribute('target')
                )
        return urls_dict

    def validate_inline_links_in_article(self):
        href_and_target_params = self.get_urls_params()
        flag_target = True
        for param in href_and_target_params.values():
            self.logger.info('%s url + target', param)
            if len(param) > 1 and param[0].startswith('https://blog.google'):
                flag_target = False
        return flag_target

    def click_on_carousel_dot(self, index):
        index = '% s' % index
        self.driver.find_element(
            By.CSS_SELECTOR,
            '.uni-related-articles-cards__pagination :nth-child(' + index + ')',
        ).click()
        self.driver.wait_for_element_visible(
            By.CSS_SELECTOR,
            '.uni-related-articles-cards__wrap > li:nth-child(' + index + ')',
        )
        self.driver.wait_for_element_clickable(
            By.CSS_SELECTOR,
            '.uni-related-articles-cards__wrap > li:nth-child(' + index + ')',
        )

    def validate_tags_in_related_stories(self):
        """return True if the list of article in related articles section match the tagging in the current article"""
        formatted_tags = self.find_tags_in_related_stories()
        self.logger.info('%s formatted_tags in stories related', formatted_tags)
        tags_in_article = self.get_secondary_tags_in_article()
        self.logger.info('%s tags_in_article', tags_in_article)
        for index, tag in enumerate(formatted_tags):
            if tag not in tags_in_article:
                self.validate_secondary_tags_in_related_articles(
                    index + 1, tags_in_article
                )
        if set(formatted_tags) & set(tags_in_article):
            self.logger.info(
                '%s matching tags', set(formatted_tags) & set(tags_in_article)
            )
            return True

    def find_tags_in_related_stories(self):
        list_of_tags = self.driver.find_elements(
            *PageLocators.article_related_stories_category_tags
        )
        return [tag.get_attribute('innerHTML') for tag in list_of_tags]

    def validate_secondary_tags_in_related_articles(
        self, index, tags_in_article
    ):
        secondary_tags_in_related_article = (
            self.find_secondary_tags_in_related_stories_articles(index)
        )
        if set(secondary_tags_in_related_article) & set(tags_in_article):
            return True
        else:
            return False

    def find_secondary_tags_in_related_stories_articles(self, index):
        self.click_on_carousel_dot(index)
        time.sleep(1)
        index = '% s' % index
        element = self.driver.find_element(
            By.CSS_SELECTOR,
            '.uni-related-articles-cards__wrap > li:nth-child(' + index + ')',
        )
        self.driver.wait_for_element_visible(element)
        element.click()
        secondary_tags_related_article = self.get_secondary_tags_in_article()
        self.driver.go_back_to_url()
        time.sleep(1)
        self.logger.info(
            '%s secondary_tags_related_article', secondary_tags_related_article
        )
        return secondary_tags_related_article

    def get_secondary_tags_in_article(self):
        secondary_tags_list = self.driver.find_elements(
            *PageLocators.article_secondary_tags
        )
        return [
            element.get_attribute('innerHTML').strip()
            for element in secondary_tags_list
        ]

import datetime
import time
import random
import bs4
import requests
from selenium.common.exceptions import WebDriverException

from tests.consts.constants import Constants
from tests.pages.base_page import BasePage
from tests.pages.locators import PageLocators


class ArticlePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_to_mute_video(self):
        self.driver.click_to_element(PageLocators.article_mute_video)

    def click_to_pause_video(self):
        self.driver.click_to_element(PageLocators.article_pause_video)

    def click_to_play_video(self, video_type):
        if video_type == 'hero':
            self.driver.click_to_element(PageLocators.article_play_hero_video)
        elif video_type == 'body':
            self.driver.click_to_element(PageLocators.article_play_embed_video)
        time.sleep(2)

    def click_to_see_subtitles(self):
        self.driver.click_to_element(PageLocators.article_see_subtitles)

    def close_cookie_banner(self):
        self.close_bar(PageLocators.cookie_banner_ok_cta)

    def confirm_internal_status(self):
        inline_links = self.driver.get_urls_list(PageLocators.article_inline_links)
        for internal_link in inline_links:
            response = requests.get(internal_link)
            if response != 404:
                print('response', response, 'internal', internal_link)
            assert response.status_code != 404

    def find_tags_in_related_stories(self):
        tags_in_related_stories = []
        list_of_tags = self.driver.find_elements(*PageLocators.article_related_stories_category_tags)
        for tag in list_of_tags:
            tags_in_related_stories.append(tag.get_attribute("innerHTML"))
        return tags_in_related_stories

    def find_secondary_tags_in_related_stories_articles(self, tags_in_article):
        tags_in_related_stories = []
        list_of_tags = self.driver.find_elements(*PageLocators.article_related_stories_category_tags)
        for tag in list_of_tags:
            if tag not in tags_in_article:
                tag.click()
                secondary_tags = self.get_secondary_tags_in_article()
                tags_in_related_stories.append(secondary_tags)
        for e in tags_in_related_stories:
            print('caro', e)

    def get_current_time_video(self):
        current_time = self.driver.find_element(*PageLocators.article_current_time)
        time_formatted = current_time.get_attribute("innerHTML").split(':')[1]
        return int(time_formatted)

    def get_date_in_article(self):
        return self.driver.find_element(*PageLocators.article_published_at)

    def get_secondary_tags_in_article_api_format(self):
        secondary_tags_list = self.driver.find_elements(*PageLocators.article_secondary_tags)
        tags_in_article = []
        for element in secondary_tags_list:
            tag_string = element.get_attribute("innerHTML")
            tag = self.replace_space(tag_string)
            tags_in_article.append(tag.lower())
        return tags_in_article

    def get_secondary_tags_in_article(self):
        secondary_tags_list = self.driver.find_elements(*PageLocators.article_secondary_tags)
        tags_in_article = []
        for element in secondary_tags_list:
            tag_string = element.get_attribute("innerHTML")
            tags_in_article.append(tag_string.strip())
        return tags_in_article

    def get_primary_tag_in_article(self):
        return self.driver.find_element(*PageLocators.article_primary_tag).get_attribute("innerHTML")

    def get_urls_params(self, locator):
        elements = self.driver.find_elements(*locator)
        urls_dict = {}
        index = 0
        for element in elements:
            index += 1
            href = element.get_attribute("href")
            if element.get_attribute("target"):
                urls_dict.setdefault(index, []).append(href)
                urls_dict.setdefault(index, []).append(element.get_attribute("target"))
            else:
                urls_dict.setdefault(index, []).append(href)
        print(urls_dict)
        return urls_dict

    def validate_inline_links_in_article(self):
        inline_links = self.get_urls_params(PageLocators.article_inline_links)
        print(len(inline_links))
        flag_target = 0
        for link in inline_links.values():
            if link[0].startswith("https://blog.google") and len(link) > 1:
                flag_target = 1
        return flag_target

    def validate_tags_in_related_stories(self):
        tags_in_article = set(self.get_secondary_tags_in_article())
        for e in tags_in_article:
            print('secondary', e)
        tags_in_related_stories = set(self.find_tags_in_related_stories())
        for e in tags_in_related_stories:
            print('relate', e)
        if not tags_in_related_stories == tags_in_article:
            self.find_secondary_tags_in_related_stories_articles(tags_in_article)


    @staticmethod
    def find_all_links(url):
        # download the page
        print('parsing...')  # displaying text while parsing the page
        res = requests.get(Constants.BASE_URL + url)  # takes the string of the url to download
        res.raise_for_status()  # will raise exception if error downloading
        # retrieve all the links
        soup = bs4.BeautifulSoup(res.text)
        # print('all', soup.prettify())
        linkel = soup.select('.uni-container > a')  # could be altered as required
        # print(linkel)
        # return a set of links
        numOpen = len(linkel)
        # print(numOpen) #optional for console validation
        linkel2 = []
        for i in range(numOpen):
            linkel2 = linkel2 + [(linkel[i].get('href'))]
            print('linkel2', linkel2)
        return linkel2

    def page_hits(self, url):
        # log events and pagename
        # put the block in try/except
        try:
            pageName = self.driver.execute_script("return (s.pageName);")
            events = self.driver.execute_script("return (s.events);")
            print(pageName)  # optional for console validation
            print(events)  # optional for console validation
            Constants.HTML_string += '''<tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>'''.format(url, pageName, events)
            Constants.HTML_string += "</tr>"
        except WebDriverException:
            print("Exception on {}".format(url))

    def switch_to_video_context(self):
        self.driver.switch_to_iframe(PageLocators.article_video_frame)

    def test(self, keyword):
        url_list = self.find_all_links(Constants.BASE_URL + keyword)
        # Iterate the links and collect data
        for i in range(len(url_list)):
            # for i in range(10,15): #optional for initial validation
            tag_link = str(url_list[i])
            print('tag_link', tag_link)
            if tag_link.startswith('/'):
                self.page_hits(tag_link)
            elif tag_link.startswith('http' or 'www' or 'https'):
                self.page_hits(tag_link)
            else:
                continue
        # Append the closing html
        Constants.HTML_string += '''</table></body></html>'''
        # Write the HTML to a file
        HTML_file = open("file.html", "w")
        HTML_file.write(Constants.HTML_string)
        HTML_file.close()











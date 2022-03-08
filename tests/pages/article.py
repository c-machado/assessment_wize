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

    def confirm_share_video(self):
        self.driver.click_to_element(PageLocators.article_share_video)
        # link_to_share = self.driver.find_element(*PageLocators.article_share_video_link).get_attribute("innerHTML")
        # print(link_to_share)

    def get_current_time_video(self):
        current_time = self.driver.find_element(*PageLocators.article_current_time)
        time_formatted = current_time.get_attribute("innerHTML").split(':')[1]
        return int(time_formatted)

    def get_date_in_article(self):
        return self.driver.find_element(*PageLocators.article_published_at)

    def get_secondary_tags_in_article(self):
        secondary_tags_list = self.driver.find_elements(*PageLocators.article_secondary_tags)
        tags_in_article = []
        for element in secondary_tags_list:
            tag_string = element.get_attribute("innerHTML")
            tag = self.replace_space(tag_string)
            tags_in_article.append(tag.lower())
        return tags_in_article

    @staticmethod
    def find_all_links(url):
        # download the page
        print('parsing...')  # displaying text while parsing the page
        res = requests.get(url)  # takes the string of the url to download
        res.raise_for_status()  # will raise exception if error downloading
        # retrieve all the links
        soup = bs4.BeautifulSoup(res.text)
        print('all', soup.prettify())
        linkel = soup.find(class_='ytp-youtube-button')  # could be altered as required
        print(linkel)
        # return a set of links
        numOpen = len(linkel)
        print(numOpen) #optional for console validation
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











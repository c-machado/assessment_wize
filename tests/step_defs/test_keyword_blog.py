import time

import pytest
import requests
from pytest_bdd import scenarios, given, when, then

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

scenarios("../features/")

BASE_URL = 'https://blog.google'
# BASE_URL = 'https://gweb-uniblog-publish-stage.appspot.com/supportingnews'
# BASE_URL = 'https://www.google.com/'


@given("a user is at the <keyword> site")
def at_the_blog(keyword, browser, get_web_browser, get_viewport):
    print('keyword url', BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    browser.start(get_web_browser, get_viewport)
    browser.go_to_URL(BASE_URL + keyword)
    # browser.set_cookie()
    # browser.refresh()


@when("I click on every <social_media> item")
def click_on_social(footer, social_media):
    footer.click_social_media_item(social_media)


# Checking status 200 or 429, because instagram and linkedin redirects to authentication pages
@then("the user is redirected to <url>")
def redirect_to_url_new_tab(browser, base_page, url):
    browser.switch_to_active_tab()
    time.sleep(1)
    assert base_page.get_status_redirect() == 200 or base_page.get_status_redirect() == 429
    assert browser.current_url().__contains__(url)


@when("I click on legal items")
def click_on_legal_links(footer):
    legal_links = footer.get_legal_links()
    for link in legal_links:
        response = requests.get(legal_links[link])
        assert response.status_code == 200


@then("the user sees the url according to <keyword> locale")
def confirm_legal_urls(footer, keyword):
    url = BASE_URL + keyword
    legal_items_dict = footer.get_legal_links()
    if url == "https://blog.google/":
        assert legal_items_dict == Constants.LEGAL_LINKS_FOOTER_US_LOCALE_DICT

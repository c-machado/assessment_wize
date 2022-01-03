import time

import pytest
import requests
from pytest_bdd import scenarios, given, when, then

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

scenarios("../features/globals/")


# TODO: SEPARATE STEP FILES


@given("a user is at the <keyword> site")
def at_the_blog(keyword, driver, get_web_browser, get_viewport):
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    print('keyword', keyword)
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL + keyword)
    # browser.set_cookie()
    # browser.refresh()


@when("the user clicks on every <social_media> item")
def click_on_social(footer, social_media):
    footer.click_social_media_item(social_media)


# Checking status 200 or 429, because instagram and linkedin redirects to authentication pages
@then("the user is redirected to <url> in a new tab")
def redirect_to_url_new_tab(driver, base_page, url):
    driver.switch_to_active_tab()
    time.sleep(1)
    assert base_page.get_status_redirect() == 200 or base_page.get_status_redirect() == 429
    assert driver.current_url().__contains__(url)


@when("the user clicks on legal items")
def click_on_legal_links(footer):
    legal_links = footer.get_legal_links()
    for link in legal_links:
        response = requests.get(legal_links[link])
        assert response.status_code == 200


@then("the user sees the url according to <keyword> locale")
def confirm_legal_urls(footer, keyword):
    url = Constants.BASE_URL + keyword
    legal_items_dict = footer.get_legal_links()
    if url == "https://blog.google/":
        assert legal_items_dict == Constants.LEGAL_LINKS_FOOTER_US_LOCALE_DICT


@when("the user on <keyword> clicks the CTA See all product updates")
def click_on_cta_all_product_updates(header, keyword):
    header.click_cta_all_product_updates(keyword)


@then("the user is redirected to <url>")
def redirected_to_page(url, base_page, driver):
    assert base_page.get_status_redirect() == 200
    print('status base_page:', base_page.get_status_redirect())
    print('url:', url)
    print('current url:', driver.current_url())
    assert driver.current_url().__contains__(url)


@when("the user clicks on the <submenu>")
def user_clicks_to_submenu(header, submenu):
    header.click_on_submenu_item(submenu)


@pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="requests.exceptions.ConnectionError: ('Connection aborted.',"
                                                      " TimeoutError(60, 'Operation timed out'))")
@then("every link in the <submenu> selected return an Http 200")
def check_http_status_internal_links(header, submenu):
    submenu_items = header.get_url_submenu_items(submenu, PageLocators.submenu_items_locators)
    header.check_internal_status(submenu_items)


@then("every 'see all' CTA selected return an http 200")
def user_clicks_to_see_all_within_company_menu(header):
    header.click_see_all_cta_sub_menu()


@when("the user triggers the kebab menu")
def user_trigger_kebab_menu(header):
    header.click_on_kebab_menu()


@then("the user sees <kebab_option> according to <locale>")
def user_sees_rss_and_press_options(header, kebab_option, locale):
    header.confirm_kebab_menu_opts(locale, kebab_option)

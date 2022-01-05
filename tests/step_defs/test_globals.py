import time

import pytest
import requests
from pytest_bdd import scenarios, given, when, then

from tests.consts.constants import Constants
from tests.pages.cookie_banner import CookieBanner
from tests.pages.footer import Footer
from tests.pages.header import Header
from tests.pages.locators import PageLocators
from tests.pages.newsletterr import Newsletter

scenarios("../features/globals/")

BASE_URL = 'https://blog.google'


# BASE_URL = 'https://gweb-uniblog-publish-stage.appspot.com/supportingnews'


@given("a user is at the <keyword> site")
def at_the_blog(keyword, driver, get_web_browser, get_viewport):
    print('keyword url', BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL + keyword)
    driver.wait_for_page_load()
    # browser.set_cookie()
    # browser.refresh()


@when("the user clicks on every <social_media> item")
def click_on_social(footer, social_media):
    footer.click_social_media_item(social_media)
    time.sleep(1)


# Checking status 200 or 429, because instagram and linkedin redirects to authentication pages
@pytest.mark.flaky(reruns=1, reruns_delay=0.5)
@then("the user is redirected to <url> in a new tab")
def redirect_to_url_new_tab(driver, base_page, url):
    driver.switch_to_active_tab()
    # time.sleep(1)
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


@when("the user clicks on language selector")
def user_clicks_on_language_selector(driver, footer):
    footer.go_to_footer()
    driver.click_to_element(PageLocators.language_selector)


@then("the system displays the selector with the corresponding <locale>")
def confirm_language_options(driver, footer, locale):
    assert footer.verify_language_selector_content(locale)


@given("the system displays the cookie banner per <language>")
def verify_cookie_banner_displayed(cookie_banner, language):
    assert cookie_banner.get_cookie_text_per_language(language) == cookie_banner.get_cookie_text_in_page()


@given("the user clicks in the Ok cta")
def user_clicks_ok_cookies_msg(cookie_banner):
    cookie_banner.close_cookie_banner()


@given("the user clicks in the hero article")
def user_clicks_hero_article(cookie_banner):
    cookie_banner.click_to_read_more_article()


@when("the user clicks the see details CTA")
def user_clicks_see_details_cta(cookie_banner):
    cookie_banner.click_see_details_cta()


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


@then("the cookie banner is not displayed")
def cookie_not_displayed(cookie_banner):
    cookie_banner.cookie_not_displayed()


@when("the user clicks on subscribe cta")
def user_clicks_subscribe_cta(header):
    header.click_on_subscribe_cta()


@when("the user fills out the form")
def user_fills_out_newsletter_form(newsletter):
    newsletter.enter_first_name()
    newsletter.enter_email()


@when("the user submits the information")
def user_submit_form(newsletter):
    newsletter.submit_newsletter_form()


@then("the system displays confirmation message")
def verify_confirmation_msg(newsletter, base_page):
    message = newsletter.confirm_newsletter_subscription().text
    formatted_message = base_page.remove_enter(message)
    print('formatted_message', formatted_message)
    print('expected_message', Constants.NEWSLETTER_CONFIRMATION)
    assert Constants.NEWSLETTER_CONFIRMATION == formatted_message


@when("the user clicks on subscribe cta in the toast")
def user_clicks_subscribe_cta_toast(cookie_banner, footer, header):
    footer.go_to_footer()
    header.click_on_subscribe_cta_toast()


@when("the user closes the modal")
def user_clicks_to_close_newsletter_modal(newsletter):
    newsletter.close_newsletter_modal()


@then("the system hides the modal")
def newsletter_modal_not_visible(newsletter):
    newsletter.modal_not_visible()

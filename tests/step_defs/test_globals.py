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


@given("a user is at the <keyword> site in mobile")
def at_the_blog(keyword, driver, get_web_browser):
    print('keyword url', BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    driver.start(get_web_browser, "mobile")
    driver.go_to_URL(Constants.BASE_URL + keyword)
    driver.wait_for_page_load()
    # browser.set_cookie()
    # browser.refresh()


@when("the user clicks on every <social_media> item")
def click_on_social_item(footer, cookie_banner, social_media):
    footer.go_to_footer()
    cookie_banner.close_cookie_banner()
    footer.click_social_media_item(social_media)


# TODO: facebook urls are not secure (locales: in & au) https://jira.hugeinc.com/browse/UNI-5897
@then("the user is redirected to <url> in a new tab")
def redirect_to_url_new_tab(base_page, url):
    actual_url = base_page.get_current_page()
    print("expected url", url, "actual url", actual_url)
    assert actual_url.__contains__(url)


@when("the user clicks on legal items")
def click_on_legal_links(footer):
    legal_links = footer.get_legal_links()
    for link in legal_links:
        response = requests.get(legal_links[link])
        assert response.status_code == 200


@then("the user sees the url according to <keyword> locale")
def confirm_legal_urls(footer, keyword):
    legal_items_dict = footer.get_legal_links()
    print('legal links in page', legal_items_dict)
    expected_links = footer.get_expected_legal_links_per_locale(keyword)
    print('expected_links', expected_links)
    assert legal_items_dict == expected_links


@when("the user clicks on language selector")
def user_clicks_on_language_selector(footer):
    footer.go_to_footer()
    footer.click_to_open_language_selector()


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


@when("the user clicks the search icon")
def user_clicks_search(search):
    search.click_search_icon()


@then("the system shows the search bar expanded")
def search_bar_expanded(search):
    assert search.is_search_bar_visible()


@when("the user closes the search bar")
def user_click_close_icon_search_bar(search):
    search.close_search_bar()


@then("the system collapsed the search bar")
def search_bar_collapsed(search):
    assert search.is_search_bar_collapsed()


@when("the user types the <text_to_search>")
def user_type_criteria_to_search(text_to_search, search):
    search.type_search_criteria()


@then("the system adds the <text_to_search> as a parameter in the <keyword> url")
def user_sees_parameter_in_url(text_to_search, keyword, driver):
    url_results_page = keyword + Constants.SEARCH_URL + text_to_search
    assert url_results_page == driver.current_url()


@given("the user selects a <filter_option> the results")
def user_selects_filter(filter_option, search):
    search.get_results_by_filter(filter_option)


@then("the system updates the result based on the <filter>")
def step_impl():
    raise NotImplementedError(u'STEP: Then the system updates the result based on the <filter>')


@when("the user clicks the Google logo")
def user_clicks_google_logo(footer):
    footer.click_google_logo()


# TODO: bring date_in_article from the API
@then("the publish date matches with the <content_date>")
def confirm_date_format_in_rss(header, base_page, content_date):
    publish_date_rss = header.get_publish_date_in_rss()
    print(publish_date_rss)
    date_in_article = base_page.get_format_date(content_date, Constants.YYYY_MM_DD)
    print(date_in_article)
    assert publish_date_rss == date_in_article


@when("the user clicks <kebab_option>")
def user_clicks_rss(kebab_option, header, driver):
    header.click_on_kebab_option(kebab_option)


@when("the user triggers the hamburger menu")
def user_expand_hamburger_menu(header):
    header.click_on_hamburger_menu()


@when("the user clicks on rss option")
def user_clicks_rss_in_mobile(header):
    header.click_on_hamburger_rss()
    time.sleep(2)


@when("the user clicks on the keyword logo")
def user_clicks_keyword_logo(header):
    header.click_on_nav_logo()

import time

import pytest
import requests
from pytest_bdd import scenarios, given, when, then

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

scenarios("../features/globals/")
scenarios("../features/globals_mobile")


@given("a user is at the <keyword> site")
def at_the_blog(keyword, driver, get_web_browser, get_viewport):
    print('keyword url', Constants.BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    # time.sleep(2)
    driver.start(get_web_browser, get_viewport)
    # time.sleep(5)
    driver.go_to_URL(Constants.BASE_URL + keyword)
    driver.wait_for_page_load()


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


@then("the user sees the URL according to <keyword> locale")
def confirm_legal_urls(footer, keyword):
    legal_items_dict = footer.get_legal_links()
    expected_links = footer.get_expected_legal_links_per_locale(keyword)
    assert legal_items_dict == expected_links


@when("the user clicks on every language in the selector")
def user_clicks_on_every_language_in_selector(footer):
    footer.go_to_footer()
    footer.click_to_each_language_in_selector()


@then("the user can see all expected locales in the selector")
def confirm_language_options(footer):
    assert set(footer.languages) == set(Constants.LANGUAGE_SELECTOR)


@given("the system displays the cookie banner per <language>")
def verify_cookie_banner_displayed(cookie_banner, language):
    cookie_banner.clear_local_storage()
    assert cookie_banner.get_cookie_text_per_language(language) == cookie_banner.get_cookie_text_in_page()


@given("the user clicks in the Ok cta")
def user_clicks_ok_cookies_msg(cookie_banner):
    cookie_banner.clear_local_storage()
    cookie_banner.close_cookie_banner()


@given("the user clicks on the hero article")
def user_clicks_hero_article(cookie_banner, get_viewport):
    cookie_banner.click_to_read_more_article(get_viewport)


@when("the user clicks the see details CTA")
def user_clicks_see_details_cta(cookie_banner):
    cookie_banner.click_see_details_cta()


@when("the user on <keyword> clicks the CTA See all product updates")
def click_on_cta_all_product_updates(header, keyword, get_viewport):
    header.click_cta_all_product_updates(keyword, get_viewport)


@then("the user is redirected to <url>")
def redirected_to_page(url, base_page, driver):
    assert base_page.get_status_redirect() == 200
    assert driver.current_url().__contains__(url)


@when("the user clicks on the <submenu>")
def user_clicks_to_submenu(header, submenu, get_viewport):
    header.click_on_hamburger_menu()
    header.click_on_submenu_item(submenu, get_viewport)


@when("the user clicks on each list in the <submenu>")
def user_clicks_to_expand_submenus(header, submenu):
    header.click_submenu_items_mobile(submenu)


@pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="requests.exceptions.ConnectionError: ('Connection aborted.',"
                                                      " TimeoutError(60, 'Operation timed out'))")
@then("every link in the <submenu> selected return an Http 200")
def check_http_status_internal_links(header, submenu):
    submenu_urls = header.get_url_submenu_items(submenu, PageLocators.submenu_items_urls)
    header.check_internal_status(submenu_urls)


@then("every 'see all' CTA selected return an http 200")
def user_clicks_to_see_all_within_company_menu(header, get_viewport):
    header.click_see_all_cta_company_sub_menu(get_viewport)


@when("the user triggers the kebab menu")
def user_trigger_kebab_menu(header):
    header.click_on_kebab_menu()


@then("the user sees <kebab_option> according to <locale>")
def user_sees_rss_and_press_options(header, kebab_option, locale):
    header.confirm_kebab_menu_opts(locale, kebab_option)


@then("the cookie banner is not displayed")
def cookie_not_displayed(cookie_banner):
    cookie_banner.cookie_not_displayed()


@when("the user clicks on subscribe cta on mobile")
def user_clicks_subscribe_cta_mobile(header):
    header.close_cookie_banner()
    header.click_on_hamburger_menu()
    header.click_on_subscribe_cta_mobile()
    time.sleep(2)


@when("the user clicks on the subscribe cta in the sticky bar")
def user_clicks_subscribe_cta_mobile(header):
    header.click_on_subscribe_cta_mobile_sticky()
    time.sleep(2)


@when("the user fills out the email in the sticky bar")
def user_fills_out_newsletter_form(newsletter):
    newsletter.enter_email_in_sticky(Constants.NEWSLETTER_EMAIL)


@when("the user fills out the email on the sticky with invalid data")
def user_fills_out_form_with_invalid_data(newsletter):
    newsletter.enter_email_in_sticky(Constants.NEWSLETTER_INVALID_EMAIL)
    newsletter.submit_newsletter_sticky_form()


@when("the user fills out the form")
def user_fills_out_newsletter_form(newsletter):
    newsletter.enter_email(Constants.NEWSLETTER_EMAIL)


@when("the user submits the information on the sticky")
def user_submit_form(newsletter):
    newsletter.submit_newsletter_sticky_form()


@when("the user submits the information")
def user_submit_form(newsletter):
    newsletter.submit_newsletter_form()


@then("the system displays a confirmation message on the sticky")
def verify_confirmation_msg(newsletter, base_page):
    message = newsletter.confirm_newsletter_sticky_subscription().text
    assert Constants.NEWSLETTER_CONFIRMATION_MOBILE == message


@then("the system displays a confirmation message")
def verify_confirmation_msg(newsletter, base_page):
    message = newsletter.confirm_newsletter_subscription().text
    formatted_message = base_page.remove_enter(message)
    assert Constants.NEWSLETTER_CONFIRMATION == formatted_message


@then("the system displays a confirmation message on the homepage")
def verify_confirmation_msg(newsletter, base_page):
    message = newsletter.confirm_newsletter_homepage_subscription().text
    formatted_message = base_page.remove_enter(message)
    assert Constants.NEWSLETTER_CONFIRMATION == formatted_message

@then("the user sees an error message on sticky")
def newsletter_error_message(newsletter):
    assert newsletter.get_email_message_error_in_sticky() == Constants.NEWSLETTER_ERROR_MSG_EMAIL

@when("the user clicks on subscribe cta in the toast")
def user_clicks_subscribe_cta_toast(footer, header):
    header.click_on_subscribe_cta_toast()


@when("the user closes the modal")
def user_clicks_to_close_newsletter_modal(newsletter):
    newsletter.close_newsletter_modal()


@then("the system hides the modal")
def newsletter_modal_not_visible(newsletter):
    newsletter.modal_not_visible()


@when("the user clicks the Google logo")
def user_clicks_google_logo(footer):
    footer.close_cookie_banner()
    footer.click_google_logo()


# Per each new locale add the latest feed URL to the api_const.py, this is because the
# RSS should match the content in the feed
@then("the dates in RSS and <keyword> matches")
def confirm_date_format_in_rss(header, feed, keyword):
    publish_date_rss = header.get_publish_date_in_rss()
    date_in_first_article = feed.get_date_first_article_in_feed(keyword)
    assert publish_date_rss == date_in_first_article


@when("the user clicks <kebab_option>")
def user_clicks_rss(kebab_option, header, driver):
    header.click_on_kebab_option(kebab_option)


@when("the user triggers the hamburger menu")
def user_expand_hamburger_menu(header):
    header.click_on_hamburger_menu()


@when("the user clicks on the RSS option")
def user_clicks_rss_in_mobile(header):
    header.click_on_hamburger_rss()
    time.sleep(2)


@when("the user clicks on the keyword logo")
def user_clicks_keyword_logo(header):
    header.click_on_nav_logo()


@given("the user closes the cookie banner")
def user_closes_cookie_banner(cookie_banner):
    cookie_banner.close_cookie_banner()


@when("the user fills out the form with invalid data")
def user_fills_out_form_with_invalid_data(newsletter):
    newsletter.enter_email(Constants.NEWSLETTER_INVALID_EMAIL)
    newsletter.submit_newsletter_form()


@given("the toast bar has appeared")
def toast_bar_visible(cookie_banner, homepage, newsletter, toast_bar, get_viewport):
    cookie_banner.close_cookie_banner()
    homepage.click_to_read_more_article(get_viewport)
    toast_bar.make_toast_bar_visible()


@then("the user sees an error message")
def newsletter_error_message(newsletter):
    assert newsletter.get_email_message_error() == Constants.NEWSLETTER_ERROR_MSG_EMAIL


@when("the user closes the toast bar")
def user_closes_toast_bar(toast_bar):
    time.sleep(2)
    toast_bar.close_toast_bar()


@then("the toast bar is not visible anymore")
def toast_bar_not_visible(toast_bar):
    assert toast_bar.is_toast_bar_visible()


@when("the user clicks on a random sitespace")
def user_clicks_on_random_site_space(header):
    site_spaces_list = header.get_sitespaces_list()
    header.get_random_sitespace(site_spaces_list)
    title_expected_in_products = header.get_sitespace_title_expected_in_products()
    header.click_random_site_space(site_spaces_list)
    title_sitespace_in_products = header.site_space_title_in_products
    assert title_expected_in_products == title_sitespace_in_products


@then("the system shows the updated header")
def user_sees_sitespace_nav(header):
    assert header.site_space_url in header.get_current_page()
    title_sitespace_in_nav = header.get_site_space_title_in_navigation()
    title_expected_in_nav = header.get_sitespace_title_expected_in_nav()
    assert title_sitespace_in_nav == title_expected_in_nav


@when("the user clicks in an article in a <sitespace_tag> in <keyword>")
def user_clicks_on_random_site_space(sitespace_tag, keyword, feed):
    tags_list = feed.get_eyebrows_in_feed_site_space_page()
    articles_within_sitespace = feed.get_articles_indexes_matching_sitespace_tag(tags_list, sitespace_tag)
    random_index = feed.get_random_index_in_list(articles_within_sitespace)
    feed.click_on_sitespace_element(articles_within_sitespace[random_index], keyword)


@then("the system shows the <sitespace_title> nav menu in an article")
def user_sees_nav_sitespace_in_article(sitespace_title, header):
    title_in_sitespace_nav = header.get_site_space_title_in_navigation()
    assert title_in_sitespace_nav == sitespace_title


@when("the user clicks on every social media")
def user_clicks_on_every_social_link(footer):
    assert footer.click_all_social_media_links()


@then("the system opens each link in a new tab")
def each_link_opens_in_a_new_tab(footer):
    assert footer.confirm_links_opened_in_a_new_tab()


@then("the system shows a secure url per each link")
def url_per_social_media_is_secure(footer):
    assert footer.confirm_social_media_url_is_secure()


@then("the system shows the waze header")
def test_header_waze_sitespace(header):
    title_sitespace_in_nav = header.get_site_space_title_in_navigation()
    assert title_sitespace_in_nav == Constants.SITESPACE_WAZE_IN_NAV_MENU


@given("a user navigates to <url_from>")
def user_navigate_to_previous_redirect(url_from, driver):
    time.sleep(5)
    driver.go_to_URL(Constants.BASE_URL + url_from)
    time.sleep(4)


@then("the user gets a 400 error")
def redirected_to_page(base_page):
    assert base_page.get_status_redirect() == 400


@when("the user scroll to see the progress bar")
def user_scroll_in_article_page(base_page):
    base_page.scroll_to_bottom()

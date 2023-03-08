import pytest
from pytest_bdd import when, parsers, then, scenarios

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

scenarios("../features/globals_desktop/header.feature")


@when(parsers.parse("the user clicks on the {submenu}"))
def user_clicks_to_submenu(header, submenu, get_viewport):
    header.click_on_submenu_item(submenu, get_viewport)


@then(parsers.parse("the user is redirected to {keyword}"))
def redirected_to_page(keyword, base_page, driver):
    assert base_page.get_status_redirect() == 200
    assert driver.current_url().__contains__(keyword)


@pytest.mark.flaky(reruns=1, reruns_delay=0.5, reason="requests.exceptions.ConnectionError: ('Connection aborted.',"
                                                      " TimeoutError(60, 'Operation timed out'))")
@then(parsers.parse("every link in the {submenu} selected return an Http 200"))
def check_http_status_internal_links(header, submenu):
    submenu_items = header.get_url_submenu_items(submenu, PageLocators.submenu_items_urls)
    header.check_internal_status(submenu_items)


@when("the user triggers the kebab menu")
def user_trigger_kebab_menu(header):
    header.click_on_kebab_menu()


@when(parsers.parse("the user clicks the {kebab_option}"))
def user_clicks_rss(kebab_option, header, driver):
    header.click_on_kebab_option(kebab_option)


@then(parsers.parse("the dates in RSS and {keyword} matches"))
def confirm_date_format_in_rss(header, feed, keyword):
    publish_date_rss = header.get_publish_date_in_rss()
    date_in_first_article = feed.get_date_first_article_in_feed(keyword)
    assert publish_date_rss == date_in_first_article


@when(parsers.parse("the user clicks on main logo"))
def user_clicks_keyword_logo(header):
    header.click_on_nav_logo()


@then("the system shows the waze header")
def test_header_waze_sitespace(header):
    title_sitespace_in_nav = header.get_site_space_title_in_navigation()
    assert title_sitespace_in_nav == Constants.SITESPACE_WAZE_IN_NAV_MENU


@when(parsers.parse("the user clicks in an article in a {sitespace_tag} in {keyword}"))
def user_clicks_on_random_site_space(sitespace_tag, keyword, feed):
    tags_list = feed.get_eyebrows_in_feed_site_space_page()
    articles_within_sitespace = feed.get_articles_indexes_matching_sitespace_tag(tags_list, sitespace_tag)
    random_index = feed.get_random_index_in_list(articles_within_sitespace)
    feed.click_on_sitespace_element(articles_within_sitespace[random_index], keyword)


@then(parsers.parse("the system shows the {sitespace_title} nav menu in an article"))
def user_sees_nav_sitespace_in_article(sitespace_title, header):
    title_in_sitespace_nav = header.get_site_space_title_in_navigation()
    assert title_in_sitespace_nav == sitespace_title


@when(parsers.parse("the user on {keyword} clicks the CTA See all product updates"))
def click_on_cta_all_product_updates(header, keyword, get_viewport):
    header.click_cta_all_product_updates(keyword, get_viewport)


@then(parsers.parse("the user is redirected to {url}"))
def redirected_to_page(url, base_page, driver):
    assert base_page.get_status_redirect() == 200
    assert driver.current_url().__contains__(url)


@then("every 'see all' CTA selected return an http 200")
def user_clicks_to_see_all_within_company_menu(header, get_viewport):
    header.click_see_all_cta_company_sub_menu(get_viewport)


@then(parsers.parse("the user sees {kebab_option} according to {language}"))
def user_sees_rss_and_press_options(header, kebab_option, language):
    header.confirm_kebab_menu_opts(language, kebab_option)

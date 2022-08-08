import time

import pytest
import requests
from pytest_bdd import scenarios, given, when, then

from tests.consts.constants import Constants

scenarios("../features/press/")


@given("a user is at the <keyword> site")
def at_the_blog(keyword, driver, get_web_browser, get_viewport):
    print('keyword url', Constants.BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    # time.sleep(5)
    driver.start(get_web_browser, get_viewport)
    # time.sleep(5)
    driver.go_to_URL(Constants.BASE_URL + keyword)
    driver.wait_for_page_load()


@when("the user chooses the <type_filter>")
def user_chooses_random_filter(press, type_filter):
    press.get_results_filter_by_type(type_filter)


@when("the user chooses the <product_filter>")
def user_chooses_random_filter(press, product_filter):
    press.get_results_filter_by_product(product_filter)


@when("the user chooses the <topic_filter>")
def user_chooses_random_filter(press, topic_filter):
    press.get_results_filter_by_topic(topic_filter)


@when("the user chooses the <filter_by_type> and <filter_by_product>")
def user_chooses_random_filter(press, filter_by_type, filter_by_product):
    press.get_results_filter_by_type_and_product(filter_by_type, filter_by_product)


@then("the system updates the grid with the <type_filter> in <keyword>")
def results_assets_get_filtered(press, type_filter, keyword):
    actual_titles = press.get_titles_in_press_assets_page()
    print('actual_titles', actual_titles)
    api_url = press.get_api_url_with_type(type_filter, keyword)
    expected_titles = press.get_titles_in_press_asset_api(api_url)
    print('expected_titles', expected_titles)
    download_urls = press.get_assets_download_urls_per_filter_in_press_api(api_url)
    assert expected_titles == actual_titles
    assert press.confirm_download_url_per_assets(download_urls)


@then("the system updates the grid with the <type_filter> and <tag_filter> in <keyword>")
def results_assets_get_filtered(press, type_filter, tag_filter, keyword):
    actual_titles = press.get_titles_in_press_assets_page()
    print('actual_titles', actual_titles)
    api_url = press.get_api_url_with_type_and_tag(type_filter, tag_filter, keyword)
    expected_titles = press.get_titles_in_press_asset_api(api_url)
    print('expected_titles', expected_titles)
    download_urls = press.get_assets_download_urls_per_filter_in_press_api(api_url)
    assert expected_titles == actual_titles
    assert press.confirm_download_url_per_assets(download_urls)

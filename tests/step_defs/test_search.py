import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

# scenarios('../features/search')
scenarios('../features/search_desktop/search_bar.feature')
# scenarios('../features/search/search_global.feature')


@when('the user clicks the search icon')
def user_clicks_search(search):
    search.click_search_icon_in_nav_bar()


@when('the user clicks the magnifying glass')
def user_clicks_magnifying_glass(search):
    search.click_search_icon_in_bar_expanded()


@then('the system shows the search bar expanded')
def search_bar_expanded(search):
    assert search.is_search_bar_visible()


@when('the user closes the search bar')
def user_click_close_icon_search_bar(search):
    search.close_search_bar()


@then('the system collapsed the search bar')
def search_bar_collapsed(search):
    search.is_search_bar_not_visible()
    assert search.is_searchbar_button_visible()


@when(parsers.parse('the user types the {text_to_search}'))
def user_type_criteria_to_search(text_to_search, search):
    search.type_search_criteria(text_to_search)


@then(
    parsers.parse(
        'the system adds the {text_to_search} as a parameter in the {keyword} url'
    )
)
def user_sees_parameter_in_url(text_to_search, keyword, driver):
    url_results_page = (
        Constants.BASE_URL + keyword + Constants.SEARCH_URL + text_to_search
    )
    print('current url:', driver.current_url())
    assert url_results_page == driver.current_url()


@when('the user selects a random filter')
def user_selects_random_filter(search):
    search.click_filter_by_random_option()


@then(parsers.parse('the system filters the results on {keyword}'))
def results_per_filter_by_option(keyword, search, get_viewport):
    assert search.get_results_filtered(keyword, get_viewport)


@then(
    parsers.parse(
        'the system shows suggestions per {text_to_search} in {keyword} page'
    )
)
def correct_suggestions_per_criteria(text_to_search, keyword, search):
    actual_suggestions = search.get_suggested_results_in_page()
    expected_suggestions = search.get_suggested_results_expected(
        keyword, text_to_search
    )
    print('expected_suggestions', expected_suggestions)
    print('actual_suggestions', actual_suggestions)
    assert expected_suggestions == actual_suggestions


# TODO: aleatory tests may fail, because sometimes the results are being shown in different order. bug reported UNI-6189
@then(
    parsers.parse(
        'the system shows results per {text_to_search} in {keyword} page'
    )
)
def correct_search_results_per_criteria(text_to_search, keyword, search):
    assert search.is_search_results_header_visible()
    expected_results = search.get_suggested_results_expected(
        keyword, text_to_search
    )
    actual_results = search.get_search_results_in_page()
    assert len(actual_results) > 0
    assert len(expected_results) > 0
    assert expected_results == actual_results


@then(
    parsers.parse(
        'the system shows msg per {text_to_search} in corresponding {language}'
    )
)
def visibility_of_no_search_results_message(text_to_search, language, search):
    expected_msg = search.get_msg_no_search_results_per_language(
        text_to_search, language
    )
    actual_msg = search.get_msg_no_search_results_in_page()
    assert expected_msg == actual_msg


@given('the progress bar is visible')
def make_progress_bar_visible(homepage, base_page, get_viewport):
    homepage.click_to_read_more_article(get_viewport)
    base_page.scroll_to_fifty_percent()


@given(parsers.parse('the user selects an article in {keyword} feed'))
def user_selects_article_in_feed(keyword, feed, base_page, get_viewport):
    base_page.close_bar(PageLocators.cookie_banner_ok_cta)
    feed.get_random_index_in_list(
        feed.get_articles_in_feed_list(), get_viewport
    )
    feed.click_to_random_article_in_feed(keyword, get_viewport)


@given('the user scroll to see the progress bar')
def user_scroll_in_article_page(base_page):
    base_page.scroll_to_fifty_percent()

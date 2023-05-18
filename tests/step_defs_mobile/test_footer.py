import requests
from pytest_bdd import parsers, scenarios, then, when

scenarios('../features/globals/footer.feature')


@when('the user clicks on legal items')
def click_on_legal_links(footer):
    legal_links = footer.get_legal_links()
    for link in legal_links:
        response = requests.get(legal_links[link])
        assert response.status_code == 200


@then(
    parsers.parse('the user clicks on each URL according to {keyword} locale')
)
def confirm_legal_urls(footer, keyword):
    legal_items_dict = footer.get_legal_links()
    expected_links = footer.get_expected_legal_links_per_locale(keyword)
    assert legal_items_dict == expected_links


@when(parsers.parse('the user clicks on {language} in the selector'))
def user_clicks_on_every_language_in_selector(footer, language):
    footer.click_to_language_in_selector(language)


@then(parsers.parse('the user can see the homepage per {language}'))
def url_per_locale_and_language_selector(footer, language):
    footer.confirm_url_per_language(language)


@when('the user clicks on every social media')
def user_clicks_on_every_social_link(footer):
    assert footer.click_all_social_media_links()


@then('the system opens each link in a new tab')
def each_link_opens_in_a_new_tab(footer):
    assert footer.confirm_links_opened_in_a_new_tab()


@then('the system shows a secure url per each link')
def url_per_social_media_is_secure(footer):
    assert footer.confirm_social_media_url_is_secure()

from pytest_bdd import given, parsers, scenarios, then, when

scenarios('../features/globals/cookiebanner.feature')


@given(parsers.parse('the system displays the cookie banner per {language}'))
def verify_cookie_banner_displayed(cookie_banner, language):
    cookie_banner.clear_local_storage()
    assert (
        cookie_banner.get_cookie_text_per_language(language)
        == cookie_banner.get_cookie_text_in_page()
    )


@when('the user clicks on see details CTA')
def user_clicks_see_details_cta(cookie_banner):
    cookie_banner.click_see_details_cta()


# TODO: facebook urls are not secure (locales: in & au) https://jira.hugeinc.com/browse/UNI-5897
@then(parsers.parse('the user is redirected to {url} in a new tab'))
def redirect_to_url_new_tab(base_page, url):
    actual_url = base_page.get_current_page()
    print('expected url', url, 'actual url', actual_url)
    assert actual_url.__contains__(url)


@given('the user clicks in the Ok cta')
def user_clicks_ok_cookies_msg(cookie_banner):
    cookie_banner.clear_local_storage()
    cookie_banner.close_cookie_banner()


@then('the cookie banner is not displayed')
def cookie_not_displayed(cookie_banner):
    cookie_banner.cookie_not_displayed()

from pytest_bdd import given, when, then, scenarios, parsers

scenarios("../features/globals/cookiebanner.feature")


@given(parsers.parse("the system displays the cookie banner per {language}"))
def verify_cookie_banner_displayed(cookie_banner, language):
    cookie_banner.clear_local_storage()
    assert cookie_banner.get_cookie_text_per_language(language) == cookie_banner.get_cookie_text_in_page()


@when("the user clicks the see details CTA")
def user_clicks_see_details_cta(cookie_banner):
    cookie_banner.click_see_details_cta()


@given("the user clicks in the Ok cta")
def user_clicks_ok_cookies_msg(cookie_banner):
    cookie_banner.clear_local_storage()
    cookie_banner.close_cookie_banner()


@then("the cookie banner is not displayed")
def cookie_not_displayed(cookie_banner):
    cookie_banner.cookie_not_displayed()

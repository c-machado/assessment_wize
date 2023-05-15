# pylint: disable=function-redefined

import time

import pytest
from pytest_bdd import given, scenarios, then, when

from tests.consts.constants import Constants

scenarios('../features/globals_desktop/newsletter.feature')


@pytest.mark.flaky(
    reruns_delay=0.5, reason='Element is not clickable at point (1418, 1166)'
)
@when('the user clicks on subscribe cta')
def user_clicks_subscribe_cta_desktop(header):
    header.close_cookie_banner()
    header.click_on_subscribe_cta()
    time.sleep(1)


@when('the user fills out the form')
def user_fills_out_newsletter_form(newsletter):
    newsletter.enter_email(Constants.NEWSLETTER_EMAIL)


@when('the user submits the information')
def user_submit_form(newsletter):
    newsletter.submit_newsletter_form()


@then('the system displays a confirmation message')
def verify_confirmation_msg(newsletter, base_page):
    message = newsletter.confirm_newsletter_subscription().text
    formatted_message = base_page.remove_enter(message)
    assert Constants.NEWSLETTER_CONFIRMATION == formatted_message


@when('the user fills out the form with invalid data')
def user_fills_out_form_with_invalid_data(newsletter):
    newsletter.enter_email(Constants.NEWSLETTER_INVALID_EMAIL)
    newsletter.submit_newsletter_form()


@then('the user sees an error message')
def newsletter_error_message(newsletter):
    assert (
        newsletter.get_email_message_error()
        == Constants.NEWSLETTER_ERROR_MSG_EMAIL
    )


@when('the user fills out the email in the sticky bar')
def user_fills_out_newsletter_form(newsletter):
    newsletter.enter_email_in_sticky(Constants.NEWSLETTER_EMAIL)


@when('the user submits the information on the sticky')
def user_submit_form(newsletter):
    newsletter.submit_newsletter_sticky_form()


@then('the system displays a confirmation message on the sticky')
def verify_confirmation_msg(newsletter, base_page):
    message = newsletter.confirm_newsletter_sticky_subscription().text
    assert Constants.NEWSLETTER_CONFIRMATION_STICKY == message


@when('the user fills out the email on the sticky with invalid data')
def user_fills_out_form_with_invalid_data(newsletter):
    newsletter.enter_email_in_sticky(Constants.NEWSLETTER_INVALID_EMAIL)
    newsletter.submit_newsletter_sticky_form()


@then('the user sees an error message on sticky')
def newsletter_error_message(newsletter):
    assert (
        newsletter.get_email_message_error_in_sticky()
        == Constants.NEWSLETTER_ERROR_MSG_EMAIL
    )


@given('the toast bar has appeared')
def toast_bar_visible(
    cookie_banner, homepage, newsletter, toast_bar, get_viewport
):
    cookie_banner.close_cookie_banner()
    homepage.click_to_read_more_article(get_viewport)
    toast_bar.make_toast_bar_visible()


@when('the user clicks on subscribe cta in the toast')
def user_clicks_subscribe_cta_toast(footer, header):
    header.click_on_subscribe_cta_toast()


@when('the user closes the toast bar')
def user_closes_toast_bar(toast_bar):
    time.sleep(2)
    toast_bar.close_toast_bar()


@then('the toast bar is not visible anymore')
def toast_bar_not_visible(toast_bar):
    assert toast_bar.is_toast_bar_visible()


@then('the system displays a confirmation message on the homepage')
def verify_confirmation_msg(newsletter, base_page):
    message = newsletter.confirm_newsletter_homepage_subscription().text
    formatted_message = base_page.remove_enter(message)
    assert Constants.NEWSLETTER_CONFIRMATION == formatted_message

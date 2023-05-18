import pytest
import requests
from pytest_bdd import given, parsers, scenarios, then, when

from tests.consts.constants import Constants
from tests.pages.locators import PageLocators

# scenarios("../features/globals/")

# @when("the user clicks on every <social_media> item")
# def click_on_social_item(footer, cookie_banner, social_media):
#     footer.go_to_footer()
#     cookie_banner.close_cookie_banner()
#     footer.click_social_media_item(social_media)
#
#
# @when("the user clicks on every language in the selector")
# def user_clicks_on_every_language_in_selector(footer):
#     footer.go_to_footer()
#     footer.click_to_each_language_in_selector()
#
#
# @then("the user can see all expected locales in the selector")
# def confirm_language_options(footer):
#     assert set(footer.languages) == set(Constants.LANGUAGE_SELECTOR)
#
#
# # @given("the user clicks on the hero article")
# # def user_clicks_hero_article(cookie_banner, get_viewport):
# #     cookie_banner.click_to_read_more_article(get_viewport)
#
#
# @when("the user closes the modal")
# def user_clicks_to_close_newsletter_modal(newsletter):
#     newsletter.close_newsletter_modal()
#
#
# @then("the system hides the modal")
# def newsletter_modal_not_visible(newsletter):
#     newsletter.modal_not_visible()
#
#
# @given("the user closes the cookie banner")
# def user_closes_cookie_banner(cookie_banner):
#     cookie_banner.close_cookie_banner()
#
#
# @given("a user navigates to <url_from>")
# def user_navigate_to_previous_redirect(url_from, driver):
#     time.sleep(2)
#     driver.go_to_URL(Constants.BASE_URL + url_from)
#     time.sleep(2)
#
#
# @then("the user gets a 400 error")
# def redirected_to_page(base_page):
#     assert base_page.get_status_redirect() == 400

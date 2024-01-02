import pytest

from pytest_bdd import given, scenarios, when, then
from tests.consts.constants import Constants

scenarios("../features/shopping_wizeline.feature")


@given("a user is at the homepage")
def at_the_homepage(driver, get_web_browser, get_viewport):
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL)


@given("the user is logged in")
def user_logging(login_page, driver):
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_to_login()
    assert driver.current_url() == Constants.BASE_URL + 'inventory.html'


@when("the user clicks on the CTA to add an item")
def add_an_item_to_cart(home_sauce):
    home_sauce.add_an_item_to_cart()


@then("the system adds the item to the cart")
def item_added_to_the_cart(home_sauce):
    assert home_sauce.is_remove_btn_visible()


@then("the user navigates to the cart")
def navigates_to_the_cart(driver):
    driver.go_to_URL(Constants.BASE_URL + 'cart.html')


@then("the user confirms the correct item is added")
def confirm_item_in_the_cart(cart_sauce):
    assert cart_sauce.confirm_item_title() == Constants.TITLE
    assert cart_sauce.confirm_item_description() == Constants. DESCRIPTION
    assert cart_sauce.confirm_quantity() == Constants.QUANTITY



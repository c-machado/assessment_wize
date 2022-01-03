import time

import pytest
import requests
# from pytest_bdd import scenarios, given, when, then
#
# from tests.consts.constants import Constants
#
# scenarios("../features/globals/header.feature")
#
# BASE_URL = 'https://blog.google'
# # BASE_URL = 'https://gweb-uniblog-publish-stage.appspot.com/supportingnews'
# # BASE_URL = 'https://www.google.com/'
#
#
# @given("a user is at the <keyword> site")
# def at_the_blog(keyword, driver, get_web_browser, get_viewport):
#     print('keyword url', BASE_URL + keyword)
#     print('get_web_browser', get_web_browser)
#     print('get_viewport', get_viewport)
#     driver.start(get_web_browser, get_viewport)
#     driver.go_to_URL(Constants.BASE_URL + keyword)
#     # browser.set_cookie()
#     # browser.refresh()
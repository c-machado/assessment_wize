import time

from pytest_bdd import scenarios, given, when, then

from tests.consts.constants import Constants


scenarios("../features/article/")


@given("a user is at the <keyword> site")
def at_the_blog(keyword, driver, get_web_browser, get_viewport):
    print('keyword url', Constants.BASE_URL + keyword)
    print('get_web_browser', get_web_browser)
    print('get_viewport', get_viewport)
    driver.start(get_web_browser, get_viewport)
    driver.go_to_URL(Constants.BASE_URL + keyword)
    driver.wait_for_page_load()


@then("we test the code in the example <keyword>")
def test_tagging(keyword, article):
    article.test(keyword)


@given("the user clicks to play the <video_type>")
def user_play_video(article, video_type):
    article.close_cookie_banner()
    article.click_to_play_video(video_type)


@then("the user can interact with the video controls")
def user_pause_video(article):
    article.switch_to_video_context()
    article.click_to_mute_video()
    assert article.get_current_time_video() > 0
    article.click_to_pause_video()


@then("all links are marked with the target property accordingly")
def validate_internal_links(article):
    assert article.validate_inline_links_in_article() == 0


@then("all links redirects to an existing page")
def redirect_to_an_existing_page(article):
    article.confirm_internal_status()


@when("the user scrolls to the related stories section")
def user_scroll_related_articles_section(article):
    article.close_cookie_banner()
    article.scroll_to_bottom()


@then("the user sees articles matching tags in current article")
def user_sees_articles_matching_current_tag(article):
    article.validate_tags_in_related_stories()

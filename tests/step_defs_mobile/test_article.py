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


@given("the user clicks to play the <video_type>")
def user_play_video(article, video_type):
    article.close_cookie_banner()
    article.click_to_play_video(video_type)


@then("the user can interact with the video controls")
# TODO: Adding test according to Will proposal https://jira.hugeinc.com/browse/UNI-6187
def user_interacting_with_video(article):
    article.click_to_mute_video()
    assert article.get_current_time_video() > 0
    article.click_to_pause_video()


@then("all links are marked with the target property accordingly")
def validate_internal_links(article):
    assert article.validate_inline_links_in_article()


@then("all links redirects to an existing page")
def redirect_to_an_existing_page(article):
    article.confirm_internal_status()


@when("the user scrolls to the related stories section")
def user_scroll_related_articles_section(article):
    article.close_cookie_banner()
    article.scroll_to_bottom()


@then("the user sees articles matching tags in current article")
def user_sees_articles_matching_current_tag(article):
    assert article.validate_tags_in_related_stories()


@then("the date shown in the related stories articles are according to the <locale> format")
def date_format_in_related_stories(article, base_page, locale):
    time.sleep(1)
    date_in_article_list = article.get_date_in_related_articles()
    date_format_expected = article.get_date_format_per_locale(locale, Constants.DATE_FORMAT_PER_LOCALE)
    for date_in_article in date_in_article_list:
        assert base_page.is_date_format_correct(date_in_article, date_format_expected, locale)


@given("the user chooses a random article")
def user_choose_random_article(feed, article):
    article.close_cookie_banner()
    article_feed_list = feed.get_articles_in_feed_list()
    feed.get_random_index_in_list(article_feed_list)


@when("the user opens the selected random article in <keyword> feed")
def user_open_random_article_in_feed(feed, keyword):
    feed.click_to_random_article_in_feed(keyword)

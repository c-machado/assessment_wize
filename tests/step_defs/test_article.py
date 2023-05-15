import time

from pytest_bdd import given, parsers, scenarios, then, when

from tests.consts.constants import Constants

scenarios(
    '../features/article/article_inline_links.feature',
    '../features/article/article_related_articles.feature',
    '../features/article/article_related_stories_date_format.feature',
    '../features/article/article_videos.feature',
)


@given(parsers.parse('the user clicks to play the {video_type}'))
def user_play_video(article, video_type):
    article.close_cookie_banner()
    article.click_to_play_video(video_type)


@then('the user can interact with the video controls')
# TODO: Adding test according to Will proposal https://jira.hugeinc.com/browse/UNI-6187
def user_interacting_with_video(article):
    article.click_to_mute_video()
    assert article.get_current_time_video() > 0
    article.click_to_pause_video()


@then('all links are marked with the target property accordingly')
def validate_internal_links(article):
    assert article.validate_inline_links_in_article()


@then('all links redirects to an existing page')
def redirect_to_an_existing_page(article):
    article.confirm_internal_status()


@when('the user scrolls to the related stories section')
def user_scroll_related_articles_section(article):
    article.close_cookie_banner()
    article.scroll_to_bottom()


@then('the user sees articles matching tags in current article')
def user_sees_articles_matching_current_tag(article):
    assert article.validate_tags_in_related_stories()


@then(
    parsers.parse(
        'the date shown in the related stories articles are according to the {locale} format'
    )
)
def date_format_in_related_stories(article, feed, base_page, locale):
    time.sleep(1)
    date_in_article_list = article.get_list_dates_in_related_articles()
    for date_in_article in date_in_article_list:
        date_format_expected = (
            article.get_date_in_related_article_in_babel_format(
                feed, date_in_article, locale
            )
        )
        print('date_format_expected', date_format_expected)
        print('date_article', date_in_article)
        assert date_in_article == date_format_expected

from selenium.webdriver.common.by import By


class PageLocators:
    article_current_time = (By.CSS_SELECTOR, '.ytp-time-current')
    article_inline_links = (By.CSS_SELECTOR, '.uni-blog-article-container a')
    article_mute_video = (By.CSS_SELECTOR, 'span .ytp-mute-button')
    article_pause_video = (By.CSS_SELECTOR, '.ytp-play-button')
    article_play_hero_video = (By.CSS_SELECTOR, '.uni-article-video--hero')
    article_play_embed_video = (By.CSS_SELECTOR, '.uni-article-video--body')
    article_primary_tag = (By.CSS_SELECTOR, '.article-hero__primary-tag')
    article_published_at = (By.CSS_SELECTOR, '.article-meta__published-at')
    article_read_more_mobile_no_additional = (
        By.CSS_SELECTOR,
        "section[data-component='uni-featured-article']",
    )
    # article_read_more_mobile = (By.CSS_SELECTOR, ".featured-article__image--full-width.uni-click-tracker:nth-child(1)")
    article_read_more_mobile = (
        By.CSS_SELECTOR,
        '.featured-article__image--full-width',
    )
    article_read_more_cta = (By.CSS_SELECTOR, 'a.featured-article__link')
    article_related_stories_category_tags = (
        By.CSS_SELECTOR,
        '.uni-related-articles-cards__category',
    )
    article_related_stories_cards = (
        By.CSS_SELECTOR,
        '.uni-related-articles-cards__link',
    )
    article_related_stories_published_at = (
        By.CSS_SELECTOR,
        '.uni-related-articles-cards__date',
    )
    article_secondary_tags = (By.CSS_SELECTOR, '.uni-blog-article-tags-value')
    article_see_subtitles = (By.CSS_SELECTOR, '.ytp-subtitles-button')
    article_video_hero_frame = (
        By.CSS_SELECTOR,
        '.uni-article-video--hero > div> iframe',
    )
    article_video_body_frame = (
        By.CSS_SELECTOR,
        '.uni-article-video--body > div> iframe',
    )
    collection_data_analytics = (By.CSS_SELECTOR, '.page-analytics-data')
    cookie_banner_ok_cta = (By.CSS_SELECTOR, '.cookieBarConsentButton')
    cookie_banner_bar = (By.ID, 'cookieBar')
    cookie_see_details_cta = (By.CSS_SELECTOR, '.cookieBarMoreButton')
    feed_articles_list = (By.CSS_SELECTOR, '.feed-article.ng-scope')
    feed_articles_list_top = (
        By.CSS_SELECTOR,
        '.feed-article.ng-scope:nth-child(1)',
    )
    feed_articles_list_scroll_to = (
        By.CSS_SELECTOR,
        '.feed-article.ng-scope:nth-child(index_to_scroll)',
    )
    feed_articles_category_horizontal_top = (
        By.CSS_SELECTOR,
        '.feed-article.ng-scope:nth-child(2)',
    )
    feed_articles_category_horizontal_scroll_to = (
        By.CSS_SELECTOR,
        '.feed-article.ng-scope:nth-child(index_to_scroll)',
    )
    feed_article_dates_list = (
        By.CSS_SELECTOR,
        '.feed-article.ng-scope .eyebrow__date time',
    )
    feed_article_titles_list = (By.CSS_SELECTOR, '.feed-article__title')
    feed_load_more = (By.CSS_SELECTOR, '.article-list__load-more--cards')
    feed_load_more_text = (By.CSS_SELECTOR, '.article-list__loader-text')
    footer_google_logo = (By.CSS_SELECTOR, '.h-c-footer__logo')
    hamburger_menu = (By.CSS_SELECTOR, '.uni-header__hamburguer-button')
    hamburger_menu_rss = (
        By.CSS_SELECTOR,
        'ul.uni-header__kebab-menu--mobile > li:nth-child(2) > a',
    )
    kebab_toggle = (By.CSS_SELECTOR, '.uni-header__kebab-toggle')
    kebab__options_locators = {
        'rss': (
            By.CSS_SELECTOR,
            'div.uni-header__kebab > ul > li:nth-child(2) > a',
        ),
        'press': (
            By.CSS_SELECTOR,
            'div.uni-header__kebab > ul > li:nth-child(1) > a',
        ),
    }
    language_selector = (By.NAME, 'language')
    language_selector_options = (
        By.CSS_SELECTOR,
        "select[name='language'] > option",
    )
    legal_links_list = (By.CSS_SELECTOR, '.h-c-footer__link')
    menu_keyword_logo = (By.CSS_SELECTOR, '.uni-header__site-title')
    menu_all_product_updates_cta_desktop = (
        By.CSS_SELECTOR,
        '.uni-main-menu__submenu-view-all-link',
    )
    menu_all_product_updates_cta_mobile = (
        By.CSS_SELECTOR,
        '.uni-main-menu__subnav--mobile > a',
    )
    menu_hidden = (By.CSS_SELECTOR, '.uni-header.h-u-box-shadow-2')
    menu_subscribe_cta = (By.CSS_SELECTOR, '.uni-header__newsletter--desktop')
    menu_subscribe_mobile_cta_sticky = (
        By.CSS_SELECTOR,
        '.sticky-form__mobile-cta >button',
    )
    menu_subscribe_mobile_hamburger_cta = (
        By.CSS_SELECTOR,
        '.uni-navigation--mobile .uni-header__newsletter--cta--mobile',
    )
    newsletter_close_icon = (
        By.CSS_SELECTOR,
        '.uni-subscribe-modal__icon-close-container',
    )
    newsletter_email_field = (
        By.CSS_SELECTOR,
        '.newsletter-form:not(.sticky) .uni_subscribe_email',
    )
    newsletter_sticky_email_field = (
        By.CSS_SELECTOR,
        '.newsletter-form.sticky .uni_subscribe_email',
    )
    newsletter_error_email = (
        By.CSS_SELECTOR,
        '.newsletter-form:not(.sticky) .uni_subscribe_email--error',
    )
    newsletter_sticky_error_email = (
        By.CSS_SELECTOR,
        '.newsletter-form.sticky .uni_subscribe_email--error',
    )
    newsletter_modal = (By.CSS_SELECTOR, '.uni-subscribe-modal__body')
    newsletter_success_modal = (By.ID, 'newsletter-form--success')
    newsletter_subscribe_cta = (
        By.CSS_SELECTOR,
        '.newsletter-form:not(.sticky) .newsletter-form__submit',
    )
    newsletter_sticky_subscribe_cta = (
        By.CSS_SELECTOR,
        '.newsletter-form.sticky .newsletter-form__submit',
    )
    # newsletter_subscribed_msg = (By.CSS_SELECTOR, ".newsletter-form__success-text p#subscribe_box_success_label")
    newsletter_subscribed_msg = (
        By.CSS_SELECTOR,
        '.newsletter-form:not(.sticky) #subscribe_box_success_label',
    )
    newsletter_sticky_subscribed_msg = (
        By.CSS_SELECTOR,
        '.newsletter-form.sticky #subscribe_box_success_label',
    )
    newsletter_homepage_subscribed_msg = (
        By.CSS_SELECTOR,
        '.newsletter-form:not(.sticky) #subscribe_success_label',
    )
    press_titles_in_page = (By.CSS_SELECTOR, '.press-item__title')
    press_filter_by_type = (
        By.CSS_SELECTOR,
        '.uni-search-results-filters>div:nth-child(2)>div>select',
    )
    press_filter_by_topic = (
        By.CSS_SELECTOR,
        '.uni-search-results-filters>div:nth-child(4)>div>select',
    )
    press_filter_by_product = (
        By.CSS_SELECTOR,
        '.uni-search-results-filters>div:nth-child(3)>div>select',
    )
    press_number_of_results = (By.CSS_SELECTOR, '.uni-search-results-counter')
    search_bar_text_field = (By.CSS_SELECTOR, 'input.uni-search__input')
    search_close_icon_desktop = (
        By.CSS_SELECTOR,
        'button.uni-search__button.uni-search__button-close',
    )
    search_eyebrow_articles_in_feed = (
        By.CSS_SELECTOR,
        '.feed-article__eyebrow',
    )
    search_filter_by = (
        By.CSS_SELECTOR,
        '.uni-search-results__select select > option',
    )
    search_icon_nav_desktop = (By.CSS_SELECTOR, '.uni-header__kebab-search')
    search_icon_nav_expanded = (
        By.CSS_SELECTOR,
        '.uni-search__button.uni-search__button-search',
    )
    search_tag_filter_selected = (
        By.CSS_SELECTOR,
        '.uni-search-results__selected-facets',
    )
    search_results_list = (By.CSS_SELECTOR, '.feed-article__title.ng-binding')
    search_no_results_header = (By.CSS_SELECTOR, '.h-c-page > h3')
    search_results_header = (By.CSS_SELECTOR, '.uni-search-results__header h1')
    search_suggestions_results_list = (
        By.CSS_SELECTOR,
        '.uni-search__auto-complete-title',
    )
    site_spaces_in_ads_and_analytics = (
        By.CSS_SELECTOR,
        '.all-products-list__category:nth-child(7) > a',
    )
    site_space_title_in_nav_menu = (
        By.CSS_SELECTOR,
        '.uni-header__sitespace-text',
    )
    social_media_list = (By.CSS_SELECTOR, '.h-c-social__link.uni-click-tracker')
    social_media_locators = {
        'instagram': (
            By.XPATH,
            "//*[starts-with(@href, 'https://www.instagram.com')]",
        ),
        'twitter': (
            By.XPATH,
            "//a[@class='h-c-social__link uni-click-tracker' and starts-with"
            "(@href, 'https://twitter.com')]",
        ),
        'youtube': (
            By.XPATH,
            "//*[starts-with(@href, 'https://www.youtube.com')]",
        ),
        'facebook': (
            By.XPATH,
            "//a[@class='h-c-social__link uni-click-tracker' and "
            "starts-with(@href, 'https://www.facebook.com')]",
        ),
        'linkedin': (
            By.XPATH,
            "//a[@class='h-c-social__link uni-click-tracker' and "
            "starts-with(@href, 'https://www.linkedin.com')]",
        ),
    }
    submenu_company_news_see_all_ctas = (
        By.CSS_SELECTOR,
        '.uni-main-menu__submenu-item-see-all',
    )
    submenu_company_news_see_all_ctas_mobile = (
        By.CSS_SELECTOR,
        'li.uni-main-menu__item--mobile:nth-child(3) > div > ul >li >ul >li:last-child >a',
    )
    submenu_items_urls = {
        'product_updates': (
            By.XPATH,
            "//a[@data-navigation='Product-updates']"
            "[@class='uni-main-menu__submenu-anchor']",
        ),
        'company_news': (
            By.XPATH,
            "//a[@data-navigation='Company-news'][@class='uni-main-menu__submenu-anchor']",
        ),
    }
    submenu_locators_desktop = {
        'latest_stories': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--desktop:nth-child(1)',
        ),
        'product_updates': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--desktop:nth-child(2)',
        ),
        'company_news': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--desktop:nth-child(3)',
        ),
    }
    submenu_locators_mobile = {
        'latest_stories': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--mobile:nth-child(1)',
        ),
        'product_updates': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--mobile:nth-child(2)',
        ),
        'company_news': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--mobile:nth-child(3)',
        ),
    }
    submenu_items_mobile = {
        'product_updates': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--mobile:nth-child(2) > div > ul >li',
        ),
        'company_news': (
            By.CSS_SELECTOR,
            'li.uni-main-menu__item--mobile:nth-child(3) > div > ul >li',
        ),
    }
    toast_bar = (By.CSS_SELECTOR, '.uni-newsletter-toast--container')
    toast_bar_subscribe_cta = (
        By.CSS_SELECTOR,
        '.uni-newsletter-toast__cta--sub',
    )
    toast_bar_close_cta = (
        By.CSS_SELECTOR,
        '.uni-newsletter-toast__buttons > button:nth-child(2)',
    )

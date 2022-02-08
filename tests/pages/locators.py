from selenium.webdriver.common.by import By


class PageLocators(object):

    article_read_more_cta = (By.CSS_SELECTOR, "a.featured-article__link span.cta")
    article_secondary_tags = (By.CSS_SELECTOR, ".uni-blog-article-tags-value")
    article_published_at = (By.CSS_SELECTOR, ".article-meta__published-at")
    cookie_banner_ok_cta = (By.CSS_SELECTOR, ".cookieBarConsentButton")
    cookie_banner_bar = (By.ID, "cookieBar")
    cookie_see_details_cta = (By.CSS_SELECTOR, ".cookieBarMoreButton")
    feed_articles_list = (By.CSS_SELECTOR, ".feed-article.ng-scope")
    feed_articles_list_top = (By.CSS_SELECTOR, ".feed-article.ng-scope:nth-child(1)")
    feed_articles_category_horizontal_top = (By.CSS_SELECTOR, ".feed-article.ng-scope:nth-child(2)")
    feed_article_dates_list = (By.CSS_SELECTOR, ".feed-article__content .uni-timesince")
    feed_article_titles_list = (By.CSS_SELECTOR, ".feed-article__title")
    feed_load_more = (By.CSS_SELECTOR, ".article-list__load-more")
    footer_google_logo = (By.CSS_SELECTOR, ".h-c-footer__logo")
    hamburger_menu = (By.CSS_SELECTOR, ".uni-header__hamburguer-button")
    hamburger_menu_rss = (By.CSS_SELECTOR, "ul.uni-header__kebab-menu--mobile > li:nth-child(2) > a")
    kebab_toggle = (By.CSS_SELECTOR, '.uni-header__kebab-toggle')
    kebab__options_locators = {
        "rss": (By.CSS_SELECTOR, 'div.uni-header__kebab > ul > li:nth-child(2) > a'),
        "press": (By.CSS_SELECTOR, 'div.uni-header__kebab > ul > li:nth-child(1) > a')
    }
    language_selector = (By.NAME, "language")
    language_selector_options = (By.CSS_SELECTOR, "select[name='language'] > option")
    legal_links_list = (By.CSS_SELECTOR, ".h-c-footer__link")
    menu_keyword_logo = (By.CSS_SELECTOR, ".uni-header__site-title")
    menu_all_product_updates_cta = (By.CSS_SELECTOR, ".uni-main-menu__submenu-view-all-link")
    menu_hidden = (By.CSS_SELECTOR, ".uni-header.h-u-box-shadow-2")
    menu_subscribe_cta = (By.CSS_SELECTOR, "div[data-component='uni-cta-newsletter'].uni-header__newsletter--desktop")
    newsletter_close_icon = (By.CSS_SELECTOR, ".uni-subscribe-modal__icon-close-container")
    newsletter_first_name_field = (By.ID, "uni-subscribe-first-name")
    newsletter_email_field = (By.ID, "uni-subscribe-email")
    newsletter_error_first_name = (By.ID, "uni-subscribe-first-name--error")
    newsletter_error_email = (By.ID, "uni-subscribe-email--error")
    newsletter_modal = (By.CSS_SELECTOR, ".uni-subscribe-modal__body")
    newsletter_success_modal = (By.CSS_SELECTOR, "[data-slide='success']")
    newsletter_subscribe_cta = (By.CSS_SELECTOR, ".uni-subscribe-modal__submit")
    newsletter_subscribed_msg = (By.ID, "subscribe_success_label")
    search_button_desktop = (By.CSS_SELECTOR, '.uni-header__kebab-search')
    search_button_bar_expanded = (By.CSS_SELECTOR, '.uni-search__button.uni-search__button-search')
    search_bar_text_field = (By.CSS_SELECTOR, 'input.uni-search__input')
    search_close_icon_desktop = (By.CSS_SELECTOR, 'button.uni-search__button.uni-search__button-close')
    search_eyebrow_articles_in_feed = (By.CSS_SELECTOR, '.feed-article__eyebrow')
    search_tag_filter_selected = (By.CSS_SELECTOR, ".uni-search-results__selected-facets")
    search_filter_by = (By.CSS_SELECTOR, '.uni-search-results__select select > option')
    social_media_list = (By.CSS_SELECTOR, ".h-c-social__link.uni-click-tracker")
    social_media_locators = {
        "instagram": (By.XPATH, "//*[starts-with(@href, 'https://www.instagram.com')]"),
        "twitter": (By.XPATH, "//a[@class='h-c-social__link uni-click-tracker' and starts-with"
                              "(@href, 'https://twitter.com')]"),
        "youtube": (By.XPATH, "//*[starts-with(@href, 'https://www.youtube.com')]"),
        "facebook": (By.XPATH, "//a[@class='h-c-social__link uni-click-tracker' and "
                               "starts-with(@href, 'https://www.facebook.com')]"),
        "linkedin": (By.XPATH, "//a[@class='h-c-social__link uni-click-tracker' and "
                               "starts-with(@href, 'https://www.linkedin.com')]")
    }
    submenu_company_news_see_all_ctas = (By.CSS_SELECTOR, ".uni-main-menu__submenu-item-see-all")
    submenu_items_locators = {
        "product_updates": (By.XPATH, "//a[@data-navigation='Product-updates']"
                                      "[@class=' uni-main-menu__submenu-anchor']"),
        "company_news": (By.XPATH, "//a[@data-navigation='Company-news'][@class=' uni-main-menu__submenu-anchor']")
    }
    submenu_locators = {
        "product_updates": (By.CSS_SELECTOR, "#uni-main-menu > li:nth-child(2)"),
        "company_news": (By.CSS_SELECTOR, "#uni-main-menu > li:nth-child(3)")
    }
    toast_bar = (By.CSS_SELECTOR, ".uni-newsletter-toast--container")
    toast_bar_subscribe_cta = (By.CSS_SELECTOR, ".uni-newsletter-toast__cta--sub")
    toast_bar_close_cta = (By.CSS_SELECTOR, ".uni-newsletter-toast__buttons > button:nth-child(2)")
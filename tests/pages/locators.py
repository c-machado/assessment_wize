from selenium.webdriver.common.by import By


class PageLocators(object):

    overview = (By.CSS_SELECTOR, "[data-section='overview']")
    cookie_banner = (By.CSS_SELECTOR, ".cookieBarConsentButton")
    kebab_toggle = (By.CSS_SELECTOR, '.uni-header__kebab-toggle')
    kebab__options_locators = {
        "rss": (By.CSS_SELECTOR, 'div.uni-header__kebab > ul > li:nth-child(2) > a'),
        "press": (By.CSS_SELECTOR, 'div.uni-header__kebab > ul > li:nth-child(1) > a')
    }
    legal_links_list = (By.CSS_SELECTOR, ".h-c-footer__link")
    menu_cta_all_product_updates = (By.CSS_SELECTOR, ".uni-main-menu__submenu-view-all-link")
    social_media_list = (By.CSS_SELECTOR, ".h-c-social__link.uni-click-tracker")
    social_media_locators = {
        "instagram": (By.XPATH, "//*[starts-with(@href, 'https://www.instagram.com')]"),
        "twitter": (By.XPATH, "//a[@class='h-c-social__link uni-click-tracker' and starts-with"
                              "(@href, 'https://twitter.com')]"),
        "youtube": (By.XPATH, "//*[starts-with(@href, 'https://www.youtube.com')]"),
        "facebook": (By.XPATH, "//*[starts-with(@href, 'https://www.facebook.com')]"),
        "linkedin": (By.XPATH, "//*[starts-with(@href, 'https://www.linkedin.com')]")
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
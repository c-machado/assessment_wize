from selenium.webdriver.common.by import By


class PageLocators(object):

    # chrome_url = "https://www.google.com/"
    # chrome_url = "https://chromatica-dot-googwebreview.appspot.com"

    overview = (By.CSS_SELECTOR, "[data-section='overview']")
    ############old
    accept_tos = (By.ID, "js-accept-install")
    accept_installer = {
        "WIN": (By.ID, "js-accept-install--win"),
        "MAC": (By.ID, "js-accept-install--mac"),
        "LIN": (By.ID, "js-accept-install--linux")
    }
    additional_tos_popup = (By.CSS_SELECTOR, ".js-simplified-legal-links a:nth-of-type(2)")
    # arm_chip = (By.ID, "js-accept-install--mac_arm")
    anywhere_page_link = (By.CSS_SELECTOR, "a[href='/chrome/anywhere/']")
    android_page = (By.XPATH, "//a[contains(@href,'play.google.com')]")
    built_in_page_link = (By.CSS_SELECTOR, "a[href='/chrome/googlebuiltin/']")
    cookie_banner_cta = (By.CSS_SELECTOR, ".chr-cookie-banner__button button")
    cookie_banner = (By.ID, "js-cookie-banner")
    close_cookie_cta = (By.CSS_SELECTOR, "button[ga-event-label='cookie:ok-got-it']")
    deprecated_msg_dev_mac49 = (By.ID, "hero-u-d-channel-mac49-dev")
    download_again = (By.ID, "js-download-fallback")
    download_cta_hero = (By.ID, "js-download-hero")
    download_cta_bottom = (By.ID, "js-download-now")
    download_cta_nav = (By.CSS_SELECTOR, ".cta-container button")
    eula_modal = (By.ID, "js-chrome-os-modal")
    eula_default_checkbox = (By.ID, "js-default-cb")
    eula_help_checkbox = (By.ID, "js-stats-cb")
    google_settings_cookie_link = (By.CSS_SELECTOR, "a[ga-event-label='cookie:google-settings']")
    installer_version = {
        "intel": (By.ID, "js-accept-install--mac"),
        "arm": (By.ID, "js-accept-install--mac_arm"),
        "debian": (By.ID, "js-linux-ubuntu"),
        "fedora": (By.ID, "js-linux-fedora")
    }
    language_selector = (By.ID, "language-selector")
    learn_more_cookie_link = (By.CSS_SELECTOR, "a[ga-event-label='cookie:learn-more']")
    link_locators = {
        "learn-more":  (By.ID, "js-chrome-os-update"),
        "supported":  (By.ID, "js-chrome-os-other"),
        "chrome_os_not_supported":  (By.CSS_SELECTOR, "div[id='js-chrome-os-modal'] a"),
        "here":  (By.ID, "js-linux-community"),
    }
    nav_menu = (By.ID, "js-header")
    nav_menu_class_hidden = (By.CLASS_NAME, "cta--hidden")
    other_platforms_win32 = (By.ID, "js-other-win")
    other_platforms_win64 = (By.ID, "js-other-win64")
    other_platforms_mac = (By.ID, "js-other-mac")
    other_platforms_linux = (By.ID, "js-other-linux")
    other_platforms_win_xp = (By.ID, "js-other-xp")
    other_platforms_win_vista = (By.ID, "js-other-vista")
    other_platforms_mac49 = (By.ID, "js-other-mac49")
    other_platforms_mac65 = (By.ID, "js-other-mac65")
    other_platforms_mac88 = (By.ID, "js-other-mac88")
    other_platforms_android = (By.ID, "js-other-android")
    other_platforms_ios = (By.ID, "js-other-ios")
    other_platforms_link = (By.ID, "js-other-platform")
    platforms_ids_locators = {
        "js-other-win": (By.ID, "js-other-win"),
        "js-other-win64": (By.ID, "js-other-win64"),
        "js-other-mac": (By.ID, "js-other-mac"),
        "js-other-linux": (By.ID, "js-other-linux"),
        "js-other-xp": (By.ID, "js-other-xp"),
        "js-other-vista": (By.ID, "js-other-vista"),
        "js-other-mac49": (By.ID, "js-other-mac49"),
        "js-other-mac65": (By.ID, "js-other-mac65"),
        "js-other-mac88": (By.ID, "js-other-mac88")
    }
    platforms_labels_to_ids = {
        "windows-7-to-10-32-bit": "js-other-win",
        "windows-7-to-10-64-bit": "js-other-win64",
        "mac-10-10-later": "js-other-mac",
        "linux": "js-other-linux",
        "windows-xp": "js-other-xp",
        "windows-vista": "js-other-vista",
        "mac-10-6-to-10-8": "js-other-mac49",
        "mac-10-9": "js-other-mac65",
        "mac-10-10": "js-other-mac88"
    }

    privacy_link_hero = (By.ID, "js-privacy-link")
    privacy_page_link = (By.CSS_SELECTOR, "a[href='/chrome/privacy/']")
    productivity_page_link = (By.CSS_SELECTOR, "a[href='/chrome/productivity/']")
    retry_link_win = (By.ID, "js-download-again")
    retry_link_other = (By.ID, "js-download-fallback")
    retry_link = {
        "MAC": (By.ID, "js-download-fallback"),
        # "WIN": (By.ID, "js-download-fallback")
        # This only applies to win stable, and is going to be updated on 9/16 with the l10n release
        "WIN": (By.ID, "js-download-again"),
        "LIN": (By.ID, "js-download-fallback")
    }
    security_page_link = (By.CSS_SELECTOR, "a[href='/chrome/security/']")
    tos_link_hero = (By.ID, "js-tos-link")
    tos_link_popup = (By.CSS_SELECTOR, ".js-simplified-legal-links a:nth-of-type(1)")
    get_stable_installer = {
        "MAC49dev": (By.XPATH, "//*[contains(@id, 'js-get-stable-dev-mac49-hero')]"),
        "MAC65dev": (By.XPATH, "//*[contains(@id, 'js-get-stable-dev-mac49-hero')]"),
        "MAC49beta": (By.ID, "js-get-stable-beta-mac49-hero"),
        "MAC65beta": (By.ID, "js-get-stable-beta-mac65-hero"),
        "MAC49canary": (By.ID, "js-get-stable-canary-mac49-hero"),
        "MAC65canary": (By.ID, "js-get-stable-canary-mac65-hero"),
        "WINXPbeta": (By.ID, "js-get-stable-beta-win49-hero"),
        "WINXPcanary": (By.ID, "js-get-stable-canary-win49-hero"),
        "WINXPdev": (By.ID, "js-get-stable-dev-win49-hero"),
        "LINUXcanary": (By.ID, "js-get-stable-canary-linux-hero")

    }
    unsupported_hero = {
        "MAC49dev": (By.ID, "hero-u-d-channel-mac49-dev"),
        "MAC65dev": (By.ID, "hero-u-d-channel-mac65-dev"),
        "MAC88dev": (By.ID, "hero-u-d-channel-mac88-dev"),
        "MAC49beta": (By.ID, "hero-u-d-channel-mac49-beta"),
        "MAC65beta": (By.ID, "hero-u-d-channel-mac65-beta"),
        "MAC88beta": (By.ID, "hero-u-d-channel-mac88-beta"),
        "MAC49canary": (By.ID, "hero-u-d-channel-mac49-canary"),
        "MAC65canary": (By.ID, "hero-u-d-channel-mac65-canary"),
        "MAC88canary": (By.ID, "hero-u-d-channel-mac88-canary"),
        "WINXPbeta": (By.ID, "hero-u-d-channel-win49-beta"),
        "WINXPcanary": (By.ID, "hero-u-d-channel-win49-canary"),
        "WINXPdev": (By.ID, "hero-u-d-channel-win49-dev"),
        "LINUXcanary": (By.ID, "hero-u-d-channel-linux-canary")
    }

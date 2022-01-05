class Constants(object):
    BASE_URL = 'https://blog.google'
    # BASE_URL = 'https://gweb-uniblog-publish-stage.appspot.com/supportingnews'

    COOKIE_BANNER_TXT = {
        "en": "Google serves cookies to analyze traffic to this site. Information about your use of our site is "
              "shared with Google for that purpose.",
        "de": "Google verwendet Cookies, um Zugriffe auf diese Website zu analysieren. " 
              "Informationen zu deiner Nutzung dieser Website werden deshalb mit Google geteilt."
    }

    CHROME_WINDOWS_SIZE = {
        "mobile": "window-size=414,896",
        "tablet": "window-size=600,800",
        "desktop": "window-size=1920,1080"
    }
    DESKTOP_PLATFORMS = [
        'WIN10',
        'WIN1064'
    ]
    FF_WINDOWS_WIDTH = {
        "mobile": "--width=360",
        "tablet": "--width=768,",
        "desktop": "--width=1366"
    }
    FF_WINDOWS_HEIGHT = {
        "mobile": "--height=640",
        "tablet": "--height=1024",
        "desktop": "--height=768"
    }
    KEBAB_MENU_OPTIONS = {
        "rss_us": "RSS feed",
        "rss_de": "RSS-Feed",
        "rss_in": "RSS feed",
        "rss_au": "RSS feed",
        "press_us": "Press corner",
        "press_de": "Pressezentrum",
        "press_in": "Press corner",
        "press_au": "Press corner",

    }
    LEGAL_LINKS_FOOTER_US_LOCALE_DICT = {
        "Privacy": "https://policies.google.com/privacy",
        "Terms": "https://policies.google.com/terms",
        "About Google": "https://about.google/",
        "Google Products": "https://about.google/products/",
        "About the Keyword": "https://blog.google/inside-google/company-announcements/about/",
        "Help": "https://support.google.com/"
    }
    NEWSLETTER_FIRST_NAME = 'AT TEST'
    NEWSLETTER_EMAIL = 'at_test@hugeinc.com'
    NEWSLETTER_CONFIRMATION = 'Done! Check your inbox toconfirm your subscription.'
    PLATFORM_IOS = 'IOS'
    PLATFORM_MAC = 'MAC'
    PLATFORM_WIN = "WIN"
    PLATFORMS_WITH_UA = [
        'WIN10',
        'WIN1064',
        'ANDROID',
        'IOS'
    ]
    SAFARI_WINDOWS_WIDTH = {
        "mobile": "360",
        "tablet": "768",
        "desktop": "1366"
    }
    SAFARI_WINDOWS_HEIGHT = {
        "mobile": "640",
        "tablet": "1024",
        "desktop": "768"
    }
    MOBILE_PLATFORMS = [
        'ANDROID',
        'IOS'
    ]
    UA_BROWSERS = [
        'edge',
        'ie',
        'firefox_ua',
        'ios'
    ]
    USER_AGENTS = {
        "android": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965F Build/R16NW) AppleWebKit/537.36 (KHTML, "
                   "Chrome/63.0.3239.111 Mobile Safari/537.36",
        "ios": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
        "ie": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 "
                 "Safari/537.36 Edge/14.14393",
        "edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/63.0.3239.111 Safari/537.36 Edge/15.15063 "
    }




class Constants(object):
    BASE_URL = 'https://blog.google'
    SEARCH_URL = "search/?query="
    BASE_URL_STAGE = 'https://gweb-uniblog-publish-stage.appspot.com/supportingnews'

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
    # %b: Returns the first three characters of the month name.
    # %d: Returns day of the month, from 1 to 31.
    # %Y: Returns the year in four-digit format.
    # %m: Returns the month as a number
    DATE_FORMAT_IN_RSS = '%d %b %Y'
    DATE_FORMAT_IN_API = '%Y-%m-%d'
    DATE_FORMAT_IN_FEED_PER_LOCALE = {
        'en_US': '%b %d',
        'de_DE': '%d. %b.',
        'en_AU': '%b %d',
        'en_GB': '%d %b'
    }
    DATE_FORMAT_IN_FEED_PAST_YEAR_PER_LOCALE = {
        'en_US': '%b %Y',
        'de_DE': '%b %Y',
        'en_AU': '%b %Y',
        'en_GB': '%b %Y'
    }
    DATE_FORMAT_PER_LOCALE = {
        'en_US': '%b %d, %Y',
        'de_DE': '%d.%b.%Y',
        'en_AU': '%b %d, %Y',
        'en_GB': '%d %b, %Y'
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
    LEGAL_LINKS_FOOTER_INDIA_LOCALE_DICT = {
        "Privacy": "https://policies.google.com/privacy",
        "Terms": "https://policies.google.com/terms",
        "About Google": "https://about.google/",
        "Google Products": "https://about.google/products/",
        "About the Keyword": "https://blog.google/intl/en-in/about",
        "Help": "https://support.google.com/"
    }
    LEGAL_LINKS_FOOTER_AUSTRALIA_LOCALE_DICT = {
        "Privacy": "https://policies.google.com/privacy",
        "Terms": "https://policies.google.com/terms",
        "About Google": "https://about.google/intl/ALL_au/google-in-australia/",
        "Google Products": "https://about.google/products/",
        "About the blog": "https://blog.google/intl/en-au/about",
        "Help": "https://support.google.com/"
    }
    LEGAL_LINKS_FOOTER_GERMANY_LOCALE_DICT = {
        "Datenschutz": "https://policies.google.com/privacy?hl=de&fg=1",
        "Nutzungsbedingungen": "https://policies.google.com/terms?hl=de",
        "Über Google": "https://about.google/",
        "Unsere Produkte": "https://about.google/products/",
        "Über unseren Blog": "https://blog.google/intl/de-de/uber",
        "Hilfe": "https://support.google.com/?hl=de"
    }
    US_LOCALE = "/"
    INDIA_LOCALE = "/intl/en-in/"
    INDIA_CATEGORY_PAGE = '/intl/en-in/products/platforms/#android'
    AUSTRALIA_LOCALE = "/intl/en-au/"
    AUSTRALIA_CATEGORY_PAGE = '/intl/en-au/products/android-chrome-more/'
    GERMANY_LOCALE = "/intl/de-de/"
    GERMANY_CATEGORY_PAGE = "/intl/de-de/produkte/android-chrome-mehr/#android"
    NEWSLETTER_FIRST_NAME = 'AT TEST'
    NEWSLETTER_INVALID_FIRST_NAME = 'AT TEST.*'
    NEWSLETTER_ERROR_MSG_NAME = 'Sorry, only letters (a-z), and numbers (0-9) are allowed.'
    NEWSLETTER_ERROR_MSG_EMAIL = 'Email address contains error(s).'
    NEWSLETTER_EMAIL = 'at_test@hugeinc.com'
    NEWSLETTER_INVALID_EMAIL = 'at_test@'
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





class Constants(object):

    PLATFORM_IOS = 'IOS'
    PLATFORM_MAC = 'MAC'
    PLATFORM_WIN = "WIN"
    PLATFORMS_WITH_UA = [
        'WIN10',
        'WIN1064',
        'ANDROID',
        'IOS'
    ]
    DESKTOP_PLATFORMS = [
        'WIN10',
        'WIN1064'
    ]
    MOBILE_PLATFORMS = [
        'ANDROID',
        'IOS'
    ]
    UA_BROWSERS = [
        'chrome',
        'edge',
        'ie'
    ]
    USER_AGENTS = {
        "ANDROID": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965F Build/R16NW) AppleWebKit/537.36 (KHTML, "
                   "Chrome/63.0.3239.111 Mobile Safari/537.36",
        "IOS": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
        "WIN10": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 "
                 "Safari/537.36 Edge/14.14393",
        "WIN1064": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/63.0.3239.111 Safari/537.36 Edge/15.15063 "
    }
    WINDOWS_SIZE = {
        "mobile": "window-size=375,800",
        "tablet": "window-size=600,800",
        "desktop": "window-size=1440,1200"
    }



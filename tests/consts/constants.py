class Constants(object):

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




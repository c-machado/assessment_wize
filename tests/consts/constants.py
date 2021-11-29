class Constants(object):
    ADD_TOS_LINK = "/chrome/terms/"
    APP_NAME = "appname=Google%20Chrome"
    AP_WIN32 = "ap=stable-arch_x86"
    AP_WIN_PARAMETER = {
        "STABLEWIN7": "stable-arch_x86-statsdef_1",
        "STABLEWIN10": "stable-arch_x86-statsdef_1",
        "STABLEWIN764": "x64-stable-statsdef_1",
        "STABLEWIN1064": "x64-stable-statsdef_1",
        "STABLEWINXP": "stable-arch_x86",
        "CANARYWIN7": "-statsdef_1",
        "CANARYWIN764": "x64-canary-statsdef_1",
        "CANARYWIN10": "-statsdef_1",
        "CANARYWIN1064": "x64-canary-statsdef_1",
        "BETAWIN7": "-arch_x86-statsdef_1",
        "BETAWIN764": "-arch_x64-statsdef_1",
        "BETAWIN10": "-arch_x86-statsdef_1",
        "BETAWIN1064": "-arch_x64-statsdef_1",
        "DEVWIN7": "-arch_x86-statsdef_1",
        "DEVWIN764": "-arch_x64-statsdef_1",
        "DEVWIN10": "-arch_x86-statsdef_1",
        "DEVWIN1064": "-arch_x64-statsdef_1"
    }
    BASE_URL = "https://www.google.com/"
    BROWSER_VERSION = {
        "safari": "0",
        "ie": "2",
        "firefox": "3",
        "chrome": "4",
        "edge": "5"
    }
    BROWSER_VERSION_PARAM = "browser"
    CHANNEL_GUID = {
        "stable": "{8A69D345-D564-463C-AFF1-A69D9E530F96}",
        "beta": "{8237E44A-0054-442C-B6B6-EA0509993955}",
        "dev": "{401C381F-E0DE-4B85-8BD8-3F3F14FBDA57}",
        "canary": "{4EA16AC7-FD5A-47C3-875B-DBF4A2008C20}",
    }
    CHANNEL_GUID_PARAM = "appguid"
    CHANNEL_APP_NAME = {
        "stable": "Google Chrome",
        "beta": "Google Chrome Beta",
        "dev": "Google Chrome Dev",
        "canary": "Google Chrome Canary",
    }
    CHANNEL_APP_NAME_PARAM = "appname"
    DATA_INDEX_DEFAULT = "defaultbrowser"
    DATA_INDEX_EMPTY = "empty"
    DEFAULT_BROWSER_PARAM = "defaultbrowser"
    DOWNLOAD_CTA_BOTTOM = "js-download-now"
    DOWNLOAD_SECTION = ".chr-download-browser"
    EULA_MODAL = {
        "eula": "js-eula-content",
        "other_versions": "js-other-platform-modal",
        "chrome_os": "js-chrome-os-modal"
    }
    FOOTER_ID = "js-footer"
    GUID_STABLE = "8A69D345-D564-463C-AFF1-A69D9E530F96"
    GUID_BETA = "8237E44A-0054-442C-B6B6-EA0509993955"
    GUID_DEV = "401C381F-E0DE-4B85-8BD8-3F3F14FBDA57"
    GUID_CANARY = "4EA16AC7-FD5A-47C3-875B-DBF4A2008C20"
    INSTALL_DATA_INDEX = "installdataindex"
    LANGUAGE_PARAM = "lang"
    LINUX_CHROME_DRIVER = "/chrome-test/bin/linux/chromedriver"
    LINUX_FIREFOX_DRIVER = "/chrome-test/bin/linux/geckodriver"
    MAC_49_INSTALLER = "https://dl.google.com/dl/chrome/mac/legacy/GGRO/googlechrome.dmg"
    MAC_49_DEV = "js-get-stable-dev-mac49-hero"
    MAC_65_INSTALLER = "https://dl.google.com/dl/chrome/mac/legacy10_9/GGRO/googlechrome.dmg"
    NEEDS_ADMIN_CANARY = "false"
    NEEDS_ADMIN_PARAM = "needsadmin"
    NEEDS_ADMIN_PREFER = "prefers"
    NO_PROMO_CODE = "GGRO"
    OTHER_VS_MODAL = "js-other-platform-modal"
    PLATFORM_IOS = 'IOS'
    PLATFORM_MAC = 'MAC'
    PLATFORM_LINUX = "LINUX"
    PLATFORM_WIN = "WIN"
    PLATFORMS_WITH_UA = [
        'MAC49',
        'MAC65',
        'MAC88',
        'WIN7',
        'WIN764',
        'WINXP',
        'WIN10',
        'WIN1064',
        'CHROMEOS',
        'ANDROID'
    ]
    STAGE_THANK_YOU = "thankyou"
    STAGE_PARAM = "stage"
    STAGE_RETRY = "retry"
    STATCB_PARAM = "statcb"
    STANDALAONE_64 = "64"
    STANDALONE_INSTALLER_WIN = {
        "beta64": "/chrome/install/beta/ChromeBetaStandaloneSetup64.exe",
        "beta": "/chrome/install/beta/ChromeBetaStandaloneSetup.exe",
        "dev64": "/chrome/install/dev/ChromeDevStandaloneSetup64.exe",
        "dev": "/chrome/install/dev/ChromeDevStandaloneSetup.exe"
    }
    THANK_YOU = "thank-you"
    TOS_LINK = "https://policies.google.com/terms"
    USAGESTATS_0 = "0"
    USAGESTATS_1 = "1"
    USAGESTATS_PARAM = "usagestats"
    UA_BROWSERS = [
        'chrome',
        'edge',
        'ie',
        'firefox'
    ]
    USER_AGENTS = {
        "ANDROID": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965F Build/R16NW) AppleWebKit/537.36 (KHTML, "
                   "Chrome/63.0.3239.111 Mobile Safari/537.36",
        "IOS": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
        "MAC49": "Mozilla/5.0 (Macintosh; Intel mac_platform OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/63.0.3239.111 Safari/537.36",
        "MAC65": "Mozilla/5.0 (Macintosh; Intel mac_platform OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/67.0.3396.62 Safari/537.36",
        "MAC88": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "LINUX": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 "
                 "Safari/537.36",
        "CHROMEOS": "Mozilla/5.0 (X11; CrOS x86_64 11021.81.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/70.0.3538.110 Safari/537.36",
        "WIN7": "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0; MSN 9.0;MSN 9.1;MSN 9.6;MSN 10.0;MSN 10.2;MSN "
                "10.5; MSNbMSNI; MSNmen-us; MSNcIA)",
        "WIN764": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; MSN 9.0;MSN 9.1;MSN 9.6;MSN 10.0;MSN "
                  "10.2;MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)",
        "WINXP": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; SV1",
        "WIN10": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 "
                 "Safari/537.36 Edge/14.14393",
        "WIN1064": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/63.0.3239.111 Safari/537.36 Edge/15.15063 "
    }
    UNSUPPORTED_DOWNLOAD_MSG = {
        "dev": 'ga-event-label="home-dev:get-chrome-stable"',
        "beta": 'ga-event-label="home-beta:get-chrome-stable"',
        "canary": '"home-canary:get-chrome-stable"'
    }


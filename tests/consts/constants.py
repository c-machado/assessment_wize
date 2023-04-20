from dataclasses import dataclass


@dataclass
class Constants:
    # BASE_URL = 'https://blog.google'
    BASE_URL = 'https://gweb-uniblog-publish-prod.appspot.com'
    SEARCH_URL = "search/?query="
    # BASE_URL = 'https://gweb-uniblog-publish-stage.appspot.com'
    # BASE_URL = 'https://gweb-uniblog-publish-dev.appspot.com'
    # BASE_URL = 'https://gweb-uniblog-author-dev.appspot.com/admin'
    PROD_URL = 'blog.google'
    CHROME_PROFILE = '/Users/cmachado/Documents/chrome_huge_inc'
    CHROME_PROFILE_APJ = '/Users/pieschaconjoya/Documents/Chrome_Profile'
    CHROME_PROFILE_DZ = '/Users/luisdavid/Documents/automation/keyword/chrome_profile'
    #CHROME_PROFILE_LINUX = '/usr/local/google/home/machadoca/Documents/chrome_google'
    FIREFOX_PROFILE = '/Users/machadoca/Library/Application Support/Firefox/Profiles/4jwzwjvm.default'
    # FIREFOX_PROFILE = '	/Users/machadoca/Library/Application Support/Firefox/Profiles/e0zi780p.Keyword_test'
    COOKIE_BANNER_TXT = {
        "en": "Google serves cookies to analyze traffic to this site. Information about your use of our site is "
              "shared with Google for that purpose.",
        "de": "Auf dieser Website werden Google eigene Cookies verwendet, um Google-Dienste bereitzustellen, "
              "deren Qualität zu verbessern und Datenverkehr zu analysieren.",
        "fr": "Ce site utilise des cookies provenant de Google afin de fournir ses services, d'en améliorer "
              "la qualité et d'analyser le trafic.",
        "pt": "Este site usa cookies do Google para prestar serviços e melhorar a qualidade deles, além de analisar o tráfego.",
        "es": "Este sitio usa cookies de Google para ofrecer y mejorar la calidad de sus servicios y analizar el tráfico.",
        "it": "Questo sito utilizza i cookie di Google per erogare i propri servizi, migliorarne la qualità e analizzare il traffico.",
        "ar": "يستخدم هذا الموقع الإلكتروني ملفات تعريف ارتباط من Google لتقديم خدماته وتحسين جودتها وتحليل عدد الزيارات."
    }

    CHROME_WINDOWS_SIZE = {
        "mobile": "window-size=414,1000",
        "tablet": "window-size=600,800",
        "desktop": "window-size=1920,1080"
    }
    # %b: Returns the first three characters of the month name.
    # %d: Returns day of the month, from 1 to 31.
    # %Y: Returns the year in four-digit format.
    # %m: Returns the month as a number
    DATE_FORMAT_IN_RSS = '%d %b %Y'
    DATE_FORMAT_IN_API = '%Y-%m-%d'

    DATE_FORMAT_BABEL_IN_FEED_PER_LOCALE = {
        'en_US': 'MMM dd',
        'de_DE': 'dd. MMM.',
        'en_AU': 'MMM dd',
        'en_GB': 'dd MMM',
        'fr_CA': 'dd MMM',
        'en_CA': 'MMM dd',
        'pt_BR': 'dd MMM',
        'es_ES': 'MMM dd',
        'it_IT': 'dd MMM',
        'ar_MENA': 'dd MMM',
        'en_africa': 'dd MMM'
    }
    DATE_FORMAT_BABEL_IN_FEED_PAST_YEAR_PER_LOCALE = {
        'en_US': 'MMM yyyy',
        'de_DE': 'MMM yyyy',
        'en_AU': 'MMM yyyy',
        'en_GB': 'MMM yyyy',
        'fr_CA': 'MMM yyyy',
        'en_CA': 'MMM yyyy',
        'pt_BR': 'MMM yyyy',
        'es_ES': 'MMM yyyy',
        'it_IT': 'MMM yyyy',
        'ar_MENA': 'MMM yyyy',
        'en_africa': 'MMM yyyy'
    }
    DATE_FORMAT_PER_LOCALE = {
        'en_US': '%b %d, %Y',
        'de_DE': '%d.%b.%Y',
        'en_AU': '%b %d, %Y',
        'en_GB': '%d %b, %Y',
        'en_IN': '%d %b, %Y',
        'pt_BR': '%d %b, %Y',
        'en_CA': '%b %d, %Y',
        'fr_CA': '%d %b, %Y',
        'es_ES': '%b %d, %Y',
        'it_IT': '%d %b, %Y',
        'ar_MENA': '%b, %Y %d'
    }
    DATE_FORMAT_PER_LOCALE_BABEL = {
        'en_US': 'MMM dd, yyyy',
        'de_DE': 'dd.MMM.yyyy',
        'en_AU': 'MMM dd, yyyy',
        'en_GB': 'dd MMM, yyyy',
        'pt_BR': 'dd MMM, yyyy',
        'en_CA': 'MMM dd, yyyy',
        'fr_CA': 'dd MMM, yyyy',
        'es_ES': 'MMM dd, yyyy',
        'it_IT': 'dd MMM, yyyy',
        'ar_MENA': 'dd MMM, yyyy'
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
    HTML_string = '''<!DOCTYPE html><html><head><style>table …'''
    KEBAB_MENU_OPTIONS = {
        "rss_en": "RSS feed",
        "rss_de": "RSS-Feed",
        "rss_ar_mena": "خلاصة RSS",
        "press_en": "Press corner",
        "press_de": "Pressezentrum",
        "press_fr_ca": "Salle de presse",
        "press_pt_br": "Imprensa",
        "press_es_419": "Prensa",
        "press_it_it": "Stampa",
        "press_ar_mena": "ركن الصحافة"
    }
    LANGUAGE_SELECTOR = {
        "English",
        "Deutsch",
        "English (Africa)",
        "English (India)",
        "English (Australia)",
        "English (Canada)",
        "Français (Canada)",
        "Português (Brasil)",
        "Español (Latinoamérica)",
        "Italiano",
    }
    LANGUAGE_SELECTOR_URLS = {
        "English": "/",
        "Deutsch": "/intl/de-de/",
        # "English (Africa)": "/intl/en-africa/,
        "English (India)": "/intl/en-in/",
        "English (Australia)": "/intl/en-au/",
        "English (Canada)": "/intl/en-ca/",
        "Français (Canada)": "/intl/fr-ca/",
        "Português (Brasil)": "/intl/pt-br/",
        "Español (Latinoamérica)": "/intl/es-419/",
        "Italiano": "/intl/it-it/",
    }
    LEGAL_LINKS = {
        '/': {
            "Privacy": "https://policies.google.com/privacy",
            "Terms": "https://policies.google.com/terms",
            "About Google": "https://about.google/",
            "Google Products": "https://about.google/products/",
            "Help": "https://support.google.com/"
        },
        '/intl/en-in/': {
            "Privacy": "https://policies.google.com/privacy",
            "Terms": "https://policies.google.com/terms",
            "About Google": "https://about.google/",
            "Google Products": "https://about.google/products/",
            "Help": "https://support.google.com/"
        },
        '/intl/en-au/': {
            "Privacy": "https://policies.google.com/privacy",
            "Terms": "https://policies.google.com/terms",
            "About Google": "https://about.google/intl/ALL_au/google-in-australia/",
            "Google Products": "https://about.google/products/",
            "Help": "https://support.google.com/"
        },
        '/intl/en-ca/': {
            "Privacy": "https://policies.google.com/privacy",
            "Terms": "https://policies.google.com/terms",
            "About Google": "https://about.google/",
            "Google Products": "https://about.google/products/",
            "Help": "https://support.google.com/"
        },
        '/intl/en-africa/': {
            "Privacy": "https://policies.google.com/privacy",
            "Terms": "https://policies.google.com/terms",
            "About Google": "https://about.google/",
            "Google Products": "https://about.google/products/",
            "Help": "https://support.google.com/"
        },
        '/intl/fr-ca/': {
            "Confidentialité": "https://policies.google.com/privacy?hl=fr-CA",
            "Conditions": "https://policies.google.com/terms?hl=fr-CA",
            "À propos de Google": "https://about.google/",
            "Google Produits": "https://about.google/products/",
            "Aide": "https://support.google.com/?hl=fr"
        },
        '/intl/de-de/': {
            "Datenschutz": "https://policies.google.com/privacy?hl=de&fg=1",
            "Nutzungsbedingungen": "https://policies.google.com/terms?hl=de",
            "Über Google": "https://about.google/",
            "Unsere Produkte": "https://about.google/products/",
            "Hilfe": "https://support.google.com/?hl=de"
        },
        '/intl/pt-br/': {
            "Política de Privacidade": "https://policies.google.com/privacy?hl=pt-br",
            "Termos de Serviço": "https://policies.google.com/terms?hl=pt-br",
            "Sobre o Google": "https://about.google/intl/pt-br/",
            "Produtos do Google": "https://about.google/products/",
            "Ajuda": "https://support.google.com/?hl=pt-BR"
         },
        '/intl/es-419/': {
            "Privacidad": "https://policies.google.com/privacy?hl=es-419",
            "Términos y condiciones": "https://policies.google.com/terms?hl=es-419",
            "Sobre Google": "https://about.google/intl/es-419/",
            "Productos de Google": "https://about.google/products/",
            "Ayuda": "https://support.google.com/?hl=es-419"
        },
        '/intl/it-it/': {
            "Norme sulla privacy": "https://policies.google.com/privacy?hl=it-IT",
            "Termini e condizioni": "https://policies.google.com/terms?hl=it-IT",
            "L’azienda": "https://about.google/",
            "Prodotti di Google": "https://about.google/products/",
            "Aiuto": "https://support.google.com/?hl=it"
        },
        '/intl/ar-mena/': {
            "الخصوصية": "https://policies.google.com/privacy?hl=ar",
            "بنود الخدمة": "https://policies.google.com/terms?hl=ar",
            "لمحة عن Google": "https://about.google/",
            "منتجات Google": "https://about.google/products/",
            "مساعدة": "https://support.google.com/?hl=ar"
        },
        '/products/ads-commerce': {
            "Privacy": "https://policies.google.com/privacy",
            "Terms": "https://policies.google.com/terms",
            "About Google": "https://about.google/",
            "Google Products": "https://about.google/products/",
            "Help": "https://support.google.com/"
        },
        '/waze/': {
            "Privacy": "https://policies.google.com/privacy",
            "Terms": "https://policies.google.com/terms",
            "About Google": "https://about.google/",
            "Google Products": "https://about.google/products/",
            "Help": "https://support.google.com/"
        }
    }
    LEGAL_LINKS_ABOUT_THE_BLOG_COPY = {
        "/": "About the Keyword",
        "/intl/en-in/": "About the blog",
        '/intl/en-au/': "About the blog",
        '/intl/en-ca/': "About the blog",
        '/intl/en-africa/': "About the blog",
        '/intl/fr-ca/': "À propos du blogue",
        '/intl/de-de/': "Über unseren Blog",
        '/intl/pt-br/': "Sobre o blog",
        '/intl/es-419/': "Sobre el blog",
        '/intl/it-it/': "Il blog",
        '/intl/ar-mena/': "لمحة عن المدونة"
        }
    LEGAL_LINKS_ABOUT_THE_BLOG_URL = {
        "/": "/inside-google/company-announcements/about/",
        "/intl/en-in/": "/intl/en-in/about",
        '/intl/en-au/': "/intl/en-au/about",
        '/intl/en-africa/': "/intl/en-africa/about",
        '/intl/en-ca/': "/intl/en-ca/about",
        '/intl/fr-ca/': "/intl/fr-ca/a-propos",
        '/intl/de-de/': "/intl/de-de/uber",
        '/intl/pt-br/': "/intl/pt-br/sobre-o-blog",
        '/intl/es-419/': "/intl/es-419/sobre-el-blog",
        '/intl/it-it/': "/intl/it-it/sul-blog",
        '/intl/ar-mena/': "/intl/ar-mena/about"
    }

    CATEGORY_HORIZONTAL = [
        '/intl/en-au/products/android-chrome-more/',
        '/intl/en-ca/products/explore-get-answers/',
        '/intl/fr-ca/produits/explorez-obtenez-des-reponses/',
        '/intl/de-de/produkte/android-chrome-mehr/#android',
        '/intl/en-in/products/platforms/#android',
        '/intl/pt-br/produtos/android-chrome-play/',
        '/intl/es-419/actualizaciones-de-producto/android-chrome-play/',
        '/intl/it-it/prodotti/android-chrome-play/',
        '/intl/it-it/prodotti/devices-services/#pixel',
        '/intl/en-africa/products/android-chrome-play/#googleplay'
    ]
    US_LOCALE = "/"
    INDIA_LOCALE = "/intl/en-in/"
    AUSTRALIA_LOCALE = "/intl/en-au/"
    EN_CANADA_LOCALE = "/intl/en-ca/"
    EN_AFRICA_LOCALE = "/intl/en-africa/"
    FR_CANADA_LOCALE = "/intl/fr-ca/"
    GERMANY_LOCALE = "/intl/de-de/"
    PT_BRAZIL_LOCALE = "/intl/pt-br/"
    NEWSLETTER_ERROR_MSG_EMAIL = 'Email address contains error(s).'
    NEWSLETTER_EMAIL = 'at_test@hugeinc.com'
    NEWSLETTER_INVALID_EMAIL = "at_'%^test@hmail.com"
    NEWSLETTER_CONFIRMATION = 'Done. Just one step more.Check your inbox to confirm your subscription.'
    NEWSLETTER_CONFIRMATION_STICKY = 'Done. Just one step more. Check your inbox to confirm your subscription.'
    NEWSLETTER_CONFIRMATION_MOBILE = 'Done. Just one step more.\nCheck your inbox to confirm your subscription.'
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
    SCROLL_TO_HOME_FEED = '.feed-article.ng-scope:nth-child(index_to_scroll)'
    SCROLL_TO_CATEGORY_HORIZONTAL_FEED = '.feed-article.ng-scope:nth-child(index_to_scroll)'
    SCROLL_TO_FEED = '.article-list__feed'
    SITESPACE_TITLE_IN_PRODUCTS = [
        'AdSense',
        'Google Ads & Commerce',
        'Google Ad Manager',
        'Google Analytics products',
        'Google AdMob',
        'Google Marketing Platform'
    ]
    SITESPACE_TITLE_IN_NAV_MENU = [
        'AdSense',
        'Ads & Commerce Blog',
        'Ad Manager',
        'Marketing Platform',
        'AdMob',
        'Marketing Platform',
    ]
    SITESPACE_WAZE_IN_NAV_MENU = 'Waze Blog'
    SEARCH_NO_RESULTS_MSG = {
        'de': "Ups, die Suche nach “text_to_search” führte zu keinem Ergebnis.",
        'en': "Oops, your search for “text_to_search” didn't return any results.",
        'fr': "Oups, votre recherche “text_to_search” n’a générée aucun résultat.",
        'pt': "Ops, sua pesquisa por “text_to_search” não retornou nenhum resultado.",
        'es': "Oops, tu búsqueda “text_to_search” no arrojó resultados",
        'it': "Ops, la tua ricerca per “text_to_search” non ha avuto risultati.",
        'ar': "عذرًا، ليس هناك نتائج بحث عن “text_to_search” ."
    }
    MOBILE_PLATFORMS = [
        'ANDROID',
        'IOS'
    ]
    UA_BROWSERS = [
        'edge',
        'ie',
        'firefox',
        'safari',
        'ios',
        'android'
    ]
    USER_AGENTS = {
        "android": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/100.0.4896.58 Mobile Safari/537.36",
        "ios": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"
               " Version/15.3 Mobile/15E148 Safari/604.1",
        "edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/100.0.4896.60 Safari/537.36 Edg/99.0.1150.36",
        "firefox": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                   "Version/15.3 Safari/605.1.15"

    }





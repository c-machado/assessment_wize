# Created by machadoca at 17/01/22
Feature: As a user, I want to confirm dates are showing according to the expected format


    @feed-article-date-format
    Scenario Outline: Confirm article's date is in the correct format in homepage feed
        Given a user is at the <keyword> site
        And the user chooses a random article
        When the user in <keyword> <locale> check the date in the feed
        And the user opens the selected random article in <keyword> feed
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword      |
            | en_US     | /            |
            | de_DE     | /intl/de-de/ |
            | en_AU     | /intl/en-au/ |
            | en_GB     | /intl/en-in/ |
            | fr_CA     | /intl/fr-ca/ |
            | en_CA     | /intl/en-ca/ |
            | pt_BR     | /intl/pt-br/ |
            | es_ES     | /intl/es-419/|
            | it_IT     | /intl/it-it/ |
            | ar_MENA    | /intl/ar-mena/ |
#            TODO: Update locale code date format
            | en_US     | /intl/en-africa/ |

#    @feed-article-date-format
#    Scenario Outline: Confirm article's date is in the correct format in homepage feed
#        Given a user is at the <keyword> site
#        And the user chooses a random article
#        When the user in <keyword> <locale> check the date in the feed
#        And the user opens the selected random article in <keyword> feed
#        Then the date matches the <locale> format
#        Examples:
#            | locale    | keyword        |
#            | ar_IL     | /intl/ar-mena/ |
#
#
    @feed-article-date-format
    Scenario Outline: Confirm article's date is in the correct format in category page feed
        Given a user is at the <keyword> site
        And the user chooses a random article
        When the user in <keyword> <locale> check the date in the feed
        And the user opens the selected random article in <keyword> feed
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword                                               |
            | en_US     | /outreach-initiatives/                                |
            | de_DE     | /intl/de-de/produkte/android-chrome-mehr/#android     |
            | en_GB     | /intl/en-in/products/platforms/#android               |
            | en_AU     | /intl/en-au/products/android-chrome-more/             |
            | fr_CA     | /intl/fr-ca/produits/explorez-obtenez-des-reponses/   |
            | en_CA     | /intl/en-ca/products/explore-get-answers/             |
            | pt_BR     | /intl/pt-br/produtos/android-chrome-play/             |
            | es_ES     | /intl/es-419/actualizaciones-de-producto/android-chrome-play/ |
            | it_IT     | /intl/it-it/prodotti/devices-services/#pixel                  |
            | en_US     | /intl/en-africa/products/android-chrome-play/#googleplay      |

    #Add subcategory pages for other locales if the content gets updated
    @feed-article-date-format
    Scenario Outline: Confirm article's date is in the correct format in the subcategory page feed
        Given a user is at the <keyword> site
        And the user chooses a random article
        When the user in <keyword> <locale> check the date in the feed
        And the user opens the selected random article in <keyword> feed
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword               |
            | en_US     | /products/android/    |


    @feed-article-date-format
    Scenario Outline: Confirm article's date is in the correct format in series page feed
        Given a user is at the <keyword> site
        And the user chooses a random article
        When the user in <keyword> <locale> check the date in the feed
        And the user opens the selected random article in <keyword> feed
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword                             |
            | en_US     | /inside-google/googlers/she-word/   |


    @feed-article-date-format
    Scenario Outline: Confirm article's date is in the correct format in the perspective page feed
        Given a user is at the <keyword> site
        And the user chooses a random article
        When the user in <keyword> <locale> check the date in the feed
        And the user opens the selected random article in <keyword> feed
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword                       |
            | en_US     | /perspectives/sundar-pichai/  |

    @feed-article-date-format
    Scenario Outline: Confirm article's date is in the correct format in the sitespace feed
        Given a user is at the <keyword> site
        And the user chooses a random article
        When the user in <keyword> <locale> check the date in the feed
        And the user opens the selected random article in <keyword> feed
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword   |
            | en_US     | /waze/    |
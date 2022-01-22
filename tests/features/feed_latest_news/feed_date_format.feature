# Created by machadoca at 17/01/22
Feature: As a user I want to confirm dates are showing according to the expected format


    @feed-article
    Scenario Outline: Confirm article's date is in the correct format in homepage feed
        Given a user is at the <keyword> site
        And the uses chooses a random article
        When the user in <keyword> <locale> opens an article in the feed list
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword      |
            | en_US     | /            |
            | de_DE     | /intl/de-de/ |
            | en_AU     | /intl/en-au/ |
            | en_GB     | /intl/en-in/ |

#    @feed-article
    Scenario Outline: Confirm article's date is in the correct format in category page feed
        Given a user is at the <keyword> site
        And the date in feed articles matches with the <locale> format
        When the user opens an article in the feed list
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword                                   |
            | en_US     | /outreach-initiatives/                    |
            | de_DE     | /intl/de-de/produkte/android-chrome-mehr/ |
            | en_GB     | /intl/en-in/products/platforms/#android   |
            | en_AU     | /intl/en-au/products/android-chrome-more/ |


    #Add subcategory pages for other locales if the content gets updated
#    @feed-article
    Scenario Outline: Confirm article's date is in the correct format in subcategory page feed
        Given a user is at the <keyword> site
        And the date in feed articles matches with the <locale> format
        When the user opens an article in the feed list
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword               |
            | en_US     | /products/android/    |


#    @feed-article
    Scenario Outline: Confirm article's date is in the correct format in series page feed
        Given a user is at the <keyword> site
        And the date in feed articles matches with the <locale> format
        When the user opens an article in the feed list
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword                             |
            | en_US     | /inside-google/googlers/she-word/   |


    @feed-article
    Scenario Outline: Confirm article's date is in the correct format in the perspective page feed
        Given a user is at the <keyword> site
        And the uses chooses a random article
        When the user in <keyword> <locale> opens an article in the feed list
        Then the date is according to the <locale> format
        Examples:
            | locale    | keyword                      |
            | en_US     | /perspectives/sundar-pichai  |


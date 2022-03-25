# Created by machadoca at 25/03/22
Feature: As a user, I want to confirm dates in the related stories section are showing according to the expected format

    @article-date-format-related-stories
    Scenario Outline: Confirm article's date is in the correct format in the related stories section
        Given a user is at the <keyword> site
        And the user chooses a random article
        When the user opens the selected random article in <keyword> feed
        Then the date shown in the related stories articles are according to the <locale> format
        Examples:
            | locale    | keyword      |
            | en_US     | /            |
            | de_DE     | /intl/de-de/ |
            | en_AU     | /intl/en-au/ |
            | en_GB     | /intl/en-in/ |
            | en_CA     | /intl/en-ca/ |
            | fr_CA     | /intl/fr-ca/ |
            | pt_BR     | /intl/pt-br/ |


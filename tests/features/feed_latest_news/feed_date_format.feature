# Created by machadoca at 17/01/22
Feature: As a user I want to confirm dates are showing according to the expected format


    @feed-article
    Scenario Outline: Confirm article's date is in the correct format
        Given a user is at the <keyword> site
        When the user opens an article in the feed list
        Then the date format is according to the <locale>

        Examples:
            | locale    | keyword      |
            | en_US     | /            |
            | de_DE     | /intl/de-de/ |
            | en_AU     | /intl/en-au/ |
            | en_GB     | /intl/en-in/ |
# Created by machadoca at 7/02/22
Feature: As a user I want to confirm articles in the feed list are shown to the user according to the corresponding tag

    #TODO: tags is empty in the url, to confirm what is needed to validate in the homepages across locales
    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed in the homepage are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated matches with the content in the <keyword>
        Examples:
            | keyword      |
            | /            |
            | /intl/de-de/ |
            | /intl/en-au/ |
            | /intl/en-in/ |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed in the category page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated matches with the content in the <keyword>
        Examples:
           | keyword                                           |
           | /technology/                                      |
           | /intl/de-de/produkte/android-chrome-mehr/#android |
           | /intl/en-in/products/platforms/#android           |
           | /intl/en-au/products/android-chrome-more/         |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed in a series page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated matches with the content in the <keyword>
        Examples:
           | keyword                            |
           | /inside-google/googlers/she-word/  |

    @feed-article-tagging-author-ids
    Scenario Outline: Test articles listed in the feed in a perspective landing page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated matches with the content in the <keyword>
        Examples:
           | keyword                       |
           | /perspectives/sundar-pichai/  |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed in a sitespace are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated matches with the content in the <keyword>
        Examples:
           | keyword   |
           | /waze/    |
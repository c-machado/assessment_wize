# Created by machadoca at 1/02/22
Feature: As a user I want to confirm articles in the feed list corresponds with the type of page

    @load-more
    Scenario Outline: Test articles listed in the homepage's feed are order by desc date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
            | keyword      |
            | /            |
            | /intl/de-de/ |
            | /intl/en-au/ |
            | /intl/en-in/ |

    @load-more
    Scenario Outline: Test articles listed in the feed in the category vertical page are order by desc date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
           | keyword      |
           | /technology/ |
           | /intl/de-de/produkte/android-chrome-mehr/#android |
           | /intl/en-in/products/platforms/#android           |
           | /intl/en-au/products/android-chrome-more/         |


    @load-more
    Scenario Outline: Test articles listed in the feed in the category vertical page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated matches with the content in the <keyword>
        Examples:
           | keyword         |
           | /technology/    |
           | /intl/de-de/produkte/android-chrome-mehr/#android |
           | /intl/en-in/products/platforms/#android           |
           | /intl/en-au/products/android-chrome-more/         |


#    @load-more
#    Scenario Outline: Test articles listed in the feed in the category horizontal page are tagged accordingly
#        Given a user is at the <keyword> site
#        When the user chooses a random article
#        Then the tags associated matches with the content in the <keyword>
#        Examples:
#           | keyword                                           |
#           | /intl/de-de/produkte/android-chrome-mehr/#android |
#           | /intl/en-in/products/platforms/#android           |
#           | /intl/en-au/products/android-chrome-more/         |


# Created by machadoca at 1/02/22
Feature: As a user I want to confirm articles in the feed list corresponds with the type of page

    @load-more-
    Scenario Outline: Test articles listed in the homepage's feed
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
            | keyword      |
            | /            |
            | /intl/de-de/ |
            | /intl/en-au/ |
            | /intl/en-in/ |

    @load-more-
    Scenario Outline: Test articles listed in the feed in the category vertical page are order by date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
           | keyword      |
           | /technology/ |


    @load-more-
    Scenario Outline: Test articles listed in the feed in the category vertical page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated matches with the content in the <keyword>
        Examples:
           | keyword      |
           | /technology/ |

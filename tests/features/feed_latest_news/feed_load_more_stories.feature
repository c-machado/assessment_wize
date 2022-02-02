# Created by machadoca at 1/02/22
Feature: As a user I want to confirm articles in the feed list corresponds with the type of page

     Examples:
            | keyword      |
#            | /            |
            | /intl/de-de/ |
#            | /intl/en-au/ |
#            | /intl/en-in/ |
    @load-more
    Scenario: Test articles listed in the homepage's feed
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
#        Then the articles are shown order by date desc

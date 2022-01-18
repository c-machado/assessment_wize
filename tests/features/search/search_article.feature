# Created by machadoca at 14/01/22
Feature: As a user I would like to search content within an article page

    @search-article
    Scenario: Search content in an article
        Given a user is at the <keyword> site
        Then the feed shows the most recent articles


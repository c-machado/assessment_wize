# Created by machadoca at 14/02/22
Feature: As a user I want to search content in the nav bar in a perspectives article page

    @search-article
    Scenario Outline: Test search suggestions in a perspectives article page
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                      |
            | google         | /perspectives/sundar-pichai/ |

    @search-article
    Scenario Outline: Test the search suggestions in a perspective's article using special characters
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search    | keyword                       |
            | español           | /perspectives/sundar-pichai/  |


    @search-article
    Scenario Outline: Test search results in a perspective's article
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                      |
            | google         | /perspectives/sundar-pichai/ |


    @search-article
    Scenario Outline: Test search results in a perspective's article using special characters
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword                      |
            | Valentine's     | /perspectives/sundar-pichai/ |


    @search-article
    Scenario Outline: Test search results when there are no results in a perspective's article
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search   | keyword                         | language |
            | zwischen         | /perspectives/sundar-pichai/    | en       |


    @search-article
    Scenario Outline: Test search suggestions in a perspectives article page progress bar
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                      |
            | google         | /perspectives/sundar-pichai/ |

    @search-article
    Scenario Outline: Test the search suggestions in a perspective's article progress bar using special characters
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search    | keyword                       |
            | español           | /perspectives/sundar-pichai/  |


    @search-article
    Scenario Outline: Test search results in a perspective's article progress bar
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                      |
            | google         | /perspectives/sundar-pichai/ |


    @search-article
    Scenario Outline: Test search results in a perspective's article progress bar using special characters
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword                      |
            | Valentine's     | /perspectives/sundar-pichai/ |


    @search-article
    Scenario Outline: Test search results when there are no results in a perspective's article progress bar
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search   | keyword                         | language |
            | zwischen         | /perspectives/sundar-pichai/    | en       |

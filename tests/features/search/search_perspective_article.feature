# Created by machadoca at 14/02/22
#Search functionality works as follows:
#Suggestions: Look for the content that matches the article's title.
#Results page: Look within the article's content.
#The results appeared order by relevance, that may cause the oldest content be shown at the top.
Feature: As a user, I want to search content in the nav bar on a perspectives article page

    @search_suggestions_regression
    Scenario Outline: Test search suggestions in a perspectives article page
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                      |
            | google         | /perspectives/sundar-pichai/ |

    @search_suggestions_special_char_regression
    Scenario Outline: Test the search suggestions in a perspective's article using special characters
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search    | keyword                       |
            | español           | /perspectives/sundar-pichai/  |


    @search_results_page_regression
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


    @search_results_page_special_char_regression
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


    @search_no_results_regression
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




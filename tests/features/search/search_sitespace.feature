# Created by machadoca at 17/02/22
#Search functionality works as follows:
#Suggestions: Look for the content that matches the article's title.
#Results page: Look within the article's content.
#The results appeared order by relevance, that may cause the oldest content be shown at the top.
Feature: As a user I want to be able to search content navigating within a sitespace

    @search_suggestions_business_critical
    Scenario Outline: Test search suggestions in a sitespace
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword  |
            | google         | /waze/   |

    @search_suggestions_special_char_business_critical
    Scenario Outline: Test search suggestions in a sitespace using special characters
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword  |
            | español         | /waze/   |


    @search_results_page_business_critical
    Scenario Outline: Test search results in a sitespace page
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword   |
            | google          | /waze/    |

    @search_results_page_special_char_business_critical
    Scenario Outline: Test search results in a sitespace using special characters
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search   | keyword  |
            | español          | /waze/   |

    @search_no_results_regression
    Scenario Outline: Test search results when there are no results in a sitespace
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search      | keyword    | language |
            | zwischen            | /waze/     | en       |
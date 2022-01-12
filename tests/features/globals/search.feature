# Created by machadoca at 6/01/22
Feature: As a user I want to be able to search for content within the blog

    Examples:
        |keyword    |
        |/          |

    Scenario: Test the search bar  - expanding the search bar
        Given a user is at the <keyword> site
        When the user clicks the search icon
        Then the system shows the search bar expanded

    Scenario: Test the search bar  - collapsing the search bar
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user closes the search bar
        Then the system collapsed the search bar

    Scenario Outline: Test the results page
        Given a user is at the <keyword> site
        And the user clicks the search icon
        When the user types the <text_to_search>
        Then the system adds the <text_to_search> as a parameter in the <keyword> url

        Examples:
            | text_to_search |
            | /              |

    Scenario Outline: Test the newest and the oldest filters in the results page
        Given a user is at the <keyword> site
        And the user clicks the search icon
        When the user types the <text_to_search>
        #TODO: Complete following steps once the search is working
        And the user selects a <filter_option> the results
        Then the system updates the result based on the <filter_option>

        Examples:
            | text_to_search | filter_option |
            | /              |               |

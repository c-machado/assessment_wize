# Created by machadoca at 6/01/22
Feature: As a user, I want to be able to search for content within the blog

    Examples:
         |keyword         |
         |/               |
         |/intl/de-de/    |
         |/intl/en-in/    |
         |/intl/en-au/    |
         |/intl/fr-ca/    |
         |/intl/pt-br/    |
         |/intl/en-ca/    |
#         |/intl/en-africa/|
         |/intl/es-419/   |
         |/intl/it-it/    |

    @search
    Scenario: Test the search bar  - expanding the search bar
        Given a user is at the <keyword> site
        When the user clicks the search icon
        Then the system shows the search bar expanded


    @search
    Scenario: Test the search bar  - collapsing the search bar
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user closes the search bar
        Then the system collapsed the search bar


    @search
    Scenario Outline: Test the results page
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system adds the <text_to_search> as a parameter in the <keyword> url

        Examples:
            | text_to_search |
            | google         |

    @search
    Scenario Outline: Test filter by random tag in the results page
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And  the user clicks the magnifying glass
        And the user selects a random filter
        Then the system filters the results on <keyword>

        Examples:
            | text_to_search |
            | google         |
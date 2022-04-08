# Created by machadoca at 8/04/22
Feature: As a user I want to be able to search for content within the blog on mobile

    Examples:
        |keyword      | mobile  |
        |/            | ios     |
        |/intl/de-de/ | ios     |
        |/intl/en-in/ | ios     |
        |/intl/en-au/ | ios     |
        |/intl/fr-ca/ | ios     |
        |/intl/pt-br/ | ios     |
        |/intl/en-ca/ | ios     |

    @search-mobile
    Scenario: Test the search bar  - expanding the search bar on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        Then the system shows the search bar expanded

    @search-mobile
    Scenario: Test the search bar  - collapsing the search bar on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user closes the search bar
        Then the system collapsed the search bar

    @search-mobile
    Scenario Outline: Test the results page on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system adds the <text_to_search> as a parameter in the <keyword> url

        Examples:
            | text_to_search |
            | google         |

    @search-mobile
    Scenario Outline: Test the newest and the oldest filters in the results page on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And  the user clicks the magnifying glass
        And the user selects a random filter
        Then the system filters the results on <keyword>

        Examples:
            | text_to_search |
            | google         |
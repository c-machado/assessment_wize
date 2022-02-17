# Created by machadoca at 17/02/22
Feature: As a user I would like to search content while navigating in the homepage

    @search-home
    Scenario Outline: Test search suggestions in the homepage
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword       |
            | google         | /             |
            | sicherer       | /intl/de-de/  |
            | digital        | /intl/en-in/  |
            | australians    | /intl/en-au/  |

    @search-home
    Scenario Outline: Test search suggestions in the homepage using special characters
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search            | keyword       |
            | español                   | /             |
            | Privatsphäre              | /intl/de-de/  |
            | India’s mini-masterpieces | /intl/en-in/  |
            | Australia’s non-profits   | /intl/en-au/  |


    @search-home
    Scenario Outline: Test search results in the homepage
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword       |
            | google         | /             |
            | sicherer       | /intl/de-de/  |
            | digital        | /intl/en-in/  |
            | australians    | /intl/en-au/  |

    @search-home
    Scenario Outline: Test search results in the homepage using special characters
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search            | keyword       |
            | Valentine's               | /             |
            | schützt                   | /intl/de-de/  |
            | Badshah’s #JugnuChallenge | /intl/en-in/  |
            | $1.89                     | /intl/en-au/  |

    @search-home
    Scenario Outline: Test search results when there are no results in the homepage
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search            | keyword       | language |
            | zwischen                  | /             | en       |
            | riqueza                   | /intl/de-de/  | de       |
            | Themenverwandte           | /intl/en-in/  | en       |
            | Datenaustausch            | /intl/en-au/  | en       |
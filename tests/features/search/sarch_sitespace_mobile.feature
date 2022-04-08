# Created by machadoca at 8/04/22
Feature: As a user I want to be able to search content navigating within a site space on mobile
    Examples:
    |mobile|
    |ios   |

    @search-sitespace-mobile
    Scenario Outline: Test search suggestions in a site space on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword  |
            | google         | /waze/   |

    @search-sitespace-mobile
    Scenario Outline: Test search suggestions in a site space using special characters on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword  |
            | español         | /waze/   |


    @search-sitespace-mobile
    Scenario Outline: Test search results in a site space page on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword   |
            | google          | /waze/    |

    @search-sitespace-mobile
    Scenario Outline: Test search results in a site space using special characters on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search   | keyword  |
            | español          | /waze/   |

    @search-sitespace-mobile
    Scenario Outline: Test search results when there are no results in a site space on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search      | keyword    | language |
            | zwischen            | /waze/     | en       |
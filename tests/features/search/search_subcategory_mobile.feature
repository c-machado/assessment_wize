# Created by machadoca at 7/04/22
Feature: As a user, I would like to search for the content navigating a subcategory page

    Examples:
    |mobile|
    |ios   |

    @search-subcategory-mobile
    Scenario Outline: Test search suggestions in a subcategory page
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword             |
            | google         | /products/android/  |

    @search-subcategory-mobile
    Scenario Outline: Test search suggestions in a subcategory page using special characters
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword              |
            | español         | /products/android/   |


    @search-subcategory-mobile
    Scenario Outline: Test search results on a subcategory page
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword               |
            | google          | /products/android/    |

    @search-subcategory-mobile
    Scenario Outline: Test search results in a subcategory page using special characters
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search   | keyword              |
            | español          | /products/android/   |

    @search-subcategory-mobile
    Scenario Outline: Test search results when there are no results on a subcategory page
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search      | keyword                | language |
            | zwischen            | /products/android/     | en       |
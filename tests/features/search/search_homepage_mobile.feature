# Created by machadoca at 7/04/22
# Created by machadoca at 17/02/22
Feature: As a user, I would like to search for the content while navigating the homepage

    Examples:
    |mobile|
    |ios   |

    @search-home-mobile
    Scenario Outline: Test search suggestions in the homepage
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword       |
            | google         | /             |
            | sicherer       | /intl/de-de/  |
            | digital        | /intl/en-in/  |
            | australians    | /intl/en-au/  |
            | nouvelles      | /intl/fr-ca/  |
            | parcerias      | /intl/pt-br/  |
            | cloud          | /intl/en-ca/  |

    @search-home-mobile
    Scenario Outline: Test search suggestions on the homepage using special characters
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search            | keyword       |
            | español                   | /             |
            | Privatsphäre              | /intl/de-de/  |
            | India’s mini-masterpieces | /intl/en-in/  |
            | Australia’s non-profits   | /intl/en-au/  |
            | câble                     | /intl/fr-ca/  |
            | desinformação             | /intl/pt-br/  |
            | trans-Pacific             | /intl/en-ca/  |


    @search-home-mobile
    Scenario Outline: Test search results on the homepage
        Given a user is at the <keyword> site on <mobile>
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
            | nouvelles      | /intl/fr-ca/  |
            | pessoas        | /intl/pt-br/  |
            | subsea         | /intl/en-ca/  |

    # TODO: Error with texts with special characters in the wrong format. https://hugeinc.atlassian.net/browse/UNI-6398
    @search-home-mobile
    Scenario Outline: Test search results on the homepage using special characters
        Given a user is at the <keyword> site on <mobile>
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
            | câble                     | /intl/fr-ca/  |
            | l'Asie                    | /intl/fr-ca/  |
            | informações               | /intl/pt-br/  |
            | Canada's K-12             | /intl/en-ca/  |

    @search-home-mobile
    Scenario Outline: Test search results when there are no results on the homepage
        Given a user is at the <keyword> site on <mobile>
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
            | sondern                   | /intl/pt-br/  | pt       |
            | pesquisa                  | /intl/fr-ca/  | fr       |
            | retornou                  | /intl/en-ca/  | en       |
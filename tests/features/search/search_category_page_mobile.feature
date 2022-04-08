# Created by machadoca at 7/04/22
Feature: As a user, I would like to search for the content while navigating on a category page
    Examples:
    |mobile|
    |ios   |

    @search-category-mobile
    Scenario Outline: Test search suggestions on a category page on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                                            |
            | google         | /technology/                                       |
            | sicherer       | /intl/de-de/produkte/android-chrome-mehr/#android  |
            | digital        | /intl/en-in/products/platforms/#android            |
            | australians    | /intl/en-au/products/android-chrome-more/          |
            | COVID          | /intl/en-ca/products/cloud/                        |
            | voyager        | /intl/fr-ca/produits/explorez-obtenez-des-reponses/|
            | vacinas        | /intl/pt-br/produtos/explore-e-encontre-respostas/ |

    @search-category-mobile
    Scenario Outline: Test search suggestions on a category page using special characters on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search             | keyword                                            |
            | español                    | /technology/                                       |
            | Privatsphäre               | /intl/de-de/produkte/android-chrome-mehr/#android  |
            | India’s mini-masterpieces  | /intl/en-in/products/platforms/#android            |
            | Australia’s non-profits    | /intl/en-au/products/android-chrome-more/          |
            | Google’s                   | /intl/en-ca/products/cloud/                        |
#            | possèdent                  | /intl/fr-ca/produits/explorez-obtenez-des-reponses/|
            | téléphone                  | /intl/fr-ca/produits/explorez-obtenez-des-reponses/|
            | desinformação              | /intl/pt-br/produtos/explore-e-encontre-respostas/ |


    @search-category-mobile
    Scenario Outline: Test search results on a category page on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                                            |
            | google         | /technology/                                       |
            | sicherer       | /intl/de-de/produkte/android-chrome-mehr/#android  |
            | digital        | /intl/en-in/products/platforms/#android            |
            | australians    | /intl/en-au/products/android-chrome-more/          |
            | COVID          | /intl/en-ca/products/cloud/                        |
            | voyager        | /intl/fr-ca/produits/explorez-obtenez-des-reponses/|
            | vacinas        | /intl/pt-br/produtos/explore-e-encontre-respostas/ |

    @search-category-mobile
    Scenario Outline: Test search results in a category page using special characters on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search             | keyword                                            |
            | español                    | /technology/                                       |
            | Privatsphäre               | /intl/de-de/produkte/android-chrome-mehr/#android  |
            | India’s mini-masterpieces  | /intl/en-in/products/platforms/#android            |
            | Australia’s non-profits    | /intl/en-au/products/android-chrome-more/          |
            | Google’s                   | /intl/en-ca/products/cloud/                        |
            | téléphone                  | /intl/fr-ca/produits/explorez-obtenez-des-reponses/|
            | desinformação              | /intl/pt-br/produtos/explore-e-encontre-respostas/ |

    @search-category-mobile
    Scenario Outline: Test search results when there are no results on a category page on mobile
        Given a user is at the <keyword> site on <mobile>
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search      | keyword                                            | language |
            | zwischen            | /technology/                                       | en       |
            | riqueza             | /intl/de-de/produkte/android-chrome-mehr/#android  | de       |
            | Themenverwandte     | /intl/en-in/products/platforms/#android            | en       |
            | Datenaustausch      | /intl/en-au/products/android-chrome-more/          | en       |
            | jeunes              | /intl/en-ca/products/cloud/                        | en       |
            | Themenverwandte     | /intl/fr-ca/produits/explorez-obtenez-des-reponses/| fr       |
            | Datenaustausch      | /intl/pt-br/produtos/explore-e-encontre-respostas/ | pt       |
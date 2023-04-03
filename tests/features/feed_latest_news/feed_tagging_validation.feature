# Created by machadoca at 7/02/22
Feature: As a user, I want to confirm articles in the feed list are shown to the user according to the corresponding tag

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed on the homepage are tagged accordingly
        Given a user is at the <keyword> site
        When the user scrolls to the feed in <keyword> locale
        Then the system shows articles in the <keyword> locale

        Examples:
            | keyword           |
            | /                 |
            | /intl/de-de/      |
            | /intl/en-au/      |
            | /intl/en-in/      |
            | /intl/fr-ca/      |
            | /intl/en-ca/      |
            | /intl/pt-br/      |
            | /intl/es-419/     |
            | /intl/it-it/      |
            | /intl/en-africa/  |
            | /intl/ar-mena/    |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed in the category page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated match with the content in the <keyword>
        Examples:
           | keyword                                                       |
           | /technology/                                                  |
           | /intl/de-de/produkte/android-chrome-mehr/#android             |
           | /intl/en-in/products/platforms/#android                       |
           | /intl/en-au/products/android-chrome-more/                     |
           | /intl/fr-ca/produits/explorez-obtenez-des-reponses/           |
           | /intl/en-ca/products/explore-get-answers/                     |
           | /intl/pt-br/produtos/android-chrome-play/                     |
           | /intl/es-419/actualizaciones-de-producto/android-chrome-play/ |
           | /intl/it-it/prodotti/android-chrome-play/                     |
           | /intl/ar-mena/products/android-chrome-play/                   |
           | /intl/en-africa/products/android-chrome-play/#googleplay      |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed on the subcategory page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated match with the content in the <keyword>
        Examples:
            | keyword               |
            | /products/android/    |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed in a series page are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated match with the content in the <keyword>
        Examples:
           | keyword                       |
           | /inside-google/talks-google/  |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed on a perspective landing page are tagged accordingly
        Given a user is at the <keyword> site
        When the user scrolls to the feed in <keyword> locale
        Then the system shows articles in the <keyword> locale
        Examples:
           | keyword                  |
           | /authors/sundar-pichai/  |

    @feed-article-tagging
    Scenario Outline: Test articles listed in the feed in a sitespace are tagged accordingly
        Given a user is at the <keyword> site
        When the user chooses a random article
        Then the tags associated match with the content in the <keyword>
        Examples:
           | keyword                       |
           | /waze/                        |
           | /products/marketingplatform/  |

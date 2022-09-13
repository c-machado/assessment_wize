# Created by machadoca at 10/03/22
Feature: As a user I want to confirm related articles tags are matching the current article

    @article-related
    Scenario Outline: Test the related articles tags are associated to the current article
        Given a user is at the <keyword> site
        When the user scrolls to the related stories section
        Then the user sees articles matching tags in current article

     Examples:
            | keyword                                                                       |
            | /products/search/how-were-improving-search-results-when-you-use-quotes/       |
            | /products/android/android-13/                                                 |
            | /outreach-initiatives/diversity/international-womens-day-2022/                |
            | /intl/de-de/unternehmen/inside-google/unterstuetzung-fuer-die-ukraine/            |
            | /intl/en-in/company-news/technology/empowering-women-speak-solutions/             |
            | /intl/en-ca/company-news/inside-google/supporting-communities-across-canada-2021/ |
            | /intl/en-au/company-news/outreach-initiatives/digital-future-initiative/          |
            | /intl/fr-ca/nouvelles/impact-initiatives/notre-soutien-aux-collectivites-du-canada-en-2021/ |
            | /intl/pt-br/produtos/explore-e-encontre-respostas/apresentamos-novas-ferramentas-para-ajudar-hoteis-na-retomada-do-turismo/ |
            | /intl/it-it/notizie-aziendali/iniziative/nuove-possibilita-di-scelta-dei-cookie-in-europa/|
            | /intl/es-419/noticias-de-la-empresa/iniciativas/una-nueva-ronda-del-innovation-challenge-en-latinoamerica/|

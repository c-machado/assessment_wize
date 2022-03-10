# Created by machadoca at 9/03/22
Feature: As a user I want to be sure links within the article are accessible

    @article-inline
    Scenario Outline: Test the links in the paragraph are opened according to the domain
        Given a user is at the <keyword> site
        Then all links are marked with the target property accordingly
        And all links redirects to an existing page


     Examples:
            | keyword                                                                                                 |
            | /outreach-initiatives/diversity/international-womens-day-2022/                                          |
            | /intl/de-de/unternehmen/inside-google/unterstuetzung-fuer-die-ukraine/                                  |
            | /intl/en-in/company-news/technology/empowering-women-speak-solutions/                                   |
            | /intl/en-ca/company-news/inside-google/supporting-communities-across-canada-2021/                       |
            | /intl/en-au/company-news/outreach-initiatives/digital-future-initiative/                                |
            | /intl/pt-br/novidades/iniciativas/mulheres-do-google-brasil-conheca-naiara-rocha-gerente-de-diversidade/|


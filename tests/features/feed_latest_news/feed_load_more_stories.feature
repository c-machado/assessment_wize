# Created by machadoca at 1/02/22
Feature: As a user I want to confirm articles in the feed list are shown to the user order by descendent date

    @feed-article-load-more
    Scenario Outline: Test articles listed in the homepage's feed are order by desc date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
            | keyword      |
            | /            |
            | /intl/de-de/ |
            | /intl/en-au/ |
            | /intl/en-in/ |

    @feed-article-load-more
    Scenario Outline: Test articles listed in the feed in the category page are order by desc date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
           | keyword                                           |
           | /technology/                                      |
           | /intl/de-de/produkte/android-chrome-mehr/#android |
           | /intl/en-in/products/platforms/#android           |
           | /intl/en-au/products/android-chrome-more/         |

    @feed-article-load-more
    Scenario Outline: Test articles listed in the feed in a series page are order by desc date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
           | keyword                               |
           | /inside-google/googlers/she-word/     |

    @feed-article-load-more-author-ids
    Scenario Outline: Test articles listed in the feed in a perspective landing page are order by desc date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
           | keyword                         |
           | /perspectives/sundar-pichai/    |

    @feed-article-load-more
    Scenario Outline: Test articles listed in the feed in a sitespace are order by desc date
        Given a user is at the <keyword> site
        When the user clicks on load more stories cta
        Then the articles are shown order by date desc
        Examples:
           | keyword   |
           | /waze/    |
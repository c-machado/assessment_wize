# Created by machadoca at 17/11/21
Feature: As a user I would like to interact with the footer links

  Examples:
      |keyword           |
      |/                 |
      |/intl/de-de/      |
      |/intl/en-au/      |

  @keyword-test
  Scenario Outline: Open social media links in new tab
    Given a user is at the <keyword> site
    When I click on every <social_media> item
    Then the user is redirected to <url>
    Examples:
      |social_media   |url                         |
      |instagram      |https://www.instagram.com/  |
      |twitter        |https://twitter.com/        |
      |youtube        |https://www.youtube.com/    |
      |facebook       |https://www.facebook.com/   |
      |linkedin       |https://www.linkedin.com/   |

  @keyword-test
  Scenario: Open legal links
    Given a user is at the <keyword> site
    When I click on legal items
    Then the user sees the url according to <keyword> locale


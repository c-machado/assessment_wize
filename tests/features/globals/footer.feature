# Created by machadoca at 17/11/21
Feature: As a user I would like to access the content in the footer

  Examples:
      |keyword           |
      |/                 |
      |/intl/de-de/      |
      |/intl/en-au/      |
      |/intl/en-in/      |

  @footer
  Scenario Outline: Test social media links are not broken and open in a new tab
    Given a user is at the <keyword> site
    When the user clicks on every <social_media> item
    Then the user is redirected to <url> in a new tab
    Examples:
      |social_media   |url                         |
      |instagram      |https://www.instagram.com/  |
      |twitter        |https://twitter.com/        |
      |youtube        |https://www.youtube.com/    |
      |facebook       |https://www.facebook.com/   |
      |linkedin       |https://www.linkedin.com/   |

  @footer
  Scenario: Test legal links are not broken
    Given a user is at the <keyword> site
    When the user clicks on legal items
    Then the user sees the url according to <keyword> locale

  @footer
  Scenario Outline: Test language selector contains expected locales
    Given a user is at the <keyword> site
    When the user clicks on language selector
    Then the system displays the selector with the corresponding <locale>
    Examples:
      |locale               |
      |English              |
      |Deutsch              |
      |English (India)      |
      |English (Australia)  |

  @footer
  Scenario Outline: Test Google link is not broken
    Given a user is at the <keyword> site
    When the user clicks the Google logo
    Then the user is redirected to <url> in a new tab
    Examples:
      |url                     |
      |https://www.google.com  |


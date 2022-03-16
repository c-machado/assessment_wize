# Created by machadoca at 17/11/21
Feature: As a user, I would like to access the content in the footer

  Examples:
      |keyword           |
      |/                 |
      |/intl/de-de/      |
      |/intl/en-au/      |
      |/intl/en-in/      |
      |/intl/en-ca/      |
      |/intl/fr-ca/      |
      |/intl/pt-br/      |

  @footer
  # TODO: facebook urls are not secure (locales: in & au) https://jira.hugeinc.com/browse/UNI-5897
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
    Then the user sees the URL according to <keyword> locale

  @footer1
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
      |English (Canada)     |
      |French (Canada)      |
      |Portuguese (Brazil)  |

  @footer1
  Scenario Outline: Test Google link is not broken
    Given a user is at the <keyword> site
    When the user clicks the Google logo
    Then the user is redirected to <url> in a new tab
    Examples:
      |url                     |
      |https://www.google.com  |


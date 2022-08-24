# Created by machadoca at 17/11/21
Feature: As a user, I would like to access the content in the footer

  Examples:
      |keyword                |
      |/                      |
      |/intl/de-de/           |
      |/intl/en-au/           |
      |/intl/en-in/           |
      |/intl/en-ca/           |
      |/intl/en-africa/       |
      |/intl/fr-ca/           |
      |/intl/pt-br/           |
      |/intl/es-419/          |
      |/intl/it-it/           |
      |/products/ads-commerce |
      |/waze/                 |


  @footer
  # TODO: facebook URLs are not secure (locales: in & au) https://jira.hugeinc.com/browse/UNI-5897
  Scenario: Test social media links are not broken
    Given a user is at the <keyword> site
    When the user clicks on every social media
    Then the system opens each link in a new tab
    And the system shows a secure url per each link

  @footer
  Scenario: Test legal links are not broken
    Given a user is at the <keyword> site
    When the user clicks on legal items
    Then the user sees the URL according to <keyword> locale

  @footer
  Scenario Outline: Test Google link is not broken
    Given a user is at the <keyword> site
    When the user clicks the Google logo
    Then the user is redirected to <url> in a new tab
    Examples:
      |url                     |
      |https://www.google.com  |

  @footer1
  Scenario: Test language selector contains expected locales
    Given a user is at the <keyword> site
    When the user clicks on every language in the selector
    Then the user can see all expected locales in the selector




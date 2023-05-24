# Created by machadoca at 17/11/21
Feature: As a user, I would like to access the content in the footer


  @footer_regression
  Scenario Outline: Test legal links are not broken
    Given a user is at the <keyword> site
    When the user clicks on legal items
    Then the user clicks on each URL according to <keyword> locale

    Examples:
      |keyword                |
      |/                      |
      |/intl/de-de/           |
      |/intl/en-au/           |
      |/intl/en-in/           |
      |/intl/en-ca/           |
      |/intl/fr-ca/           |
      |/intl/pt-br/           |
      |/intl/es-419/          |
      |/intl/it-it/           |
      |/intl/ar-mena/         |
      |/intl/en-africa/       |
      |/intl/fr-fr/           |
      |/products/ads-commerce |
      |/waze/                 |

  @footer_business_critical
  Scenario Outline: Test Google link is not broken
    Given a user is at the <keyword> site
    When the user clicks the Google logo
    Then the user is redirected to <url> in a new tab
    Examples:
      |keyword                |url                     |
      |/                      |https://www.google.com  |
      |/intl/de-de/           |https://www.google.com  |
      |/intl/en-au/           |https://www.google.com  |
      |/intl/en-in/           |https://www.google.com  |
      |/intl/en-ca/           |https://www.google.com  |
      |/intl/fr-ca/           |https://www.google.com  |
      |/intl/pt-br/           |https://www.google.com  |
      |/intl/es-419/          |https://www.google.com  |
      |/intl/it-it/           |https://www.google.com  |
      |/intl/ar-mena/         |https://www.google.com  |
      |/intl/en-africa/       |https://www.google.com  |
      |/intl/fr-fr/           |https://www.google.com  |
      |/products/ads-commerce |https://www.google.com  |
      |/waze/                 |https://www.google.com  |

  @footer_business_critical
  Scenario Outline: Test language selector redirect to the corresponding homepage
    Given a user is at the <keyword> site
    When the user clicks on <language> in the selector
    Then the user can see the homepage per <language>

  Examples:
      |language              |keyword           |
      | Deutsch              |/intl/de-de/      |
      | English              |/                 |
      | English (Africa)     |/intl/fr-ca/      |
      | English (India)      |/intl/en-in/      |
      | English (Australia)  |/intl/en-au/      |
      | English (Canada)     |/intl/en-ca/      |
      | Français (Canada)    |/intl/fr-ca/      |
      | Français (France)    |/intl/fr-fr/      |
      | Português (Brasil)   |/intl/pt-br/      |
      | Español (Latinoamérica)|/intl/es-419/   |
      | Italiano               |/intl/it-it/    |
      | اللغة العربية (MENA)   |/intl/ar-mena/  |

  @footer_regression
  # TODO: facebook URLs are not secure (locales: in & au) https://jira.hugeinc.com/browse/UNI-5897
  Scenario Outline: Test social media links are not broken
    Given a user is at the <keyword> site
    When the user clicks on every social media
    Then the system opens each link in a new tab
    And the system shows a secure url per each link

    Examples:
          |keyword                |
          |/                      |
          |/intl/de-de/           |
          |/intl/en-au/           |
          |/intl/en-in/           |
          |/intl/en-ca/           |
          |/intl/fr-ca/           |
          |/intl/pt-br/           |
          |/intl/es-419/          |
          |/intl/it-it/           |
          |/intl/ar-mena/         |
          |/intl/en-africa/       |
          |/intl/fr-fr/           |
          |/products/ads-commerce |
          |/waze/                 |
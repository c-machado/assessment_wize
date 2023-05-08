# Created by machadoca at 4/01/22
Feature: As a user, I want to interact with the cookie banner

    @cookie
    Scenario Outline: Test the cookie banner displaying
        Given a user is at the <keyword> site
        And the system displays the cookie banner per <language>
        When the user clicks on see details CTA
        Then the user is redirected in a new tab to <url>

        Examples:
          |keyword           | url                                                        | language |
          |/                 | https://policies.google.com/technologies/cookies           | en       |
          |/intl/de-de/      | https://policies.google.com/technologies/cookies?hl=de     | de       |
          |/intl/en-au/      | https://policies.google.com/technologies/cookies           | en       |
          |/intl/en-in/      | https://policies.google.com/technologies/cookies           | en       |
          |/intl/fr-ca/      | https://policies.google.com/technologies/cookies?hl=fr     | fr       |
          |/intl/pt-br/      | https://policies.google.com/technologies/cookies?hl=pt-BR  | pt       |
          |/intl/en-ca/      | https://policies.google.com/technologies/cookies           | en       |
          |/intl/es-419/     | https://policies.google.com/technologies/cookies?hl=es     | es       |
          |/intl/it-it/      | https://policies.google.com/technologies/cookies?hl=it     | it       |
          |/intl/en-africa/  | https://policies.google.com/technologies/cookies           | en       |
          |/intl/ar-mena/    | https://policies.google.com/technologies/cookies?hl=ar     | ar       |
          |/intl/fr-fr  /    | https://policies.google.com/technologies/cookies?hl=fr     | fr       |

    @cookie
    Scenario Outline: Test the cookie banner displayed on an article page
        Given a user is at the <keyword> site
        And the user clicks on the hero article
        And the system displays the cookie banner per <language>
        When the user clicks on see details CTA
        Then the user is redirected in a new tab to <url>

        Examples:
          |keyword           | url                                                        | language |
          |/                 | https://policies.google.com/technologies/cookies           | en       |
          |/intl/de-de/      | https://policies.google.com/technologies/cookies?hl=de     | de       |
          |/intl/en-au/      | https://policies.google.com/technologies/cookies           | en       |
          |/intl/en-in/      | https://policies.google.com/technologies/cookies           | en       |
          |/intl/fr-ca/      | https://policies.google.com/technologies/cookies?hl=fr     | fr       |
          |/intl/pt-br/      | https://policies.google.com/technologies/cookies?hl=pt-BR  | pt       |
          |/intl/en-ca/      | https://policies.google.com/technologies/cookies           | en       |
          |/intl/es-419/     | https://policies.google.com/technologies/cookies?hl=es     | es       |
          |/intl/it-it/      | https://policies.google.com/technologies/cookies?hl=it     | it       |
          |/intl/en-africa/  | https://policies.google.com/technologies/cookies           | en       |
          |/intl/ar-mena/    | https://policies.google.com/technologies/cookies?hl=ar     | ar       |
          |/intl/fr-fr  /    | https://policies.google.com/technologies/cookies?hl=fr     | fr       |

    @cookie
    Scenario Outline: Test the user can close the cookie banner
        Given a user is at the <keyword> site
        And the user clicks in the Ok cta
        Then the cookie banner is not displayed
        Examples:
            |keyword         |
            |/               |
            |/intl/de-de/    |
            |/intl/en-au/    |
            |/intl/en-in/    |
            |/intl/fr-ca/    |
            |/intl/pt-br/    |
            |/intl/en-ca/    |
            |/intl/es-419/   |
            |/intl/it-it/    |
            |/intl/en-africa/|
            |/intl/ar-mena/  |
            |/intl/fr-fr/    |
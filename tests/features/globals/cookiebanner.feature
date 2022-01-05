# Created by machadoca at 4/01/22
Feature: As a user I want to interact with the cookie banner

    @cookie
    Scenario Outline: Test the cookie banner displaying
        Given a user is at the <keyword> site
        And the system displays the cookie banner per <language>
        When the user clicks the see details CTA
        Then the user is redirected to <url> in a new tab

        Examples:
          |keyword           | url                                                    | language |
          |/                 | https://policies.google.com/technologies/cookies       | en       |
          |/intl/de-de/      | https://policies.google.com/technologies/cookies?hl=de | de       |
          |/intl/en-au/      | https://policies.google.com/technologies/cookies       | en       |
          |/intl/en-in/      | https://policies.google.com/technologies/cookies       | en       |

    @cookie
    Scenario Outline: Test the cookie banner displaying in an article page
        Given a user is at the <keyword> site
        And the user clicks in the hero article
        And the system displays the cookie banner per <language>
        When the user clicks the see details CTA
        Then the user is redirected to <url> in a new tab

        Examples:
          |keyword           | url                                                    | language |
          |/                 | https://policies.google.com/technologies/cookies       | en       |
          |/intl/de-de/      | https://policies.google.com/technologies/cookies?hl=de | de       |
          |/intl/en-au/      | https://policies.google.com/technologies/cookies       | en       |
          |/intl/en-in/      | https://policies.google.com/technologies/cookies       | en       |

    @cookie
    Scenario Outline: Test the user can close the cookie bannerr
        Given a user is at the <keyword> site
        And the user clicks in the Ok cta
        Then the cookie banner is not displayed
        Examples:
            |keyword         |
            |/               |
            |/intl/de-de/    |
            |/intl/en-au/    |
            |/intl/en-in/    |
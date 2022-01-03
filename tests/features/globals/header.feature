# Created by machadoca at 23/12/21
Feature: As a user I would like to interact with the header links

  @header
  Scenario Outline: Test link to product updates page
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      And the user on <keyword> clicks the CTA See all product updates
      Then the user is redirected to <url>
      Examples:
        |keyword           |url                    |submenu         |
        |/                 | /products/            |product_updates |
        |/intl/de-de/      | /intl/de-de/produkte/ |product_updates |
        |/intl/en-au/      | /intl/en-au/products/ |product_updates |
        |/intl/en-in/      | /intl/en-in/products/ |product_updates |


  @header
  Scenario Outline: Test the header items within products and company news submenus
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      Then every link in the <submenu> selected return an Http 200
      Examples:
        |keyword    | submenu         |
        |/          | product_updates |
        |/          | company_news    |

  @header
  Scenario Outline: Test the header cta's 'see all' within company submenu
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      Then every 'see all' CTA selected return an http 200
      Examples:
        |keyword    | submenu       |
        |/          | company_news  |

  @header
  Scenario Outline: Test the kebab menu
      Given a user is at the <keyword> site
      When the user triggers the kebab menu
      Then the user sees <kebab_option> according to <locale>

      Examples:
        |keyword      | kebab_option | locale |
        |/            | rss          | us     |
        |/            | press        | us     |
        |/intl/de-de/ | rss          | de     |
        |/intl/de-de/ | press        | de     |
        |/intl/en-au/ | rss          | au     |
        |/intl/en-au/ | press        | au     |
        |/intl/en-in/ | rss          | in     |
        |/intl/en-in/ | press        | in     |
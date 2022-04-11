# Created by machadoca at 5/04/22
Feature: As a user, I would like to interact with the header navigation on mobile

  @header-mobile
  Scenario Outline: Test link to product updates page on mobile
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
        |/intl/en-ca/      | /intl/en-ca/products/ |product_updates |
        |/intl/fr-ca/      | /intl/fr-ca/produits/ |product_updates |
        |/intl/pt-br/      | /intl/pt-br/produtos/ |product_updates |


  @header-mobile
  Scenario Outline: Test the header items within products and company news submenus
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      And the user clicks on each list in the <submenu>
      Then every link in the <submenu> selected return an Http 200
      Examples:
        |keyword    | submenu         |
        |/          | product_updates |
        |/          | company_news    |


  @header-mobile
  Scenario Outline: Test the header cta's 'see all' within the company submenu
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      And the user clicks on each list in the <submenu>
      Then every 'see all' CTA selected return an http 200
      Examples:
        |keyword    | submenu       |
        |/          | company_news  |


  @header-mobile
  Scenario Outline: Test navigation in sitespaces within products in Ads&Analytics list on mobile
      Given a user is at the <keyword> site
      When the user clicks on a random sitespace
      Then the system shows the updated header

      Examples:
      |keyword   |
      |/products |


  @header-mobile
  Scenario Outline: Test navigation in an article belonging to a sitespace on mobile
      Given a user is at the <keyword> site
      When the user clicks in an article in a <sitespace_tag> in <keyword>
      Then the system shows the <sitespace_title> nav menu in an article

      Examples:
      |keyword                 |sitespace_tag         |sitespace_title      |
      |/products/ads-commerce  |Google Ads & Commerce |Ads & Commerce Blog  |


  @header-mobile
  Scenario Outline: Test RSS matches the content on mobile
      Given a user is at the <keyword> site
      When the user triggers the hamburger menu
      And the user clicks on the RSS option
      Then the dates in RSS and <keyword> matches

      Examples:
        |keyword       |
        |/             |
        |/intl/de-de/  |
        |/intl/en-in/  |
        |/intl/en-au/  |
        |/intl/en-ca/  |
        |/intl/fr-ca/  |
        |/intl/pt-br/  |

  @header-mobile
  Scenario Outline: Test the keyword logo in the nav menu on mobile
      Given a user is at the <keyword> site
      And the user clicks on the hero article
      When the user clicks on the keyword logo
      Then the user is redirected to <url>

      Examples:
        |keyword      | url        |
        |/            | /          |
        |/intl/de-de/ |/intl/de-de/|
        |/intl/en-in/ |/intl/en-in/|
        |/intl/en-au/ |/intl/en-au/|
        |/intl/en-ca/ |/intl/en-ca/|
        |/intl/fr-ca/ |/intl/fr-ca/|
        |/intl/pt-br/ |/intl/pt-br/|
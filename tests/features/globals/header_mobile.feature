# Created by machadoca at 5/04/22
Feature: # Enter feature name here
  # Enter feature description here

  Examples:
    |mobile|
    |ios   |
#  @header-mobile
  Scenario Outline: Test RSS matches the content on mobile
      Given a user is at the <keyword> site on <mobile>
      When the user triggers the hamburger menu
      And the user clicks on the RSS option
      Then the dates in RSS and <keyword> matches

      Examples:
        |keyword       |
        |/             |
#        |/intl/de-de/  |
#        |/intl/en-in/  |
#        |/intl/en-au/  |
#        |/intl/en-ca/  |
#        |/intl/fr-ca/  |
#        |/intl/pt-br/  |

  @header-mobile
  Scenario Outline: Test link to product updates page
      Given a user is at the <keyword> site on <mobile>
      When the user triggers the hamburger menu
      And the user clicks on the <submenu>
      And the user on <keyword> clicks the CTA See all product updates
      Then the user is redirected to <url>
      Examples:
        |keyword           |url                    |submenu         |
        |/                 | /products/            |product_updates |
#        |/intl/de-de/      | /intl/de-de/produkte/ |product_updates |
#        |/intl/en-au/      | /intl/en-au/products/ |product_updates |
#        |/intl/en-in/      | /intl/en-in/products/ |product_updates |
#        |/intl/en-ca/      | /intl/en-ca/products/ |product_updates |
#        |/intl/fr-ca/      | /intl/fr-ca/produits/ |product_updates |
#        |/intl/pt-br/      | /intl/pt-br/produtos/ |product_updates |
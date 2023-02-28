# Created by machadoca at 5/04/22
Feature: As a user, I would like to interact with the header navigation on mobile

  @header_business_critical
      Scenario Outline: Test the latest stories submenu
          Given a user is at the <keyword> site
          And the user clicks on the hero article
          When the user clicks on the <submenu>
          Then the user is redirected to <keyword>
          Examples:
            |keyword      | submenu         |
            |/            | latest_stories  |
#            |/intl/de-de/ | latest_stories  |
#            |/intl/en-au/ | latest_stories  |
#            |/intl/en-in/ | latest_stories  |
#            |/intl/en-ca/ | latest_stories  |
#            |/intl/fr-ca/ | latest_stories  |
#            |/intl/pt-br/ | latest_stories  |
#            |/intl/es-419/| latest_stories  |
#            |/intl/it-it/ | latest_stories  |
#            |/intl/ar-mena/ | latest_stories  |

  @header_business_critical
  Scenario Outline: Test the header items within products and company news submenus on mobile
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      And the user clicks on each list in the <submenu>
      Then every link in the <submenu> selected return an Http 200
      Examples:
        |keyword    | submenu         |
        |/          | product_updates |
#        |/          | company_news    |
#
  @header_business_critical
  Scenario Outline: Test RSS matches the content on mobile
      Given a user is at the <keyword> site
      When the user triggers the hamburger menu
      And the user clicks on the RSS option
      Then the dates in RSS and <keyword> matches

      Examples:
        |keyword           |
        |/                 |
#        |/intl/de-de/      |
#        |/intl/en-in/      |
#        |/intl/en-au/      |
#        |/intl/en-ca/      |
#        |/intl/fr-ca/      |
#        |/intl/pt-br/      |
#        |/intl/es-419/     |
#        |/intl/it-it/      |
#        |/intl/ar-mena/    |
##        |/intl/en-africa/  |
#
  @header_business_critical
  Scenario Outline: Test navigation in sitespaces within products in Ads&Analytics list on mobile
      Given a user is at the <keyword> site
      When the user clicks on a random sitespace
      Then the system shows the updated header

      Examples:
      |keyword   |
      |/products |

  @header_business_critical
  Scenario Outline: Test navigation in waze sitespace
      Given a user is at the <keyword> site
      Then the system shows the waze header

      Examples:
      |keyword   |
      |/waze     |

  @header_business_critical
  Scenario Outline: Test navigation in an article belonging to a sitespace on mobile
      Given a user is at the <keyword> site
      When the user clicks in an article in a <sitespace_tag> in <keyword>
      Then the system shows the <sitespace_title> nav menu in an article

      Examples:
      |keyword                 |sitespace_tag         |sitespace_title      |
      |/products/ads-commerce  |Google Ads & Commerce |Ads & Commerce Blog  |


  @header_business_critical
  Scenario Outline: Test the keyword logo in the nav menu on mobile
      Given a user is at the <keyword> site
      And the user clicks on the hero article
      When the user clicks on the main logo
      Then the user is redirected to <keyword>

      Examples:
        |keyword          |
        |/                |
#        |/intl/de-de/     |
#        |/intl/en-in/     |
#        |/intl/en-au/     |
#        |/intl/en-ca/     |
#        |/intl/fr-ca/     |
#        |/intl/pt-br/     |
#        |/intl/es-419/    |
#        |/intl/it-it/     |
#        |/intl/ar-mena/   |
##        |/intl/en-africa/ |
#
  @header-regression
  Scenario Outline: Test link to product updates page on mobile
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      And the user on <keyword> clicks the CTA See all product updates
      Then the user is redirected to <url>
      Examples:
        |keyword           |url                                        |submenu         |
        |/                 | /products/                                |product_updates |
#        |/intl/de-de/      | /intl/de-de/produkte/                     |product_updates |
#        |/intl/en-au/      | /intl/en-au/products/                     |product_updates |
#        |/intl/en-in/      | /intl/en-in/products/                     |product_updates |
#        |/intl/en-ca/      | /intl/en-ca/products/                     |product_updates |
#        |/intl/fr-ca/      | /intl/fr-ca/produits/                     |product_updates |
#        |/intl/pt-br/      | /intl/pt-br/produtos/                     |product_updates |
#        |/intl/es-419/     | /intl/es-419/actualizaciones-de-producto/ |product_updates |
#        |/intl/it-it/      | /intl/it-it/prodotti/                     |product_updates |
#        |/intl/ar-mena/    | /intl/ar-mena/products/                   |product_updates |
##        |/intl/en-africa/  | /intl/en-africa/products/                 |product_updates |


  @header-regression
  Scenario Outline: Test the header cta's 'see all' within the company submenu on mobile
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      And the user clicks on each list in the <submenu>
      Then every 'see all' CTA selected return an http 200
      Examples:
        |keyword    | submenu       |
        |/          | company_news  |

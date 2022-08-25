# Created by machadoca at 23/12/21
Feature: As a user, I would like to interact with the header navigation on desktop


  #TODO: separate US which is the unique locale that contains the 'see all' CTA
  @header-desktop
  Scenario Outline: Test link to product updates page
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      And the user on <keyword> clicks the CTA See all product updates
      Then the user is redirected to <url>
      Examples:
        |keyword           |url                                        |submenu         |
        |/                 | /products/                                |product_updates |
        |/intl/de-de/      | /intl/de-de/produkte/                     |product_updates |
        |/intl/en-au/      | /intl/en-au/products/                     |product_updates |
        |/intl/en-in/      | /intl/en-in/products/                     |product_updates |
        |/intl/en-ca/      | /intl/en-ca/products/                     |product_updates |
        |/intl/fr-ca/      | /intl/fr-ca/produits/                     |product_updates |
        |/intl/pt-br/      | /intl/pt-br/produtos/                     |product_updates |
        |/intl/es-419/     | /intl/es-419/actualizaciones-de-producto/ |product_updates |
        |/intl/it-it/      | /intl/it-it/prodotti/                     |product_updates |
#        |/intl/en-africa/  | /intl/en-africa/products/                 |product_updates |


  @header-desktop
  Scenario Outline: Test the header items within products and company news submenus
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      Then every link in the <submenu> selected return an Http 200
      Examples:
        |keyword    | submenu         |
        |/          | product_updates |
        |/          | company_news    |


  @header-desktop
  Scenario Outline: Test the header cta's 'see all' within the company submenu
      Given a user is at the <keyword> site
      When the user clicks on the <submenu>
      Then every 'see all' CTA selected return an http 200
      Examples:
        |keyword    | submenu       |
        |/          | company_news  |

  #TODO: separate RSS options and add assertion on the HTTP status
  @header-desktop
  Scenario Outline: Test options in the kebab menu
      Given a user is at the <keyword> site
      When the user triggers the kebab menu
      Then the user sees <kebab_option> according to <language>

      Examples:
        |keyword      | kebab_option | language |
        |/            | rss          | en       |
        |/            | press        | en       |
        |/intl/de-de/ | rss          | de       |
        |/intl/de-de/ | press        | de       |
        |/intl/en-au/ | rss          | en       |
        |/intl/en-au/ | press        | en       |
        |/intl/en-in/ | rss          | en       |
        |/intl/en-in/ | press        | en       |
        |/intl/en-ca/ | rss          | en       |
        |/intl/en-ca/ | press        | en       |
        |/intl/fr-ca/ | rss          | en       |
        |/intl/fr-ca/ | press        | fr_ca    |
        |/intl/pt-br/ | rss          | en       |
        |/intl/pt-br/ | press        | pt_br    |
        |/intl/es-419/| rss          | en       |
        |/intl/es-419/| press        | es_419   |
        |/intl/it-it/ | rss          | en       |
        |/intl/it-it/ | press        | it_it    |
#        |/intl/en-africa/  | rss     | en       |
#        |/intl/en-africa/  | press   | en       |

  @header-desktop
  #TODO: add a new case sitespace and subcategory in en-us
  #TODO: add a comparison between 5 first articles
  Scenario Outline: Test RSS matches the content on desktop
      Given a user is at the <keyword> site
      When the user triggers the kebab menu
      And the user clicks <kebab_option>
      Then the dates in RSS and <keyword> matches

      Examples:
        |keyword      | kebab_option |
        |/            | rss          |
        |/intl/de-de/ | rss          |
        |/intl/en-au/ | rss          |
        |/intl/en-in/ | rss          |
        |/intl/en-ca/ | rss          |
        |/intl/fr-ca/ | rss          |
        |/intl/pt-br/ | rss          |
        |/intl/es-419/| rss          |
        |/intl/it-it/ | rss          |
#        |/intl/en-africa/ | rss      |

  @header-desktop
  Scenario Outline: Test the keyword logo in the nav menu
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
        |/intl/es-419/|/intl/es-419/|
        |/intl/it-it/ |/intl/it-it/|
#        |/intl/en-africa/ |/intl/en-africa/|

  @header-desktop
  Scenario Outline: Test navigation in sitespaces within products in Ads&Analytics list
      Given a user is at the <keyword> site
      When the user clicks on a random sitespace
      Then the system shows the updated header

      Examples:
      |keyword   |
      |/products |

  @header-desktop
  Scenario Outline: Test navigation in waze sitespace
      Given a user is at the <keyword> site
      Then the system shows the waze header

      Examples:
      |keyword   |
      |/waze     |

  @header-desktop
  Scenario Outline: Test navigation in an article belonging to a sitespace
      Given a user is at the <keyword> site
      When the user clicks in an article in a <sitespace_tag> in <keyword>
      Then the system shows the <sitespace_title> nav menu in an article

      Examples:
      |keyword                 |sitespace_tag         |sitespace_title      |
      |/products/ads-commerce  |Google Ads & Commerce |Ads & Commerce Blog  |
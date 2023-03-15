# Created by machadoca at 6/01/22
#Search functionality works as follows:
#Suggestions: Look for the content that matches the article's title.
#Results page: Look within the article's content.
#The results appeared order by relevance, that may cause the oldest content be shown at the top.
Feature: As a user, I want to be able to search for content within the blog


    @search_nav_business_critical
    Scenario Outline: Test the search bar  - expanding the search bar
        Given a user is at the <keyword> site
        When the user clicks the search icon
        Then the system shows the search bar expanded

    Examples:
         |keyword         |
         |/               |
         |/intl/de-de/    |
         |/intl/en-in/    |
         |/intl/en-au/    |
         |/intl/fr-ca/    |
         |/intl/pt-br/    |
         |/intl/en-ca/    |
         |/intl/en-africa/|
         |/intl/es-419/   |
         |/intl/it-it/    |
         |/intl/ar-mena/    |


    @search_nav_business_critical
    Scenario Outline: Test the search bar  - collapsing the search bar
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user closes the search bar
        Then the system collapsed the search bar

    Examples:
         |keyword         |
         |/               |
         |/intl/de-de/    |
         |/intl/en-in/    |
         |/intl/en-au/    |
         |/intl/fr-ca/    |
         |/intl/pt-br/    |
         |/intl/en-ca/    |
         |/intl/en-africa/|
         |/intl/es-419/   |
         |/intl/it-it/    |
         |/intl/ar-mena/    |


#    @search_nav_business_critical
    Scenario Outline: Test the results page
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system adds the <text_to_search> as a parameter in the <keyword> url

        Examples:
         |keyword         |text_to_search|
         |/               |google        |
         |/intl/de-de/    |android       |
         |/intl/en-in/    |youtube       |
         |/intl/en-au/    |maps          |
         |/intl/fr-ca/    |entrepreneurs |
         |/intl/pt-br/    |translate     |
         |/intl/en-ca/    |ai            |
         |/intl/en-africa/|africa        |
         |/intl/es-419/   |buscador      |
         |/intl/it-it/    |pixel         |
         |/intl/ar-mena/  |youtube       |


    @search_nav_business_critical
    Scenario Outline: Test filter by random tag in the results page
        Given a user is at the <keyword> site
        When the user clicks the search icon
        And the user types the <text_to_search>
        And  the user clicks the magnifying glass
        And the user selects a random filter
        Then the system filters the results on <keyword>

        Examples:
         |keyword         |text_to_search|
         |/               |google        |
         |/intl/de-de/    |android       |
         |/intl/en-in/    |youtube       |
         |/intl/en-au/    |maps          |
         |/intl/fr-ca/    |entrepreneurs |
         |/intl/pt-br/    |translate     |
         |/intl/en-ca/    |ai            |
         |/intl/en-africa/|africa        |
         |/intl/es-419/   |buscador      |
         |/intl/it-it/    |pixel         |
         |/intl/ar-mena/  |youtube       |
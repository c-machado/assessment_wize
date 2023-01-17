# Created by machadoca at 18/04/22
#Search functionality works as follows:
#Suggestions: Look for the content that matches the article's title.
#Results page: Look within the article's content.
#The results appeared order by relevance, that may cause the oldest content be shown at the top.
Feature: As a user, I want to search for content in the article progress bar

    @search_article_progress_bar
    Scenario Outline: Test search suggestions in an article page progress bar
        Given a user is at the <keyword> site
        And the progress bar is visible
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword       |
            | google         | /             |
            | sicherer       | /intl/de-de/  |
            | digital        | /intl/en-in/  |
            | australians    | /intl/en-au/  |
            | nouvelles      | /intl/fr-ca/  |
            | pessoas        | /intl/pt-br/  |
            | subsea         | /intl/en-ca/  |
            | privacidad     | /intl/es-419/ |
            | intelligente   | /intl/it-it/  |
            | كأس            | /intl/ar-mena/|


    @search_article_progress_bar
    Scenario Outline: Test the search suggestions in an article page progress bar using special characters
        Given a user is at the <keyword> site
        And the progress bar is visible
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search            | keyword       |
            | español                   | /             |
            | Privatsphäre              | /intl/de-de/  |
            | India’s mini-masterpieces | /intl/en-in/  |
            | Australia’s non-profits   | /intl/en-au/  |
            | l'Asie                    | /intl/fr-ca/  |
            | informações               | /intl/pt-br/  |
            | Canada's K-12             | /intl/en-ca/  |
            | año                       | /intl/es-419/ |
            | L'intrattenimento         | /intl/it-it/  |
            | الأشخاص                    | /intl/ar-mena/|


    @search_article_progress_bar
    Scenario Outline: Test search results in an article page progress bar
        Given a user is at the <keyword> site
        And the progress bar is visible
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword       |
            | google         | /             |
            | sicherer       | /intl/de-de/  |
            | digital        | /intl/en-in/  |
            | australians    | /intl/en-au/  |
            | nouvelles      | /intl/fr-ca/  |
            | pessoas        | /intl/pt-br/  |
            | subsea         | /intl/en-ca/  |
            | privacidad     | /intl/es-419/ |
            | intelligente   | /intl/it-it/  |
            | المحتوى        | /intl/ar-mena/|


    @search_article_progress_bar
    Scenario Outline: Test search results in an article page progress bar using special characters
        Given a user is at the <keyword> site
        And the progress bar is visible
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search            | keyword       |
            | Valentine's               | /             |
            | schützt                   | /intl/de-de/  |
            | Badshah’s #JugnuChallenge | /intl/en-in/  |
            | $1.89                     | /intl/en-au/  |
            | l'Asie                    | /intl/fr-ca/  |
            | informações               | /intl/pt-br/  |
            | Canada's K-12             | /intl/en-ca/  |
            | información               | /intl/es-419/ |
            | un’attività               | /intl/it-it/  |
            | الفرنسية                  | /intl/ar-mena/|


    @search_article_progress_bar
    Scenario Outline: Test search results when there are no results in an article page progress bar
        Given a user is at the <keyword> site
        And the progress bar is visible
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search            | keyword       | language |
            | zwischen                  | /             | en       |
            | riqueza                   | /intl/de-de/  | de       |
            | Themenverwandte           | /intl/en-in/  | en       |
            | Datenaustausch            | /intl/en-au/  | en       |
            | sondern                   | /intl/pt-br/  | pt       |
            | pesquisa                  | /intl/fr-ca/  | fr       |
            | retornou                  | /intl/en-ca/  | en       |
            | retornou                  | /intl/es-419/ | es       |
            | retornou                  | /intl/it-it/  | it       |
            | copa                      | /intl/ar-mena/| ar       |


    @search_article_progress_bar
    Scenario Outline: Test the search suggestions in a perspective's article progress bar using special characters
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search    | keyword                       |
            | español           | /perspectives/sundar-pichai/  |

    @search_article_progress_bar
    Scenario Outline: Test search suggestions in a perspectives article page progress bar
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        When the user clicks the search icon
        And the user types the <text_to_search>
        Then the system shows suggestions per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                      |
            | google         | /perspectives/sundar-pichai/ |


    @search_article_progress_bar
    Scenario Outline: Test search results in a perspective's article progress bar
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search | keyword                      |
            | google         | /perspectives/sundar-pichai/ |


    @search_article_progress_bar
    Scenario Outline: Test search results in a perspective's article progress bar using special characters
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows results per <text_to_search> in <keyword> page

     Examples:
            | text_to_search  | keyword                      |
            | Valentine's     | /perspectives/sundar-pichai/ |


    @search_article_progress_bar
    Scenario Outline: Test search results when there are no results in a perspective's article progress bar
        Given a user is at the <keyword> site
        And the user selects an article in <keyword> feed
        And the user scroll to see the progress bar
        When the user clicks the search icon
        And the user types the <text_to_search>
        And the user clicks the magnifying glass
        Then the system shows msg per <text_to_search> in corresponding <language>

     Examples:
            | text_to_search   | keyword                         | language |
            | zwischen         | /perspectives/sundar-pichai/    | en       |
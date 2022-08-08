# Created by machadoca at 6/06/22
#Feature: As a user, I want to update the content the user should seen when clicks on a specific content
#
#    Examples:
#    |keyword |
#    |/high-five/bird-flies-bar-and-other-top-searches-week  |
#
#    @redirects
#    Scenario: Test redirects in CMS setting in the staging environment
#        Given a user is at the <keyword> site
#        Then the user gets a 400 error
#        And the user is redirected to <url>
#    Examples:
#    | url_from                                               |
#    | /high-five/bird-flies-bar-and-other-top-searches-week  |
#        |/high-five/high-five-courtside-seats-comey-nba-sesame-snack-madrid  |/products/search/high-five-courtside-seats-comey-nba-sesame-snack-madrid/|
#        |/google-20  |/inside-google/life-at-google/google-20/|
#        |/google-20  |/inside-google/life-at-google/google-20/|
#        |/high-five/high-five-least-taxing-thing-youll-read-all-week  |/products/search/high-five-least-taxing-thing-youll-read-all-week/|
#        |/about  |/inside-google/company-announcements/about/|
#        |/app-ads  |/products/ads-commerce/|
#        |/asia-pacific-internet-entrepreneurs  |/around-the-globe/google-asia/asia-pacific-internet-entrepreneurs/|

#    Scenario Outline: Test redirects in CMS setting in the production environment
#        Given a user is at the <keyword> site
#        When the user navigates to <previous_page>
#        Then the user gets a 400 error
#
#        Examples:
#
#        |previous_page                                          | current_page                                               |
#
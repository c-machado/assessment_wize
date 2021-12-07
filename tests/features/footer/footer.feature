# Created by machadoca at 17/11/21
Feature: As a user I would like to interact with the footer links

#  Examples:
#      |keyword           |
###      |chrome/           |
##      |/                 |
#      |/intl/de-de/       |
##      |/intl/en-au/       |

  @keyword-test
  Scenario Outline: Test
    Given a user is at the <keyword> site
    When I click on every social media item
    Examples:
      |keyword           |
##      |chrome/           |
      |/                 |
#      |/intl/de-de/       |
#      |/intl/en-au/       |
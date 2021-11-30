# Created by machadoca at 17/11/21
Feature: As a user I would like to interact with the footer links

  Examples:
      |keyword           |
#      |chrome/           |
      |/                 |
      |/intl/de-de/       |
      |/intl/en-au/       |


  Scenario Outline: Test
    Given a user is at the <keyword> site on <platform>, <web_browser> and <viewport>
    When I click on every social media item

     Examples: Vertical
         | platform     | MAC       | WIN10   | ANDROID |
         | web_browser  | chrome    | ie      | chrome  |
         | viewport     | desktop   | desktop | mobile  |


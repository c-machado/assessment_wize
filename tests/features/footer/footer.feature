# Created by machadoca at 17/11/21
Feature: As a user I would like to interact with the footer links

  Examples:
      |keyword           |
      |/                 |
#      |intl/de-de/       |
#      |intl/en-au/       |


  Scenario Outline: Test
    Given a user is at the <keyword> site on <platform> and <web_browser>
    When I click on every social media item

     Examples: Vertical
         | platform     | MAC       |
         | web_browser  | chrome    |
#         | keyword      | /         |
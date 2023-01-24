# Created by machadoca at 31/03/22
#TODO: ADD VALIDATION TO TEST DOWNLOAD ASSET
Feature: As a user, I want to be able to filter the assets as needed

    Examples:
    |keyword |
    |/press  |

    @press1
    Scenario Outline: Test filter by type
        Given a user is at the <keyword> site
        When the user chooses the <type_filter>
        Then the system updates the grid with the <type_filter> in <keyword>

    Examples:
        |type_filter |
        |Headshots   |


    @press
    Scenario Outline: Test filter by type and product
        Given a user is at the <keyword> site
        When the user chooses the <type_filter>
        When the user chooses the <product_filter>
        Then the system updates the grid with the <type_filter> and <tag_filter> in <keyword>

    Examples:
        |type_filter    |product_filter | tag_filter |
        |Headshots      |Android        | Android    |
        |Life At Google |Translate      | Translate  |


    @press
    Scenario Outline: Test filter by type and topic
        Given a user is at the <keyword> site
        When the user chooses the <type_filter>
        When the user chooses the <topic_filter>
        Then the system updates the grid with the <type_filter> and <tag_filter> in <keyword>

    Examples:
        |type_filter    |topic_filter       | tag_filter         |
        |Headshots      |Arts & Culture     | Arts & Culture     |
        |Logos          |Accessibility      | Accessibility      |
        |Life At Google |Google in Asia     | Google in Asia     |
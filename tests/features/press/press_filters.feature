# Created by machadoca at 31/03/22
Feature: As a user, I want to be able to filter the assets as needed

    @press
    Scenario Outline: Test filter by type
        Given a user is at the <keyword> site
        When the user sets filter by type <type_filter>
        Then the system updates the grid with <type_filter> in <keyword>

    Examples:
        |type_filter |keyword |
        |Headshots   |/press  |


    @press
    Scenario Outline: Test filter by type and product
        Given a user is at the <keyword> site
        When the user sets filter by type <type_filter>
        When the user sets filter by product <product_filter>
        Then the system shows the grid with the <type_filter> and <tag_filter> in <keyword>

    Examples:
        |type_filter    |product_filter | tag_filter | keyword |
        |Headshots      |Android        | Android    | /press  |


    @press
    Scenario Outline: Test filter by type and topic
        Given a user is at the <keyword> site
        When the user sets filter by type <type_filter>
        When the user sets filter by topic <topic_filter>
        Then the system shows the grid with the <type_filter> and <tag_filter> in <keyword>

    Examples:
        |type_filter    |topic_filter       | tag_filter         |keyword |
        |Headshots      |Sustainability     | Sustainability     |/press  |

Feature: As a user I want to be able to search for an item on Amazon

    Scenario Outline: Test search for an item
        Given a user is at the homepage
        When the user types the <text_to_search>
        And the user clicks on the search icon
        Then the system shows the corresponding results
    Examples:
        |text_to_search|
        |adidas        |

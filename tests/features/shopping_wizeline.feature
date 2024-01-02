Feature: As a user I want to add an specific item and validate its correctly added

    @wizeline
    Scenario: Test to add  an item to the cart
        Given a user is at the homepage
        And the user is logged in
        When the user clicks on the CTA to add an item
        Then the system adds the item to the cart
        And the user navigates to the cart
        And the user confirms the correct item is added

# Created by machadoca at 5/01/22
Feature: As a user I would like to interact with the newsletter

 Examples:
        |keyword    |
        |/          |

  @newsletter
  Scenario: Test a user can complete the subscription from the header
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta
      And the user fills out the form
      And the user submits the information
      Then the system displays confirmation message

  @newsletter-stage
  Scenario: Test a user can complete the subscription from the toast
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta in the toast
      And the user fills out the form
      And the user submits the information
      Then the system displays confirmation message

  @newsletter
  Scenario: Test a user can close the newsletter modal from the header
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta
      And the user closes the modal
      Then the system hides the modal

  @newsletter-stage
  Scenario: Test a user can close the newsletter modal from the toast
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta in the toast
      And the user closes the modal
      Then the system hides the modal
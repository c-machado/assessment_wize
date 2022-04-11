# Created by machadoca at 5/01/22
Feature: As a user, I would like to interact with the newsletter

 Examples:
        |keyword    |
        |/          |

  @newsletter
  Scenario: Test a user can complete the subscription from the header
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta
      And the user fills out the form
      And the user submits the information
      Then the system displays a confirmation message

  @newsletter
  Scenario: Test a user can complete the subscription from the toast
      Given a user is at the <keyword> site
      And the toast bar has appeared
      When the user clicks on subscribe cta in the toast
      And the user fills out the form
      And the user submits the information
      Then the system displays a confirmation message

  @newsletter
  Scenario: Test a user can close the newsletter modal from the header
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta
      And the user closes the modal
      Then the system hides the modal

  @newsletter
  Scenario: Test a user can close the newsletter modal from the toast
      Given a user is at the <keyword> site
      And the toast bar has appeared
      When the user clicks on subscribe cta in the toast
      And the user closes the modal
      Then the system hides the modal

  @newsletter
  Scenario: Test the user sees an error with the invalid format
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta
      And the user fills out the form with invalid data
      Then the user sees an error message

  @newsletter
  Scenario: Test the user can choose to close the toast bar
      Given a user is at the <keyword> site
      And the toast bar has appeared
      When the user closes the toast bar
      Then the toast bar is not visible anymore


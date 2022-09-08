Feature: As a user, I would like to interact with the newsletter

 Examples:
        |keyword    |
        |/          |

  @standalone_newsletter
  Scenario: Test a user can complete the subscription from the header
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta on mobile
      And the user fills out the form
      And the user submits the information
      Then the system displays a confirmation message

  @standalone_newsletter
  Scenario: Test if the user sees an error with the invalid format from the standalone page
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta on mobile
      And the user fills out the form with invalid data
      Then the user sees an error message

  @standalone_newsletter
  Scenario: Test a user can complete the subscription from the sticky banner in the standalone
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta on mobile
      And the user scroll to see the progress bar
      And the user clicks on the subscribe cta in the sticky bar
      And the user fills out the email in the sticky bar
      And the user submits the information on the sticky
      Then the system displays a confirmation message on the sticky

   @standalone_newsletter
   Scenario: Test if the user sees an error with the invalid format in the sticky bar in the standalone
      Given a user is at the <keyword> site
      When the user clicks on subscribe cta on mobile
      And the user scroll to see the progress bar
      And the user clicks on the subscribe cta in the sticky bar
      And the user fills out the email on the sticky with invalid data
      Then the user sees an error message on sticky

  @toast_standalone_newsletter
  Scenario: Test a user can complete the subscription from the toast
      Given a user is at the <keyword> site
      And the toast bar has appeared
      When the user clicks on subscribe cta in the toast
      And the user fills out the form
      And the user submits the information
      Then the system displays a confirmation message

  @toast_standalone_newsletter
  Scenario: Test the user can choose to close the toast bar
      Given a user is at the <keyword> site
      And the toast bar has appeared
      When the user closes the toast bar
      Then the toast bar is not visible anymore

  @homepage_newsletter
  Scenario: Test a user can complete the subscription from the homepage
      Given a user is at the <keyword> site
      When the user fills out the form
      And the user submits the information
      Then the system displays a confirmation message on the homepage

  @homepage_newsletter
  Scenario: Test if the user sees an error with the invalid format on the homepage
      Given a user is at the <keyword> site
      When the user fills out the form with invalid data
      Then the user sees an error message


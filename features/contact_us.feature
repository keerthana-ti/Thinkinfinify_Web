Feature: Contact us functionality
  Scenario: Verify that the user is able to successfully submit the contact us form
    Given user is on the homepage
    When user clicks on contact menu it will open the pop-up of contact us
    And user enters the required details
    Then clicks on submit button
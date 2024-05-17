Feature: Login Success
  As a user
  I want to verify that login success with correct credentials

  Scenario: User successfully logs in with correct credentials
    Given I navigate to the login page
    When I enter correct username and password
    And I click on the submit button
    Then I should see the dashboard page
    Then I close the browser
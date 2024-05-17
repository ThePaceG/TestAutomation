Feature: Login Failure
  As a user
  I want to verify that login fails with incorrect credentials

  Scenario: Attempting to login with incorrect credentials
    Given I am on the login page
    When I enter incorrect username and password
    And I click on the login button
    Then I should see an error message
    Then I quit the browser
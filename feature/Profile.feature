Feature: Profile Management
  As a user
  I want to view and update my profile information

  Scenario: Update profile details
    Given I am logged in and on the profile page
    When I update my profile details
    And I save the changes
    Then I should see the updated profile details
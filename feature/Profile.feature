Feature: Profile Management
  As a user
  I want to view and update my profile information

  Scenario: View profile details
    Given I am logged in and on the profile page
    Then I should see my profile details

  Scenario: Update profile details
    Given I am logged in and on the profile page
    When I update my profile details
    And I save the changes
    Then I should see the updated profile details
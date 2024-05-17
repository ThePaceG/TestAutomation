Feature: Request Quotation
  As a user
  I want to request a quotation on the insurance website

  Scenario: Requesting a quotation
    Given I am on the insurance website
    When I click on the "Request Quotation" button
    And I fill out the quotation form
    And I click the submit
    Then I should see a confirmation message
    Then I remove the browser
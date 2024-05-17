Feature: Retrieve Quotation
  As a user
  I want to retrieve a quotation on the insurance website

  Scenario: User retrieves a quotation
    Given I am on the retrieve quotation page
    When I fill out the quotation retrieval form
    And I click the retrieve
    Then I should see the retrieved quotation detail
    Then I shut down the browser

Feature: Printing documents
  Scenario: Create a Markdown document
    Given a Markdown creator
    When I render the title Report
    Then the document is # Report

  Scenario: Send a document through the adapter
    Given an adapted mock printer
    When I send Report to the adapter
    Then the old printer receives Report

  Scenario: Use a student pricing strategy
    Given a student print order
    When I calculate the price of 17 pages
    Then the price is 51

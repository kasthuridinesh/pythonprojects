Feature: Pets store Application Automation
  Scenario: Sign up to the website
    Given user launches the pets store application
    When user clicks on the signin in the pets store application
    And user enters the valid username
    And user enters the valid password
    And user clicks on login button
    Then user validate the selected url
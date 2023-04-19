Feature: Stats screen
    Tests button control on stats screen

Scenario: Stat Screen Share Button
    Given I am on the stats screen
    When I press the share button
    Then the share stats graphic should be displayed

Scenario: Stat Screen Home Button
    Given I am on the stats screen
    When I press the home button
    Then the home screen should be displayed

Scenario: Stat Screen Quit Button
    Given I am on the stats screen
    When I press the quit button
    Then the application should close

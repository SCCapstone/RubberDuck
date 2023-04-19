Feature: Stats screen
    Tests button control on stats screen

Scenario: Stat Screen Share Button
    Given I am on the stats screen
    When I press the share button
    Then I should get a share dialog

Scenario: Stat Screen Home Button
    Given I am on the stats screen
    When I press the home button
    Then I should see the home screen

Scenario: Stat Screen Quit Button
    Given I am on the stats screen
    When I press the quit button
    Then I should see the quit dialog

Feature: High Score screen
    Tests if a player can use buttons to navigate and share

Scenario: High Score Screen - Play Button
    Given I am on the High Score screen
    When I press the Play button
    Then I should be on the Game screen

Scenario: High Score Screen - Share Button 
    Given I am on the High Score screen
    When I press the Share button
    Then I should be on the Share popup

Scenario: High Score Screen - Home Button
    Given I am on the High Score screen
    When I press the Home button
    Then I should be on the Home screen

  
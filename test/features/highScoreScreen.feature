Feature: High Score screen
    Tests if a player can use buttons to navigate the high score screen and share their high score

Scenario: High Score Screen - Play Again Button
    Given I am on the High Score screen
    When I press the Play Again button
    Then I should be on the Game screen

Scenario: High Score Screen - Share Button 
    Given I am on the High Score screen
    When I press the Share button
    Then I should see the Share Score graphic

Scenario: High Score Screen - Home Button
    Given I am on the High Score screen
    When I press the Home button
    Then I should be on the Home screen

  
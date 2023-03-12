Feature: GameOver screen
    Tests whether player can replay level, start a new game, access high scores, and share high scorefrom the GameOver screen

Scenario: Display Game Over screen with options
    Given the game has ended
    When the Game Over screen is displayed
    Then there should be four options available to the user
    And the users score should be displayed
    And the game time should be displayed

Scenario: Clicking "Replay Level" 
    Given the Game Over screen is displayed
    When the user clicks the "Replay Level" option
    Then the game should restart at the current level

Scenario: Clicking "New Game" 
    Given the Game Over screen is displayed
    When the user clicks the "New Game" option
    Then the game should restart from the beginning of the game

Scenario: Clicking "Share Score" 
    Given the Game Over screen is displayed
    When the user clicks the "Share Score" option
    Then the user should be prompted to share their score 

Scenario: Clicking "High Score Board" 
    Given the Game Over screen is displayed
    When the user clicks the "High Score Board" option
    Then the user should be taken to the High Score Board screen
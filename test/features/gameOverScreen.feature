Feature: GameOver screen
    Tests whether player can return home, start a new game, access high scores, and share high scorefrom the GameOver screen

Scenario: Clicking "Home" 
    Given the Game Over screen is displayed
    When the user clicks the "Home" option
    Then the user should be taken to the Home screen

Scenario: Clicking "New Game" 
    Given the Game Over screen is displayed
    When the user clicks the "New Game" option
    Then the game should restart from the beginning

Scenario: Clicking "Share Score" 
    Given the Game Over screen is displayed
    When the user clicks the "Share Score" option
    Then the Share Score Graphic should be displayed

Scenario: Clicking "High Score Board" 
    Given the Game Over screen is displayed
    When the user clicks the "High Score Board" option
    Then the user should be taken to the High Score screen
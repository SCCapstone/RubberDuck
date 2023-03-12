Feature: High Score screen
    Tests whether player can share high score, replay game, or return to home menu from the high score screen

  Scenario: User views high score screen with no high scores
    Given the game is running and the high score screen is opened
    When there are no high scores in the high score board
    Then the user sees the "High Score Board" subtitle
    And the user sees a message that there are no high scores

  Scenario: User views high score screen with high scores
    Given the game is running and the high score screen is opened
    When there are high scores in the high score board
    Then the user sees the "High Score Board" subtitle
    And the user sees a list of the top 10 high scores
    And the user sees a "Play Again" button
    And the user sees a "Home" button
    And the user sees a "Share" button

  Scenario: User clicks the "Play Again" button
    Given the high score screen is opened
    When the user clicks the "Play Again" button
    Then the game menu changes to "GAME"

  Scenario: User clicks the "Home" button
    Given the high score screen is opened
    When the user clicks the "Home" button
    Then the game menu changes to "HOME"

  Scenario: User clicks the "Share" button
    Given the high score screen is opened
    When the user clicks the "Share" button
    Then the user is prompted to save a screenshot of the high score screen
    And the file is saved to the selected directory
    And a message is displayed confirming that the high score has been saved
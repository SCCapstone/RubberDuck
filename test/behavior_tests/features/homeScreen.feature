Feature: Home screen
    Tests whether player can access desired view from the home screen

Scenario: Start game
    Given Game is loaded
    When the player clicks the 'Start Game' button
    Then a new game is started

Scenario: Access Settings screen
    Given Game is loaded
    When the player clicks the 'Settings' button
    Then the view switches to the settings screen

Scenario: Access High Scores screen
    Given Game is loaded
    When the player clicks the 'High Scores' button
    Then the view switches to the high score screen

Scenario: Access Customize screen
    Given Game is loaded
    When the player clicks the 'Customize' button
    Then the view switches to the customize screen

Scenario: Access Stats screen
    Given Game is loaded
    When the player clicks the 'Stats' button
    Then the view switches to the stats screen

Scenario: Quit game
    Given Game is loaded
    When the player clicks the 'Quit' button
    Then the application is closed

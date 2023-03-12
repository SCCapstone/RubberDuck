Feature: Stats screen
    Tests whether player can share high score, access home screen, and quit game from stat screen

Scenario: User can view stats screen, quit or return to home menu
    Given Stats screen loaded
    When the user starts the stat screen
    Then the screen background should be set to main.jpg
    And three buttons should be displayed with the text "Share", "Home", and "Quit"
    And the user should be able to click the "Share" button to share their stats
    And the user should be able to click the "Home" button to go back to the home screen
    And the user should be able to click the "Quit" button to quit the game

Scenario: User can shares stats
    Given Stats screen loaded
    When the user clicks to share their stats
    Then a file with a filename formatted as "stat-YYYYMMDD-HHMMSS.png" should be created
    And a file dialog should appear
    And the user should be able to choose a directory to save the file in
    And the file should be saved to the chosen directory
    And a message should be displayed telling the user that their stats have been saved

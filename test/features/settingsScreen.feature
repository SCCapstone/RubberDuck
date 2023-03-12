Feature: Settings screen
    Tests whether player can change settings, input or export settings, or reset settings to default from the settings screen

  Scenario: Change volume sliders
    Given the player is on the settings screen
    When the player clicks on a volume slider
    Then the volume should be lowered or increased accordingly

Scenario: Change name
    Given the player is on the settings screen
    When the player clicks on the name text box and types
    Then the new name should apper
    And the new player name should be saved in the settings file

Scenario: Change difficulty or keymapping
    Given the player is on the settings screen
    When the player clicks a difficulty setting or keymapping
    Then the difficulty level or keymapping should change accordingly

  Scenario: Input settings
    Given the player is on the settings screen
    When the player inputs new settings
    Then the new settings should be displayed

  Scenario: Export settings
    Given the player is on the settings screen
    When the player exports the current settings
    Then the settings should be saved to a file

  Scenario: Reset to default settings
    Given the player is on the settings screen
    When the player resets the settings to default
    Then the default settings should be loaded
Feature: Settings screen
    Tests whether player can change settings, input or export settings, or reset settings to default from the settings screen

Scenario: Setting Screen - Change Name
    Given the player is on the settings screen
    When the player changes the name
    Then the players name is changed

Scenario: Setting Screen - Change Master Volume
    Given the player is on the settings screen
    When the player changes the master volume
    Then 
    

Scenario: Setting Screen - Change Music Volume 
    Given the player is on the settings screen
    When the player changes the music volume
    Then the players music volume is changed

Scenario: Setting Screen - Change SFX Volume
    Given the player is on the settings screen
    When the player changes the SFX volume
    Then the players SFX volume is changed

Scenario: Setting Screen - Change Difficulty Easy
    Given the player is on the settings screen
    When the player changes the difficulty to easy
    Then the players difficulty is changed to easy

Scenario: Setting Screen - Change Difficulty Medium
    Given the player is on the settings screen
    When the player changes the difficulty to medium
    Then the players difficulty is changed to medium

Scenario: Setting Screen - Change Difficulty Hard
    Given the player is on the settings screen
    When the player changes the difficulty to hard
    Then the players difficulty is changed to hard

Scenario: Setting Screen - Change Input Wasd
    Given the player is on the settings screen
    When the player changes the input to wasd
    Then the players input is changed to wasd

Scenario: Setting Screen - Change Input Arrows
    Given the player is on the settings screen
    When the player changes the input to arrows
    Then the players input is changed to arrows
  
Scenario: Setting Screen - Help Button
    Given the player is on the settings screen
    When the player clicks the help button
    Then the help popup is displayed

Scenario: Setting Screen - Default Button
    Given the player is on the settings screen
    When the player clicks the default button
    Then the settings are reset to default

Scenario: Setting Screen - Export Button
    Given the player is on the settings screen
    When the player clicks the export button
    Then the settings are exported to a file

Scenario: Setting Screen - Import Button
    Given the player is on the settings screen
    When the player clicks the import button
    Then the settings are imported from a file
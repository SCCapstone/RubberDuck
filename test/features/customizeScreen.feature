Feature: Customize screen
    Tests whether player can buy/equip skins, hats, and background from the customize screen

Scenario: Preview previous duck base skin
    Given the player is on the customize screen
    When the player clicks on the left arrow button
    Then the preview of the previous duck base skin should be displayed
    And the player should see the option to purchase/equip the previous duck base skin

Scenario: Preview next duck base skin
    When the player clicks on the right arrow button
    Then the preview of the next duck base skin should be displayed
    And the player should see the option to purchase/equip the next duck base skin

Scenario: Equip 
    Given preview of duck base skin on the customize screen
    When the player clicks on the "Equip" button next to a duck base skin
    Then the selected duck base skin should be equipped

Scenario: Purchase
    Given preview of duck base skin on the customize screen
    When the player clicks on the "Purchase" button next to a duck base skin
    Then the selected duck base skin should be equipped
    And the coins should be decreased by the set amount

Scenario: Switch to Hats
    Given the user is on the customize screen and viewing base Skins
    When the player clicks the "Hats" button
    Then the available duck hats should appear 
    
Scenario: Switch to Backgrounds
    Given the user is on the customize screen and viewing base Skins
    When the player clicks the "Backgrounds" button
    Then the available duck hats should appear 


Feature: Game screen
    Tests whether player can perform all actions required during gameplay

Scenario: Pause Game
Given the game is running
When the player presses the pause button
Then the game should pause and the pause menu should appear

Scenario: Fire rocket
Given the game is running
When the player left clicks
Then a rocket should be launched from the player's position towards where the mouse is pointing

Scenario: Swept off screen
Given the game is running
When the player moves to the edge of the screen
Then the player should die, the game should end, and the game over menu should appear.
Scenario: Collect Coin
Given the game is running and a coin is present
When the player moves over the coin
Then the coin should disappear and the player's score and number of coins should increase

Scenario: Collect health
Given the game is running, a heart is present, and player health is not full
When the player moves over the heart
Then the heart should disappear and the player's health should increase

Scenario: Collect SpeedUp
Given the game is running and a speed boost is present
When the player moves over the speed boost
Then the speed boost should disappear and the player's movement speed should increase temporarily

Scenario: Hit by enemy
Given the game is running and an enemy is present
When the player collides with the enemy
Then the player's health should decrease and the enemy should disappear

Scenario: Lose all hearts
Given the game is running and the player has 1 health left
When the player collides with an enemy
Then the player should die, the game should end, and the game over menu should appear.
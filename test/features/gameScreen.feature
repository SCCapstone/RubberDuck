Feature: Game screen
    Tests whether player can perform all actions required during gameplay

Scenario: Start Game
Given the game is called to splash screen
When the player presses the start button
Then the game should start and the game screen should appear

Scenario: Fire rocket
Given the game is running
When the player presses the fire button
Then a rocket should be launched from the player's position towards where the mouse is pointing

Scenario: Lose a heart
Given the game is running
When the player collides with an enemy
Then the player should lose a heart

Scenario: Pause Game
Given the game is running
When the player presses the pause button
Then the game should pause and the pause screen should appear

Scenario: Lose the game
Given the game is running
When the player loses all hearts
Then the game should end and the game over screen should appear

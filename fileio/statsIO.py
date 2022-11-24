# Imports
import json
import os

# Global Variables
global distanceTravelled
global totalGamesPlayed
global totalGameTime
global enemyDefeated
global spaceshipKills
global meteroidKills
global allTimeCurrency
global averageGameTime
global averagePoints


# When the game is started, load the stats from the file
def load_stats():
    global distanceTravelled
    global totalGamesPlayed
    global totalGameTime
    global enemyDefeated
    global spaceshipKills
    global meteroidKills
    global allTimeCurrency
    global averageGameTime
    global averagePoints
    global averagePoints

    if (os.path.exists("stats.json")):
        with open("stats.json") as f:
            data = json.load(f)
            distanceTravelled = data["distanceTravelled"]
            totalGamesPlayed = data["totalGamesPlayed"]
            totalGameTime = data["totalGameTime"]
            enemyDefeated = data["enemyDefeated"]
            spaceshipKills = data["spaceshipKills"]
            meteroidKills = data["meteroidKills"]
            allTimeCurrency = data["allTimeCurrency"]
            averageGameTime = data["averageGameTime"]
            averagePoints = data["averagePoints"]
    else:
        distanceTravelled = 0
        totalGamesPlayed = 0
        totalGameTime = 0
        enemyDefeated = 0
        spaceshipKills = 0
        meteroidKills = 0
        allTimeCurrency = 0
        averageGameTime = 0
        averagePoints = 0
        save_stats()


# When the game is closed, save the stats to the file
def save_stats():
    data = {
        "distanceTravelled": distanceTravelled,
        "totalGamesPlayed": totalGamesPlayed,
        "totalGameTime": totalGameTime,
        "enemyDefeated": enemyDefeated,
        "spaceshipKills": spaceshipKills,
        "meteroidKills": meteroidKills,
        "allTimeCurrency": allTimeCurrency,
        "averageGameTime": averageGameTime,
        "averagePoints": averagePoints
    }
    with open("fileio\\stats.json", "w") as f:
        json.dump(data, f, indent=4)

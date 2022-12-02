"""summary: FileIo handler for stats
"""
import json
import os

# Global Variables
global distanceTravelled, totalGamesPlayed, totalGameTime
global enemyDefeated, spaceshipKills, meteroidKills
global allTimeCurrency, averageGameTime, averagePoints


# When the game is started, load the stats from the file
def load_stats():
    """summary: Loads the stats from the file
    """
    global distanceTravelled, totalGamesPlayed, totalGameTime
    global enemyDefeated, spaceshipKills, meteroidKills
    global allTimeCurrency, averageGameTime, averagePoints

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


def save_stats():
    """summary: Saves the stats to the file
    """
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

    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)


# Imports
import json

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

    data = json.load(open("fileio\\stats.json"))

    distanceTravelled = data["distanceTravelled"]
    totalGamesPlayed = data["totalGamesPlayed"]
    totalGameTime = data["totalGameTime"]
    enemyDefeated = data["enemyDefeated"]
    spaceshipKills = data["spaceshipKills"]
    meteroidKills = data["meteroidKills"]
    allTimeCurrency = data["allTimeCurrency"]
    averageGameTime = data["averageGameTime"]
    averagePoints = data["averagePoints"]


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

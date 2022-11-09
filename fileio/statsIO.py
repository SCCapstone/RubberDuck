import json

distanceTravelled = 0
totalGamesPlayed = 1
totalGameTime = 234
enemyDefeated = 3
spaceshipKills = 4
meteroidKills = 5432
allTimeCurrency = 6
averageGameTime = 7
averagePoints = 82

def loadStats():
    with open("fileio\stats.json", "r") as f:
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
        
def saveStats():
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
    with open("fileio\stats.json", "w") as f:
        json.dump(data, f, indent=4)
        
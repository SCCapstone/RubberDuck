"""summary: FileIo handler for stats
"""
import json
import os
from fileio import settingIO
import time
from fileio import customizationIO

# Global Variables
global distanceTravelled, totalGamesPlayed, totalGameTime, dontShow
global enemyDefeated, allTimeCurrency, averageGameTime, averagePoints

help_text = "Welcome to Ducks in Space!\n\nYour goal is to navigate outer space while shooting enemies to both stay alive and on screen. Earn high scores by collecting coins, shooting enemies, and staying alive as long as possible. Collect hearts to increase your health and grab speed boosts to move faster. Use WASD to move and shoot enemies by aiming with your mouse and click to shoot. Customize your duck with unlockables purchased with the coins you collect."


# When the game is started, load the stats from the file
def load_stats():
    """summary: Loads the stats from the file
    """
    global distanceTravelled, totalGamesPlayed, totalGameTime, dontShow
    global enemyDefeated, allTimeCurrency, averageGameTime, averagePoints

    if (os.path.exists("fileio\\stats.json")):
        with open("fileio\\stats.json") as f:
            data = json.load(f)
            distanceTravelled = data["distanceTravelled"]
            totalGamesPlayed = data["totalGamesPlayed"]
            totalGameTime = data["totalGameTime"]
            enemyDefeated = data["enemyDefeated"]
            allTimeCurrency = data["allTimeCurrency"]
            averageGameTime = data["averageGameTime"]
            averagePoints = data["averagePoints"]
            dontShow = data["dontShow"]
    else:
        distanceTravelled = 0
        totalGamesPlayed = 0
        totalGameTime = 0
        enemyDefeated = 0
        allTimeCurrency = 0
        averageGameTime = 0
        averagePoints = 0
        dontShow = False
        save_stats()


def save_stats():
    """summary: Saves the stats to the file
    """
    data = {
        "distanceTravelled": distanceTravelled,
        "totalGamesPlayed": totalGamesPlayed,
        "totalGameTime": totalGameTime,
        "enemyDefeated": enemyDefeated,
        "allTimeCurrency": allTimeCurrency,
        "averageGameTime": averageGameTime,
        "averagePoints": averagePoints,
        "dontShow": dontShow
    }

    with open("fileio\\stats.json", "w") as f:
        json.dump(data, f, indent=4)


def postgame_update(game):
    # Game Format is [Distance, Time, Points, Currency, Enemies, Spaceships, Meteroi]
    global distanceTravelled, totalGamesPlayed, totalGameTime
    global enemyDefeated, allTimeCurrency, averageGameTime, averagePoints

    customizationIO.add_currency(game[3])
    totalGamesPlayed += 1
    totalGameTime += game[1]
    averageGameTime = totalGameTime / totalGamesPlayed
    averagePoints = (
        (averagePoints * totalGamesPlayed) + game[2]) / totalGamesPlayed
    distanceTravelled += game[0]
    enemyDefeated += game[4]
    allTimeCurrency += game[3]
    save_stats()


def create_game_log(game):
    # Game Format is [Distance, Time, Points, Currency, Enemies, Spaceships, Meteroids]
    if not os.path.exists("fileio\\logs"):
        os.mkdir("fileio\\logs")
    with open("fileio\\logs\\game_log.txt", "a") as f:
        game_log = {}
        game_log["user"] = settingIO.get_username()
        game_log["date"] = time.strftime("%Y%m%d-%H%M%S")
        game_log["difficulty"] = settingIO.DifficultyLevel
        game_log["distance"] = game[0]
        game_log["time"] = game[1]
        game_log["points"] = game[2]
        game_log["currency"] = game[3]
        game_log["enemies"] = game[4]

        #append to the game_log.txt file
        f.write


def reset_stats():
    global distanceTravelled, totalGamesPlayed, totalGameTime, dontShow
    global enemyDefeated, allTimeCurrency, averageGameTime, averagePoints

    distanceTravelled = 0
    totalGamesPlayed = 0
    totalGameTime = 0
    enemyDefeated = 0
    allTimeCurrency = 0
    averageGameTime = 0
    averagePoints = 0
    dontShow = False
    save_stats()

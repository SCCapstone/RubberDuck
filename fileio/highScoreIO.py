import json
import os
import datetime

global high_score_board

# Fotmat (Number Player_Name, Score, Date)


def loadHighScore():
    global high_score_board
    if not os.path.exists("fileio\\HighScore.json"):
        high_score_board = []
    else:
        high_score_board = json.load(open("fileio\\HighScore.json"))


def saveHighScore():
    with open("fileio\\highScore.json", "w") as f:
        json.dump(high_score_board, f, indent=4)


def printHighScore():
    if len(high_score_board) == 0:
        print("No High Score")
    for i in high_score_board:
        print(i)


def getHighScore():
    return high_score_board

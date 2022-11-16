import json
import os

global high_score_board

# Fotmat (Number Player_Name, Score, Date)


def load_high_scores():
    global high_score_board
    if not os.path.exists("fileio\\HighScore.json"):
        high_score_board = []
    else:
        high_score_board = json.load(open("fileio\\HighScore.json"))


def save_high_scores():
    with open("fileio\\highScore.json", "w") as f:
        json.dump(high_score_board, f, indent=4)


def print_high_scores():
    if len(high_score_board) == 0:
        print("No High Score")
    for i in high_score_board:
        print(i)


def get_high_scores():
    return high_score_board

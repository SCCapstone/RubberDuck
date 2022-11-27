""" summary: FileIo handler for high scores
"""
import json
import os

global high_score_board

# Fotmat (Number Player_Name, Score, Date)


def load_high_scores():
    """summary: Loads the high scores from the file
    """
    global high_score_board
    if not os.path.exists("fileio\\HighScore.json"):
        high_score_board = []
    else:
        high_score_board = json.load(open("fileio\\HighScore.json"))


def save_high_scores():
    """summary: Saves the high scores to the file
    """
    with open("fileio\\highScore.json", "w") as f:
        json.dump(high_score_board, f, indent=4)

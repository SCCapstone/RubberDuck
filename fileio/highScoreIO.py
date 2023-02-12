""" summary: FileIo handler for high scores
"""
import json
import os
import pandas as pd
import menuStructure as menuS

global high_score_board

# Fotmat (Number Player_Name, Score, Date)


def load_high_scores():
    """summary: Loads the high scores from the file
    """
    global high_score_board
    if not os.path.exists("fileio\\HighScore.json"):
        high_score_board = pd.DataFrame(columns=["Player_Name", "Score", "Date"])
    else:
        try:
            high_score_board = pd.read_json("fileio\\HighScore.json")
        except:
            high_score_board = pd.DataFrame(columns=["Player_Name", "Score", "Date"])


def save_high_scores():
    """summary: Saves the high scores to the file
    """
    with open("fileio\\highScore.json", "w") as f:
        high_score_board.to_json(f)


def print_high_scores():
    if len(high_score_board) == 0:
        print("No High Score")
    else:
        for i in high_score_board:
            print(i)


def get_high_scores():
    return high_score_board

def check_for_high_score(score):
    #score format is [Player_Name, Score, Date]
    global high_score_board
    if len(high_score_board) < 10:
        add_new_high_score(score)
    else:
        if score[1] > high_score_board.iloc[-1]["Score"]:
            #adjust date to MM/DD/YYYY
            score[2] = score[2].strftime("%m/%d/%Y")
            add_new_high_score(score)
    
def add_new_high_score(score):
    global high_score_board
    high_score_board = high_score_board.append(pd.DataFrame([score], columns=["Player_Name", "Score", "Date"]))
    high_score_board = high_score_board.sort_values(by=["Score"], ascending=False)
    high_score_board = high_score_board.reset_index(drop=True)
    menuS.set_game_menu(menuS.menu.HIGH_SCORE, True)
    
    save_high_scores()
    
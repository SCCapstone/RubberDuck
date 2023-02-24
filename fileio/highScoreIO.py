""" summary: FileIo handler for high scores
"""
import os
import pandas as pd
import menuStructure as menuS
from assets import values

global high_score_board

# Fotmat (Number Player_Name, Score, Date)


def load_high_scores():
    """summary: Loads the high scores from the file
    """
    global high_score_board
    if not os.path.exists("fileio\\HighScore.json"):
        high_score_board = pd.DataFrame(
            columns=["Player_Name", "Score", "Date"])
    else:
        try:
            high_score_board = pd.read_json("fileio\\HighScore.json",
                                            convert_dates=False)
        except:
            high_score_board = pd.DataFrame(
                columns=["Player_Name", "Score", "Date"])


def save_high_scores():
    """summary: Saves the high scores to the file
    """
    with open("fileio\\highScore.json", "w") as f:
        #make pretty
        high_score_board.to_json(f, indent=2)


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
    #make date month YYYY-MM-DD
    #check if 10 entries in high score board
    if len(high_score_board) < 10:
        add_new_high_score(score)
    else:
        #check if score is higher than lowest score
        if score[1] > high_score_board.iloc[9, 1]:
            add_new_high_score(score)


def add_new_high_score(score):
    values.newHighScore = True
    global high_score_board
    #use concat to add new score
    high_score_board = high_score_board.append(
        pd.DataFrame([score], columns=["Player_Name", "Score", "Date"]))
    high_score_board = high_score_board.sort_values(by=["Score"],
                                                    ascending=False)
    high_score_board = high_score_board.reset_index(drop=True)

    #check if 11 entries in high score board
    if len(high_score_board) > 10:
        high_score_board = high_score_board.drop(10)
    menuS.set_game_menu(menuS.menu.HIGH_SCORE)

    #find i column in high score board for [score[0], score[1], score[2]]
    values.newHighScoreId = high_score_board.index[
        (high_score_board["Player_Name"] == score[0])
        & (high_score_board["Score"] == score[1]) &
        (high_score_board["Date"] == score[2])].tolist()[0]

    save_high_scores()

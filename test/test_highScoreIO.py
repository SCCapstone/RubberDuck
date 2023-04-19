import sys

sys.path.append('..')
import os
import pytest

from fileio import highScoreIO


@pytest.fixture
def test_load_high_scores():
    # Test that the high score board is loaded
    highScoreIO.load_high_scores()
    assert highScoreIO.high_score_board is not None


@pytest.fixture
def test_save_high_scores():
    # Test that the high score board is saved
    # Delete the file if it exists
    if os.path.exists("fileio\\highScore.json"):
        os.remove("fileio\\highScore.json")
    highScoreIO.save_high_scores()
    assert os.path.exists("fileio\\highScore.json")


#Used for Debugging
def test_print_high_scores():
    assert True


def test_get_high_scores():
    board = highScoreIO.get_high_scores()
    assert board is not None
    #check that the board is a dataframe
    assert type(board) == type(highScoreIO.high_score_board)


def test_check_for_high_score():
    # Make backup of highScore.json
    if os.path.exists("fileio\\highScore.json"):
        os.rename("fileio\\highScore.json", "fileio\\highScore.json.bak")
    
    # Test that a high score is added to the board
    # Get Highest Score
    highScore = highScoreIO.high_score_board.iloc[0, 1]
    score = ["Player", highScore + 1, "2020-01-01"]
    highScoreIO.check_for_high_score(score)
    assert highScoreIO.high_score_board.iloc[0, 0] == "Player"
    assert highScoreIO.high_score_board.iloc[0, 1] == highScore + 1
    assert highScoreIO.high_score_board.iloc[0, 2] == "2020-01-01"

    # Test that a low score is not added to the board
    score = ["PlayerBad", -1, "2020-01-01"]
    highScoreIO.check_for_high_score(score)
    #Check that the board is still the same
    foundNeg1 = False
    for i in highScoreIO.high_score_board:
        if i[1] == -1:
            foundNeg1 = True
    assert foundNeg1 == False

    # Restore backup of highScore.json
    if os.path.exists("fileio\\highScore.json.bak"):
        os.remove("fileio\\highScore.json")
        os.rename("fileio\\highScore.json.bak", "fileio\\highScore.json")


def test_add_new_high_score():
    # Make backup of highScore.json
    if os.path.exists("fileio\\highScore.json"):
        os.rename("fileio\\highScore.json", "fileio\\highScore.json.bak")

    # Test that a high score is added to the board
    # Get Highest Score
    highScore = highScoreIO.high_score_board.iloc[0, 1]
    score = ["PlayerBe", highScore + 1, "2020-01-01"]
    highScoreIO.add_new_high_score(score)
    assert highScoreIO.high_score_board.iloc[0, 0] == "PlayerBe"
    assert highScoreIO.high_score_board.iloc[0, 1] == highScore + 1
    assert highScoreIO.high_score_board.iloc[0, 2] == "2020-01-01"
    
    # Restore backup of highScore.json
    if os.path.exists("fileio\\highScore.json.bak"):
        os.remove("fileio\\highScore.json")
        os.rename("fileio\\highScore.json.bak", "fileio\\highScore.json")

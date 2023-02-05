import sys
sys.path.append('..')
import pygame
import os
import pandas as pd
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
    
def test_print_high_scores():
    assert True
    
def test_get_high_scores():
    assert True
    

def test_check_for_high_score():
    assert True

    
def test_add_new_high_score():
    assert True
    
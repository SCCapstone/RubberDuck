import sys
sys.path.append('..')

from fileio import settingIO

def test_convertDifficultyEasy():
    diff = "Easy"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.EASY

def test_convertDifficultyMedium():
    diff = "Medium"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.MEDIUM

def test_convertDifficultyHard():
    diff = "Hard"
    assert settingIO.convertDifficulty(diff) == settingIO.difficulty.HARD
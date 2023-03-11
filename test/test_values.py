import sys

sys.path.append('..')
import os
import pytest
import time

from assets import values

def test_set_screen_size():
        values.set_screen_size(500, 600)
        assert values.screenX == 500
        assert values.screenX == 500
        assert values.SCREEN_SIZE == (500,600)

"""def test_sessionRunTime():
        global startTime
        startTime = time.time()
        with patch('time.gmtime') as mock_gmtime:
            mock_gmtime.return_value = time.struct_time([0, 0, 0, 1, 0, 0, 0, 0, 0])
            result = values.sessionRunTime()
        assert result == "01:00"
"""

def test_setStartTime():
        global startTime
        values.setStartTime()
        assert values.startTime > -1

def test_setGameScore():
        values.setGameScore(100)
        assert values.game_score == 100

def test_resetGameScore():
        game_score = 50
        values.resetGameScore()
        assert values.game_score == 0

def test_setCoinsinGame():
        values.setCoinsinGame(10)
        assert values.coins_in_game == 10

def test_resetCoinsinGame():
        coins_in_game = 20
        values.resetCoinsinGame()
        assert values.coins_in_game == 0

def test_setSkin():
        values.setSkin("skin1")
        assert values.current_skin == "skin1"
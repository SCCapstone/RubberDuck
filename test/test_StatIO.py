import sys

sys.path.append('..')
import os

from fileio import statsIO


def test_load_stats():
    statsIO.reset_stats()
    statsIO.load_stats()
    assert statsIO.distanceTravelled == 0
    assert statsIO.totalGamesPlayed == 0
    assert statsIO.totalGameTime == 0
    assert statsIO.enemyDefeated == 0
    assert statsIO.allTimeCurrency == 0
    assert statsIO.averageGameTime == 0
    assert statsIO.averagePoints == 0


def test_save_stats():
    # Delete fileio\stats.json if it exists
    statsIO.save_stats
    assert os.path.exists("fileio\\stats.json")


def test_postgame_update():
    statsIO.reset_stats()
    statsIO.postgame_update([100, 100, 100, 100, 100, 100, 100, 100])
    assert statsIO.distanceTravelled == 100
    assert statsIO.totalGamesPlayed == 1
    assert statsIO.totalGameTime == 100
    assert statsIO.enemyDefeated == 100
    assert statsIO.allTimeCurrency == 100
    assert statsIO.averageGameTime == 100
    assert statsIO.averagePoints == 100


def test_reset_stats():
    statsIO.reset_stats()
    assert statsIO.distanceTravelled == 0
    assert statsIO.totalGamesPlayed == 0
    assert statsIO.totalGameTime == 0
    assert statsIO.enemyDefeated == 0
    #assert statsIO.spaceshipKills == 0
    #assert statsIO.meteroidKills == 0
    assert statsIO.allTimeCurrency == 0
    assert statsIO.averageGameTime == 0
    assert statsIO.averagePoints == 0

def test_create_game_log():
    # Code Abondoned
    assert True
    

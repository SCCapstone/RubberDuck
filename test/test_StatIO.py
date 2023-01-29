import sys
sys.path.append('..')
import pygame
import os

from fileio import statsIO

def test_load_stats():
    statsIO.reset_stats()
    statsIO.load_stats()
    assert statsIO.distanceTravelled == 0
    assert statsIO.totalGamesPlayed == 0
    assert statsIO.totalGameTime == 0
    assert statsIO.enemyDefeated == 0
    assert statsIO.spaceshipKills == 0
    assert statsIO.meteroidKills == 0
    assert statsIO.allTimeCurrency == 0
    assert statsIO.averageGameTime == 0
    assert statsIO.averagePoints == 0
    
def test_save_stats():
    statsIO.save_stats
    assert os.path.exists("fileio\\stats.json")
    
def test_postgame_update():
    statsIO.reset_stats()
    

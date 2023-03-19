import sys

sys.path.append('..')
import os
import pytest
import unittest

import menuStructure
import time
import math


def test_set_and_get_game_menu():
        # Test setting and getting the game menu
        from menuStructure import menu
        menuStructure.set_game_menu(menu.HOME)
        assert menuStructure.get_game_menu() == (menu.HOME)
        
        menuStructure.set_game_menu(menu.STAT)
        assert menuStructure.get_game_menu() == (menu.STAT)

        menuStructure.set_game_menu(menu.GAME)
        assert menuStructure.get_game_menu() == (menu.GAME)

        menuStructure.set_game_menu(menu.CUSTOMIZE)
        assert menuStructure.get_game_menu() == (menu.CUSTOMIZE)

        menuStructure.set_game_menu(menu.HIGH_SCORE)
        assert menuStructure.get_game_menu() == (menu.HIGH_SCORE)

        menuStructure.set_game_menu(menu.SETTING)
        assert menuStructure.get_game_menu() == (menu.SETTING)

        menuStructure.set_game_menu(menu.QUIT)
        assert menuStructure.get_game_menu() == (menu.QUIT)

        menuStructure.set_game_menu(menu.GAMEOVER)
        assert menuStructure.get_game_menu() == (menu.GAMEOVER)


def test_double_click_preventer():
        # Test that the double_click_preventer function sleeps for 0.1 seconds

        start_time = time.time()
        menuStructure.double_click_preventer()
        end_time = time.time()
        assert math.isclose(end_time - start_time, 0.1, abs_tol = 0.05)


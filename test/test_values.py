import sys

sys.path.append('..')

from assets import values

global store

def test_set_screen_size():
    values.set_screen_size(500, 600)
    assert values.screenX == 500
    assert values.screenX == 500
    assert values.SCREEN_SIZE == (500, 600)



def test_sessionRunTime():
    assert values.sessionRunTime() == "00:00"


def test_setStartTime():
    global startTime
    values.setStartTime()
    assert values.startTime > -1


def test_setGameScore():
    values.setGameScore(100)
    assert values.game_score == 100


def test_resetGameScore():
    values.resetGameScore()
    assert values.game_score == 0
    


def test_getBG():
    assert values.getBG(0) == "assets/backgrounds/base_bg.jpg"
    assert values.getBG(1) == "assets/backgrounds/pixelNebula.png"
    assert values.getBG(2) == "assets/backgrounds/pixelSpace.png"


def test_updateCoins():
    values.coins_in_game = 10
    values.updateCoins()
    assert values.coins_in_game == 10



def test_setBackground():
    
    values.setBackground("bg1")
    assert values.current_background == "bg1"


def test_setSkin():
    values.setSkin("skin1")
    assert values.current_skin == "skin1"


def test_resetCoinsinGame():
    values.resetCoinsinGame()
    assert values.coins_in_game == 0
    



def test_setCoinsinGame():
    values.setCoinsinGame(10)
    assert values.coins_in_game == 10

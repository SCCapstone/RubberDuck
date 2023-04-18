import sys
from assets import soundHandler
from fileio import settingIO
import pygame
sys.path.append('..')

global hand

def test_init():
    global hand
    hand = soundHandler.SFXHandler()
    assert hand is not None
    assert hand.currentSong == "NA"


def test_sound_volume():
    global hand
    hand.sound_volume(50)
    assert hand.Sound_volume_var == 0.5
    assert hand.sound_volume(100) == True
    assert hand.sound_volume(-1) == False


def test_music_volume():
    global hand
    hand.music_volume(50)
    assert pygame.mixer.music.get_volume() == 0.5
    assert hand.music_volume(100) == True
    assert hand.music_volume(-1) == False

def test_playSound():
    global hand
    hand.playSound("quack")
    assert hand.playSound("NA") == False
    assert hand.playSound("quack") == True


def test_playMusic():
    global hand
    hand.playMusic("menus")
    assert hand.playMusic("NA") == False
    assert hand.playMusic("menus") == True


import pygame
from fileio import settingIO

# Dictionary of all sounds
soundBook = {
    "quack": "assets/sfx/quack.ogg",
    "boost": "assets/sfx/boost.ogg",
    "coin": "assets/sfx/coin.ogg",
    "boom": "assets/sfx/boom.ogg",
    "rocket": "assets/sfx/rocket.ogg",
    "oof": "assets/sfx/oof.ogg",
    "heal": "assets/sfx/heal.ogg"
}

# Dictionary of all music tracks
musicBook = {
    "menus": "assets/music/menus.ogg",
    "gameplay": "assets/music/gameplay.ogg",
    "highScore": "assets/music/highscore.ogg"
}

# TODO:
# Add checks to see if game sounds/music is on or off
# Add volume slider backend


class SFXHandler:

    def __init__(self):
        pygame.mixer.init()
        self.currentSong = "NA"
        self.sound_volume(settingIO.SFX_Volume *
                          (settingIO.Master_Volume / 100))
        self.music_volume(settingIO.Music_Volume *
                          (settingIO.Master_Volume / 100))

    def sound_volume(self, newVol):
        # Make sure it is a valid volume
        if newVol >= 0 and newVol <= 100:
            # Set volume
            self.Sound_volume_var = newVol / 100.0
            return True
        return False

    def music_volume(self, newVol):
        # Make sure it is a valid volume
        if newVol >= 0 and newVol <= 100:
            # Set music volume
            pygame.mixer.music.set_volume(newVol / 100.0)
            return True
        return False

    # Takes in a sound (see dictionary above) and plays a corresponding sound
    # file
    def playSound(self, sound):
        if sound in soundBook:
            playedSound = pygame.mixer.Sound(soundBook[sound])
            playedSound.set_volume(self.Sound_volume_var)
            pygame.mixer.Sound.play(playedSound)
            return True
        return False

    # Takes in a string (see dictionary above) and plays a corresponding music
    # file
    def playMusic(self, music):
        if music in musicBook and self.currentSong != music:
            if self.currentSong == "NA":
                pygame.mixer.music.load(musicBook[music])
                pygame.mixer.music.play()
                return True
            # Load the new song and unload the previous one to save memory
            pygame.mixer.music.load(musicBook[music])
            pygame.mixer.music.unload(musicBook[self.currentSong])
            # Play the loaded music track (-1 loops forever)
            pygame.mixer.music.play(-1)
            self.currentSong = music
            return True
        return False

import pygame

# Dictionary of all sounds
soundBook = {"quack": "assets/sfx/quack.ogg"}

# Dictionary of all music tracks
musicBook = {
    "menus": "assets/music/menus.ogg",
    "gameplay": "assets/music/gameplay.ogg"
}

# TODO:
# Add checks to see if game sounds/music is on or off
# Add volume slider backend


class SFXHandler:

    def __init__(self):
        pygame.mixer.init()
        self.currentSong = "NA"
        self.sound_volume = 1.0
        self.music_volume(100)

    def sound_volume(self, newVol):
        # Make sure it is a valid volume
        if newVol >= 0 and newVol <= 100:
            # Set volume
            self.sound_volume = newVol / 100.0
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
            playedSound.set_volume(self.sound_volume)
            pygame.mixer.Sound.play(pygame.mixer.Sound(soundBook[sound]))
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
            pygae.mixer.music.unload(musicBook[self.currentSong])
            # Play the loaded music track (-1 loops forever)
            pygame.mixer.music.play(-1)
            self.currentSong = music
            return True
        return False

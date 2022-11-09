import pygame

# Dictionary of all sounds
soundBook = {
    "quack": "assets/sfx/quack.ogg"
}

# Dictionary of all music tracks
musicBook = {
    "menus": "assets/music/menus.ogg",
    "gameplay": "assets/music/gameplay.ogg"
}


class SFXHandler:
    def __init__(self):
        pygame.mixer.init()
        self.currentSong = "NA"

    # Takes in a sound (see dictionary above) and plays a corresponding sound
    # file
    def playSound(self, sound):
        if sound in soundBook:
            pygame.mixer.Sound.play(pygame.mixer.Sound(soundBook[sound]))

    # Takes in a string (see dictionary above) and plays a corresponding music
    # file
    def playMusic(self, music):
        if music in musicBook and self.currentSong != music:
            if self.currentSong == "NA":
                pygame.mixer.music.load(musicBook[music])
                pygame.mixer.music.play()
                return
            # Load the new song and unload the previous one to save memory
            pygame.mixer.music.load(musicBook[music])
            pygame.mixer.music.unload(musicBook[self.currentSong])
            # Play the loaded music track (-1 loops forever)
            pygame.mixer.music.play(-1)
            self.currentSong = music

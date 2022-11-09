import pygame

# Dictionary of all sounds
soundBook = {
    "quack": "assets/sfx/quack.ogg"
}

# Dictionary of all music tracks
musicBook = {
    "menus": "assets/music/song.ogg"
}

class SFXHandler:
    def __init__(self):
        pygame.mixer.init()
        self.currentSong = "NA"

    def playSound(self, sound):
        # Play a given sound here
        if sound in soundBook:
            pygame.mixer.Sound.play(pygame.mixer.Sound(soundBook[sound]))

    def playMusic(self, music):
        # Play a given music track here
        # To make music loop, use mixer.music.play(-1) after loading the file
        if music in musicBook and self.currentSong != music:
            pygame.mixer.music.load(musicBook[music])
            pygame.mixer.music.play(-1)
            self.currentSong = music
import pygame.mixer

class SoundEffects:
    """Klasa przechowująca wszystkie elementy dźwiękowe w grze."""
    
    def __init__(self):
        """Inicjalizacja efektów dźwiękowych w grze."""
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load("background_game.mp3")
    
    def play_background_music(self):
        pygame.mixer.music.play(-1)
        
#class SoundEffects:
    #def __init__(self):
        #pygame.mixer.init()
        #self.background_music = pygame.mixer.Sound("background_game.mp3")
        #self.background_music.set_volume(0.1)

    #def play_background_music(self):
        #pygame.mixer.music.load("background_game.mp3")
        #pygame.mixer.music.play(loops=-1)

    #def background_music_playing(self):
        #return pygame.mixer.music.get_busy()
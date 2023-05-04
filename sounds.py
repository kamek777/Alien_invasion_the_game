import pygame.mixer

class SoundEffects:
    """Klasa przechowująca wszystkie elementy dźwiękowe w grze."""
    
    def __init__(self):
        """Inicjalizacja efektów dźwiękowych w grze."""
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load("background_game.mp3")
        
    def play_background_music(self):
        pygame.mixer.music.play(-1)
        
   
        

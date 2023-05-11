import pygame.mixer
class SoundEffects:
    """Klasa przechowująca wszystkie elementy dźwiękowe w grze."""
    
    def __init__(self):
        """Inicjalizacja efektów dźwiękowych w grze."""
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load("background.mp3")
        self.sound_effect_game_over = pygame.mixer.Sound("game_over.wav")
        self.sound_effect_hit_ship = pygame.mixer.Sound("hit.wav")
        
    def play_background_music(self):
        pygame.mixer.music.set_volume(0.3)  # Przyciszenie muzyki
        pygame.mixer.music.play(-1)
     
    def play_sound_effect1(self):
        """Dźwięk podczas przegrania gry."""
        self.sound_effect_game_over.play() 
        
    def play_sound_effect2(self):
        """Dźwięk uderzenia w obcego."""
        self.sound_effect_hit_ship.set_volume(0.1)
        self.sound_effect_hit_ship.play()
        
    
          
   
        

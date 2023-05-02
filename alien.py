import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedynczego obcego we flocie."""
    
    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #Wczytanie obraczu obceo i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('C:/Users/PC/OneDrive/Pulpit/projekty_pythona/project_strzelajacy_statek/images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        
        #Umieszczenie nowego obcego w pobliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Przechowywanie dokładnego poziomego położenia obcego.
        self.x = float(self.rect.x)
        
    def update(self):
        """Przesunięcie obcego w prawo."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
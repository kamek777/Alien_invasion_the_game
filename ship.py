import pygame 

class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym."""
    
    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe."""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('C:/Users/PC/OneDrive/Pulpit/projekty_pythona/project_strzelajacy_statek/images/ship.bmp')
        #Zmiana rozmiaru statku
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
        #Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)
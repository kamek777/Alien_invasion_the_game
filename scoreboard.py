import pygame.font

class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""
    
    def __init__(self, ai_game):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        #Ustawienia czcionki dla informacji dotyczących punktacji.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Przygotowanie początkowych obrazów z punktacją.
        self.prep_score()
        
    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz."""
        score_str = str(self.stats.get_score())
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #Wyświetlenie punktacji w prawym górnym rogu ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Wyświetlenie wyniku punktacji gracza na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
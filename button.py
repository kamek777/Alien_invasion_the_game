import pygame.font

class Button():
    """Inicjalizacja utworzenia przycisku umożliwiającego rozpoczęcie gry."""
    
    def __init__(self, ai_game, screen, msg):
        """Inicjalizacja atrybutów przycisku."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        #Zdefiniowanie wymiarów i właściwości przycisku.
        self.width, self.height = 700, 50
        self.button_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Utworzenie prostokąta przycisku i wyśrodkowanie go.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #Komunikat wyświetlany przez przycisk należy przygotować tylko jednokrotnie.
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie i wyśrodkowanie tekstu na przycisku."""   
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center 
        
    def draw_button(self):
        #Wyświetlenie pustego przycisku, a następnie komunikatu na nim.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
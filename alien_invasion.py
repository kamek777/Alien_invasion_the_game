import sys 
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from sounds import SoundEffects


class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja obcych")
        
        #Utworzenie egzemplarza przechowującego dane statystyczne dotyczące gry oraz utworzenie 
        #egzemplarza klasy Scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        #Utworzenie przycisku Gra
        self.play_button = Button(self, self.screen, "Rozpocznij grę!")
        
        #Utworzenie muzyki w grze
        self.sound_effects = SoundEffects()
        self.sound_effects.play_background_music()
        
        
        
        
    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            #Odświeżenie ekranu w trakcie każdej iteracji pętli.
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
               
            self._update_screen()
            
            #Usunięcie pocisków, które znajdują się poza ekranem.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
            self._update_screen()
            
    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        #Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        """Rozpoczęcie nowej gry po kliknięciu przycisku przez użytkownika."""
        #Metoda collidepoint sprawdza, czy punkt kliknięcia myszy znajduje się na przycisku.
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Wyzerowanie danych statystycznych gry.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            
            #Usunięcie zawartości list aliens i bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            self.sb.prep_score()
            self.sb.prep_level()
            
            #Utworzenie nowej floty i wyśrodkowanie statku.
            self._create_fleet()
            self.ship.center_ship()
            
            #Ukrycie kursora myszy podczas grania.
            pygame.mouse.set_visible(False)
            
            
            #Wyświetlenie pozostałej ilości statków do wykorzystania przez gracza.
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""            
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True   
        elif event.key == pygame.K_q:
            sys.exit() 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                
    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
        #Uaktualnienie położenia pocisków
        self.bullets.update()
        
        #Usunięcie pocisków, które znajdują się poza ekranem.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Reakcja na kolizję między pociskiem i obcym."""
        #Usunięcie wszystkich pocisków i obcych, między którymi doszło do kolizji.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)   
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sound_effects.play_sound_effect2()
        
        if not self.aliens:
            #Pozbycie się istniejących pocisków, przyspieszenie gry i utworzenie nowej floty.
            self.bullets.empty()
            self._create_fleet()    
            self.settings.increase_speed() 
            
            
            #Inkrementacja numeru poziomu.
            self.stats.level += 1 
            self.sb.prep_level()
    
    def _create_fleet(self):
        """Utworzenie pełnej floty obcych."""
        #Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w rzędzie.
        #Odległość między poszczególnymi obcymi jest równa szerokości obcego.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = 6
        #available_space_x // (2 * alien_width)
        
        #Ustawienie, ile rzędów obcych zmieści się na ekranie.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        #Utworzenie pełnej floty obcych.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
                
    def _create_alien(self, alien_number, row_number):
        """Utworzenie obcego i umieszczenie go w rzędzie.""" 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)   
    
    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        #Odświeżenie ekranu w trakcie każdej iteracji pętli.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        #Wyświetlenie informacji o punktacji.
        self.sb.show_score()
        
        #Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna.
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()           
    
    def _update_aliens(self):
        """
        Sprawdzenie, czy flota obcych znajduje się przy krawędzi, a następnie uaktualnienie
        położenia wszystkich obcych we flocie.
        """
        self._check_fleet_edges()
        self.aliens.update()
        
        #Wykrywanie kolizji między obcym i statkiem.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        #Wyszukiwanie obcych docierających do dolnej krawędzi ekranu.
        self._check_aliens_bottom
            
    def _check_fleet_edges(self):
        """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Przesunięcie całej floty w dół i zmiana kierunku, w którym się ona porusza."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Reakcja na uderzenie obcego w statek."""
        if self.stats.ships_left > 0:
            #Zmniejszenie wartości przechowywanej w ships_left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            #Usunięcie zawartości list aliens i bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            #Utworzenie nowej floty i wyśrodkowanie statku.
            self._create_fleet()
            self.ship.center_ship()
           
            #Pauza
            sleep(0.5)
            
        
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.sound_effect_game_over.play() 
        
    def _check_aliens_bottom(self):
        """Sprawdzenie, czy którykolwiek obcy dotarł do dolnej krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Tak samo jak w przypadku zderzenia statku z obcym.
                self._ship_hit()
                break


if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()
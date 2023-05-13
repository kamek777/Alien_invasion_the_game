class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""
    
    def __init__(self):
        """Inicjalizacja ustawień gry."""
        #Ustawienia dotyczące ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        #Ustawienia dotyczące statku.
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #Ustawienia dotyczące pocisku.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #Ustawienia dotyczące obcego.
        self.fleet_drop_speed = 10
        
        #Łatwa zmiana szybkości gry.
        self.speedup_scale = 1.2
        
        #Łatwa zmiana liczby puntków przyznawanych za zestrzelenie obcego.
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        #Wartość fleet_direction wynosząca 1 oznacza prawo, natomiast -1 oznacza lewo.
        self.fleet_direction = 1
        
        #Punktacja
        self.alien_points = 50
        
    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości gry i przyznawanych punktów."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        
        
        
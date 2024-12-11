class Settings:
    """class to store settings for Alien Invasion"""

    def __init__(self):
        '''initialize game settings'''
        """screen settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        """ship settings"""
        self.ship_limit = 3

        """Bullet settings"""
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        """Alien settings"""
        self.fleet_drop_speed = 10

        """level speed up scale"""
        self.speedup_scale = 1.15
        
        """score scale"""
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize variable settings"""
        self.ship_speed = 3
        self.bullet_speed = 4
        self.alien_speed = 1.0

        """fleet_direction uses a positive 1 represents right and -1 is left"""
        self.fleet_direction = 1

        """Scoring settings"""
        self.alien_points = 50

    def increase_speed(self):
        """increase the values according to levels"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
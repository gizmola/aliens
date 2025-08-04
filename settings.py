class Settings:
    """A class to store all settings for Alien Invasion."""

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2.0
        self.bullet_speed = 2.5
        self.alien_speed = 1.2
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Jet Black        
        self.bg_color_scoreboard = (40, 33, 32)

        # Ship settings
        self.ship_speed = 2.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        # Cream
        self.bullet_color = (248, 239, 228)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        """
        # Test Settings - Uncomment to test
        self.bullet_width = 300
        self.bullet_height = 30

        self.alien_speed = 4.0
        self.fleet_drop_speed = 25
        self.ship_speed = 5.0
        self.bullets_allowed = 8
        """
        self.initialize_dynamic_settings()


    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.sprites = []
        self.sprites.append(pygame.image.load('images/alien_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('images/alien_2.png').convert_alpha())
        self.current_sprite = 0.0
        self.image = self.sprites[int(self.current_sprite)]

        # Load the alien image and set its rect attribute.
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the alien horizontally."""
        self.current_sprite += 0.1
        if self.current_sprite >= 2:
            self.current_sprite = 0.0
        self.image = self.sprites[int(self.current_sprite)]

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right or self.rect.left <= 0)
    

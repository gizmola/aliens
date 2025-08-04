import pygame.font 
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        # Gold color
        self.text_color = (250, 208, 44)
        self.bg_frame_color = (0, 0, 0)
        # Font
        self.font = pygame.font.Font('fonts/ArchivoNarrow-Regular.ttf', 40)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color_scoreboard)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        """Show remaining Ships."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)  

    def prep_level(self):
        """Render Level"""
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color_scoreboard)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 20        

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color_scoreboard)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top    

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score to the screen."""
        
        score_rect_bg = self.score_rect.copy()
        # Add some padding to rectangle
        score_rect_bg.width += 20
        score_rect_bg.height += 10
        score_rect_bg.right -= 10
        score_rect_bg.top -= 5
        pygame.draw.rect(self.screen, self.bg_frame_color, score_rect_bg)
        self.screen.blit(self.score_image, self.score_rect)

        high_score_rect_bg = self.high_score_rect.copy()
        high_score_rect_bg.width += 20
        high_score_rect_bg.height += 10
        high_score_rect_bg.right -= 10
        high_score_rect_bg.top -= 5
        pygame.draw.rect(self.screen, self.bg_frame_color, high_score_rect_bg)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        level_rect_bg = self.level_rect.copy()
        level_rect_bg.width += 20
        level_rect_bg.height += 10
        level_rect_bg.right -= 10
        level_rect_bg.top -= 5
        pygame.draw.rect(self.screen, self.bg_frame_color, level_rect_bg)
        self.screen.blit(self.level_image, self.level_rect)
        
        self.ships.draw(self.screen)

import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.data_file = 'data/game.json'
        self.settings = ai_game.settings
        self.high_score = 0
        self.load_high_score()
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit - 1
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score from a file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.high_score = data.get('high_score', 0)
        except FileNotFoundError:
            self.high_score = 0
  
    def save_high_score(self):
        """Save the high score to a file."""
        data = {'high_score': self.high_score}
        with open(self.data_file, 'w') as f:
            json.dump(data, f)
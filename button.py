import pygame.font

class Button:
    """ A class to build buttons for the game. """
    def _prep_msg(self, msg):
        """ Turn msg into a rendered image and center text on the button. """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def __init__(self, ai_game, msg):
        """ Initialize button attributes. """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 180, 60
        self.button_color = (0, 135, 0)
        self.button_border_color = (0, 102, 77) 
        self.text_color = (255, 255, 255)
        # Font
        self.font = pygame.font.Font('fonts/ArchivoNarrow-Regular.ttf', 36)
        #self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.base_rect = pygame.Rect(0, 0, self.width+8, self.height+8)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.base_rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def draw_button(self):
        """ Draw blank button and then draw message. """
        pygame.draw.rect(self.screen, self.button_border_color, self.base_rect, width=10, border_radius=5)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
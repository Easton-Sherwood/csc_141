import pygame.font

class Button:
    """Class for the start button"""

    def __init__(self, ai_game, msg):
        """initialize the button"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        """Properties of button"""
        self.width, self.height = 200, 50
        self.button_color = (12, 209, 18)
        self.text_color = (171, 245, 174)
        self.font = pygame.font.SysFont(None, 48)

        """Build the button"""
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """draw the button and then the message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
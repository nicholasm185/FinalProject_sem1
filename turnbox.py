import pygame

class Turnbox:
    def __init__(self, screen, msg):
        # gets the screen and stores the size of the screen
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # sets the width of the background "holder" box
        self.width, self.height = 200, 60
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("Calibri", 30)

        # sets the position and size of the surface
        self.rect = pygame.Rect(650, 10, self.width, self.height)

        # renders the turnbox and sets it position to the middle of the "holder" box
        self.msgImage = self.font.render(msg, True, self.text_color, self.button_color)
        self.msgImage_rect = self.msgImage.get_rect()
        self.msgImage_rect.center = self.rect.center

    # changes the turn message
    def turn_initiator(self, msg):
        self.msgImage = self.font.render(msg, True, self.text_color, self.button_color)
        self.msgImage_rect = self.msgImage.get_rect()
        self.msgImage_rect.center = self.rect.center

    # draws the turnbox to the screen
    def draw_turnbox(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msgImage, self.msgImage_rect)

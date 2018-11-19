import pygame

class Instruction_box:
    def __init__(self, screen, msg):
        # gets the screen and stores the size of the screen
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # sets the width of the background "holder" box
        self.width, self.height = 200, 40
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("Calibri", 25)

        # sets the position and size of the surface
        self.rect = pygame.Rect(650, 320, self.width, self.height)

        # renders the instruction and sets it position to the middle of the "holder" box
        self.msgImage = self.font.render(msg, True, self.text_color, self.button_color)
        self.msgImage_rect = self.msgImage.get_rect()
        self.msgImage_rect.center = self.rect.center

    # this function is used to change the instruction
    def instruction_change(self, msg):
        self.msgImage = self.font.render(msg, True, self.text_color, self.button_color)
        self.msgImage_rect = self.msgImage.get_rect()
        self.msgImage_rect.center = self.rect.center

    # draws the instruction box to the screen
    def draw_instruction(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msgImage, self.msgImage_rect)

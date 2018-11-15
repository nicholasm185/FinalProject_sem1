import pygame

class Instruction_box:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 40
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("Calibri", 25)

        self.rect = pygame.Rect(650, 320, self.width, self.height)

        self.msgImage = self.font.render(msg, True, self.text_color, self.button_color)
        self.msgImage_rect = self.msgImage.get_rect()
        self.msgImage_rect.center = self.rect.center

    def instruction_change(self, msg):
        self.msgImage = self.font.render(msg, True, self.text_color, self.button_color)
        self.msgImage_rect = self.msgImage.get_rect()
        self.msgImage_rect.center = self.rect.center

    def draw_instruction(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msgImage, self.msgImage_rect)

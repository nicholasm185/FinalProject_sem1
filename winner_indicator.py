import pygame
import time

class Winner:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 400, 200
        self.box_color = (0, 127, 255)
        self.txt_box_color = (240, 12, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("Calibri", 60)

        self.rect = pygame.Rect(250, 200, self.width, self.height)

        self.winning_team = ""

        self.win_box = self.font.render(self.winning_team, True, self.text_color, self.txt_box_color)
        self.win_box_rect = self.win_box.get_rect()
        self.win_box_rect.center = self.rect.center

    def show_winner(self, team):
        self.winning_team = team
        self.win_box = self.font.render(self.winning_team, True, self.text_color, self.txt_box_color)
        self.win_box_rect = self.win_box.get_rect()
        self.win_box_rect.center = self.rect.center
        self.screen.fill(self.box_color, self.rect)
        self.screen.blit(self.win_box, self.win_box_rect)
        pygame.display.flip()
        time.sleep(3)

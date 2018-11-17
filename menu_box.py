import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 400, 200
        self.box_color = (255, 255, 255)
        self.txt_box_color = (0, 230, 200)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("Calibri", 40)

        self.rect = pygame.Rect(250, 200, self.width, self.height)

        self.play_button = self.font.render("Play", True, self.text_color, self.txt_box_color)
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (350, 350)

        self.quit_button = self.font.render("Quit", True, self.text_color, self.txt_box_color)
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.center = (550, 350)

    def draw_menu(self):
        self.screen.fill(self.box_color, self.rect)
        self.screen.blit(self.play_button, self.play_button_rect)
        self.screen.blit(self.quit_button, self.quit_button_rect)

import pygame

class Menu:
    def __init__(self, screen, setting):
        # gets the screen and stores the size of the screen
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # sets the width of the background "holder" box
        self.width, self.height = 400, 200
        self.box_color = (255, 255, 255)
        self.txt_box_color = (0, 230, 200)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("Calibri", 40)

        # sets the position and size of the surface
        self.rect = pygame.Rect(250, 200, self.width, self.height)

        # gets the image for the logo, gets its size, and sets its position to the center of the "holder" box
        self.logo_img = setting.logo
        self.logo = pygame.image.load(self.logo_img)
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.center = self.rect.center

        # renders the "Play" button and setting its position
        self.play_button = self.font.render("Play", True, self.text_color, self.txt_box_color)
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (350, 350)

        # renders the "Quit button and sets its position
        self.quit_button = self.font.render("Quit", True, self.text_color, self.txt_box_color)
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.center = (550, 350)

    # draws the menu to the screen
    def draw_menu(self):
        self.screen.fill(self.box_color, self.rect)
        self.screen.blit(self.logo, self.logo_rect)
        self.screen.blit(self.play_button, self.play_button_rect)
        self.screen.blit(self.quit_button, self.quit_button_rect)

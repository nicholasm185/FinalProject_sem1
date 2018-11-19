import pygame.font
import random

class Dice():

    def __init__(self, screen):
        # gets the screen and stores the size of the screen
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # sets the files used for each die face
        self.dieface0 = pygame.image.load(".\\assets\\dieinit.png")
        self.dieface1 = pygame.image.load(".\\assets\\dicefaces-01.png")
        self.dieface2 = pygame.image.load(".\\assets\\dicefaces-02.png")
        self.dieface3 = pygame.image.load(".\\assets\\dicefaces-03.png")
        self.dieface4 = pygame.image.load(".\\assets\\dicefaces-04.png")
        self.dieface5 = pygame.image.load(".\\assets\\dicefaces-05.png")
        self.dieface6 = pygame.image.load(".\\assets\\dicefaces-06.png")

        # sets the "holder" box width, height and color
        self.width, self.height = 200, 200
        self.buttonColor = (255, 255, 255)

        # sets initial value of the dice
        self.value = 0

        # positions of the dice
        self.x = 650
        self.y = 100

        # sets the position and size of the surface
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # sets a random value for the dice
    def roll_dice(self):
        self.value = random.randint(1, 6)

    # draws the corresponding die face for its value
    def draw_dice(self):
        self.screen.fill(self.buttonColor, self.rect)
        if self.value == 0:
            self.screen.blit(self.dieface0, (self.x, self.y))
        elif self.value == 1:
            self.screen.blit(self.dieface1, (self.x, self.y))
        elif self.value == 2:
            self.screen.blit(self.dieface2, (self.x, self.y))
        elif self.value == 3:
            self.screen.blit(self.dieface3, (self.x, self.y))
        elif self.value == 4:
            self.screen.blit(self.dieface4, (self.x, self.y))
        elif self.value == 5:
            self.screen.blit(self.dieface5, (self.x, self.y))
        elif self.value == 6:
            self.screen.blit(self.dieface6, (self.x, self.y))

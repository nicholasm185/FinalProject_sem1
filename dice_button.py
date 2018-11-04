import pygame.font

class Dice():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.dieface0 = pygame.image.load(".\\assets\\dieinit.png")
        self.dieface1 = pygame.image.load(".\\assets\\dicefaces-01.png")
        self.dieface2 = pygame.image.load(".\\assets\\dicefaces-02.png")
        self.dieface3 = pygame.image.load(".\\assets\\dicefaces-03.png")
        self.dieface4 = pygame.image.load(".\\assets\\dicefaces-04.png")
        self.dieface5 = pygame.image.load(".\\assets\\dicefaces-05.png")
        self.dieface6 = pygame.image.load(".\\assets\\dicefaces-06.png")

        self.width, self.height = 200, 200
        self.buttonColor = (255, 255, 255)

        self.rect = pygame.Rect(650, 100, self.width, self.height)
        # self.rect.center = self.screen_rect.center

    def drawButton(self, pion):
        self.screen.fill(self.buttonColor, self.rect)
        if pion.adder == 0:
            self.screen.blit(self.dieface0, (650, 100))
        elif pion.adder == 1:
            self.screen.blit(self.dieface1, (650, 100))
        elif pion.adder == 2:
            self.screen.blit(self.dieface2, (650, 100))
        elif pion.adder == 3:
            self.screen.blit(self.dieface3, (650, 100))
        elif pion.adder == 4:
            self.screen.blit(self.dieface4, (650, 100))
        elif pion.adder == 5:
            self.screen.blit(self.dieface5, (650, 100))
        elif pion.adder == 6:
            self.screen.blit(self.dieface6, (650, 100))

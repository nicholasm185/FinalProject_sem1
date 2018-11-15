import pygame

class Setting():
    def __init__(self):
        self.gameboard = ".\\assets\\ludoladdersboard.png"
        self.rollerboard = ".\\assets\\rollerboard.png"

        self.blues = ".\\assets\\pionblue-01.png"
        self.reds = ".\\assets\\pionred-01.png"

        self.player = 1

        # self.pion1_base = (700, 440)
        # self.pion2_base = (700, 500)

# Anthony Pham - Stack Overflow with removal of unused "Sprite" class inheritance
class Background():
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

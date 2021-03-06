import pygame

# this class is used to store the file path of the assets used
class Setting():
    def __init__(self):
        self.gameboard = ".\\assets\\ludoladdersboard.png"
        self.rollerboard = ".\\assets\\rollerboard.png"

        self.blues = ".\\assets\\pionblue-01.png"
        self.reds = ".\\assets\\pionred-01.png"

        self.logo = ".\\assets\\ludoladderslogo.png"



# Anthony Pham - Stack Overflow with removal of unused "Sprite" class inheritance
# this class refractors the main function
class Background():
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

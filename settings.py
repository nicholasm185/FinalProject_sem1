import pygame

class Setting():
    def __init__(self):
        self.gameboard = ".\\assets\\ludoladdersboard.png"
        self.rollerboard = ".\\assets\\rollerboard.png"



# Anthony Pham - Stack Overflow
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

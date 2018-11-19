import pygame
from pygame.sprite import Sprite
import time

class Pion(Sprite):

    def __init__(self, screen, color):
        # inherits the attributes from Sprite class
        super().__init__()
        # sets the screen
        self.screen = screen

        # loads the image based on the given parameter
        self.image = pygame.image.load(color)
        self.rect = self.image.get_rect()

        # sets the size of the sprite
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # attributes for position of the top left corner of the sprite
        self.x = 0
        self.y = 540

        # the base position is used to bring the pion back to its original base position
        self.base_position_x = 0
        self.base_position_y = 0

        # tile number of the pion
        self.position = 0

        # direction of the pion's movement, 1 for left, 2 for right
        self.direction = 1

        # movement value of the pion
        self.adder = 0

        # False playstatus makes the pion cannot be moved when in base
        self.playstatus = False

        # surface on which the pion can be clicked
        self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)

    # moves the pion with a for loop to create illusion of "hopping" or changes its state and places it on the board
    def update(self, screen, background, own_group, rival_group):
        if self.playstatus == True:
            for i in range(0, self.adder):
                if self.position + self.adder > 100:
                    print("break")
                    break
                else:
                    if self.check_out():
                        self.y -= self.rect.y
                        self.changedir()
                        print("moved up")
                        self.position += 1
                        self.adder -= 1
                    else:
                        self.x += (self.rect.x*self.direction)
                        print("moved")
                        self.position += 1
                        self.adder -= 1
                for pion in own_group:
                    pion.blitme()
                for pion in rival_group:
                    pion.blitme()
                pygame.display.flip()
                screen.blit(background.image, background.rect)
                time.sleep(0.1)
            # updates the pion's new position to its clickable surface
            self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)
            print(self.adder)
            print(self.position)
            print(self.x)
        elif self.playstatus == False and self.adder == 6:
            self.change_state()

    # draws the pion on the screen
    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))

    # checks if the next move is outside the gameboard or not
    def check_out(self):
        if self.x + (self.rect.x*self.direction) > 540:
            return True
        elif self.x + (self.rect.x*self.direction) < 0:
            return True

    # changes the direction of the pion's movement by multiplying its attribute by -1
    def changedir(self):
        self.direction *= -1

    # puts the pion in its base position, resets it tile number, direction, and playstatus
    def put_in_base(self, baseX, baseY):
        self.playstatus = False
        self.position = 0
        self.direction = 1
        self.x = baseX
        self.y = baseY
        self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)
        self.screen.blit(self.image, (baseX, baseY))

    # puts the pion on board, sets playstatus to True, tile position to 1, and updates clickable surface
    def change_state(self):
        self.playstatus = True
        self.x = 0
        self.y = 540
        self.position = 1
        self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)

    # checks if the pion has landed on the bottom of a ladder and places it on top if it does
    def checkladderpos(self):
        if self.position == 2:
            self.x = 120
            self.y = 360
            self.position = 38
            self.changedir()
            self.blitme()
            pygame.display.flip()
        elif self.position == 4:
            self.x = 360
            self.y = 480
            self.position = 14
            self.changedir()
            self.blitme()
            pygame.display.flip()
        elif self.position == 9:
            self.x = 540
            self.y = 360
            self.position = 31
            self.changedir()
            self.blitme()
            pygame.display.flip()
        elif self.position == 33:
            self.x = 240
            self.y = 60
            self.position = 85
            self.changedir()
            self.blitme()
            pygame.display.flip()
        elif self.position == 52:
            self.x = 420
            self.y = 60
            self.position = 88
            self.changedir()
            self.blitme()
            pygame.display.flip()
        elif self.position == 80:
            self.x = 60
            self.y = 0
            self.position = 99
            self.changedir()
            self.blitme()
            pygame.display.flip()
        self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)

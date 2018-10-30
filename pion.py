import pygame
from pygame.sprite import Sprite
import time
import random

class Pion(Sprite):

    def __init__(self, screen, setting):
        super(Pion,self).__init__()
        self.screen = screen

        self.setting = setting

        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(".\\assets\\pion.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = 0
        self.y = 540

        self.position = 1

        self.direction = 1

        self.adder = 0

    def roll(self):
        self.adder = random.randint(1,6)

    def update(self, screen, background):
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
                else:
                    self.x += (self.rect.x*self.direction)
                    print("moved")
                    self.position += 1
            self.blitme()
            pygame.display.flip()
            screen.blit(background.image, background.rect)
            time.sleep(0.1)


        # to do: handle overflow
        # self.position += self.adder
        print(self.adder)
        print(self.position)
        print(self.x)

    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))

    def check_out(self):
        if self.x + (self.rect.x*self.direction) > 540:
            return True
        elif self.x + (self.rect.x*self.direction) < 0:
            return True

    def overflow(self):
        if self.position + self.adder >= 100:
            return True

    def changedir(self):
        self.direction *= -1

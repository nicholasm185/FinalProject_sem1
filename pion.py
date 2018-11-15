import pygame
from pygame.sprite import Sprite
import time
import random
import functions

class Pion(Sprite):

    def __init__(self, screen, setting, color):
        super().__init__()
        self.screen = screen

        self.setting = setting

        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(color)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = 0
        self.y = 540

        self.position = 1

        self.direction = 1

        self.adder = 0

        self.playstatus = False

        self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)

    def roll(self):
        self.adder = random.randint(1,6)

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

                # self.blitme()
                for pion in own_group:
                    pion.blitme()
                for pion in rival_group:
                    pion.blitme()
                pygame.display.flip()
                screen.blit(background.image, background.rect)
                time.sleep(0.1)

            self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)
            print(self.adder)
            print(self.position)
            print(self.x)
        elif self.playstatus == False and self.adder == 6:
            self.change_state()

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

    def put_in_base(self, baseX, baseY):
        self.x = baseX
        self.y = baseY
        self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)
        self.screen.blit(self.image, (baseX, baseY))

    def change_state(self):
        if self.adder == 6:
            self.playstatus = True
            self.x = 0
            self.y = 540
            self.position = 1
            self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)

    def checkladderpos(self, screen, background):
        if self.position == 2:
            self.x = 120
            self.y = 360
            self.position = 38
            self.changedir()
            self.blitme()
            pygame.display.flip()
            screen.blit(background.image, background.rect)
        elif self.position == 4:
            self.x = 360
            self.y = 480
            self.position = 14
            self.changedir()
            self.blitme()
            pygame.display.flip()
            screen.blit(background.image, background.rect)
        elif self.position == 9:
            self.x = 540
            self.y = 360
            self.position = 31
            self.changedir()
            self.blitme()
            pygame.display.flip()
            screen.blit(background.image, background.rect)
        elif self.position == 33:
            self.x = 240
            self.y = 60
            self.position = 85
            self.changedir()
            self.blitme()
            pygame.display.flip()
            screen.blit(background.image, background.rect)
        elif self.position == 52:
            self.x = 420
            self.y = 60
            self.position = 88
            self.changedir()
            self.blitme()
            pygame.display.flip()
            screen.blit(background.image, background.rect)
        elif self.position == 80:
            self.x = 60
            self.y = 0
            self.position = 99
            self.changedir()
            self.blitme()
            pygame.display.flip()
            screen.blit(background.image, background.rect)
        self.click_position = pygame.Rect(self.x, self.y, self.rect.x, self.rect.y)

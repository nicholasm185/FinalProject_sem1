import sys
import pygame
from dice_button import Dice
from settings import Setting

def check_events(screen, background, pion, side_panel, dice):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            roller_clicked(screen, background, pion, side_panel, dice, mouse_x, mouse_y)
            return True

def update_screen(screen, background, pion, side_panel, dice):

    screen.fill((255,255,255))

    pion.roll()

    screen.blit(side_panel.image, side_panel.rect)
    dice.drawButton(pion)
    screen.blit(background.image, background.rect)

    pion.update(screen, background)
    pion.blitme()

    pygame.display.flip()

def init_screen(screen, background, pion1, pion2, side_panel, dice):

    screen.fill((255,255,255))

    screen.blit(side_panel.image, side_panel.rect)
    dice.drawButton(pion1)
    screen.blit(background.image, background.rect)

    pion1.blitme()
    pion2.blitme()

    pygame.display.flip()

def checkwin(pion):
    if pion.position == 100:
        print("you win!")
        sys.exit()

def roller_clicked(screen, background, pion, side_panel, dice, mouse_x, mouse_y):
    button_clicked = dice.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        update_screen(screen, background, pion, side_panel, dice)

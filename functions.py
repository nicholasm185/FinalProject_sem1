import sys
import pygame
from dice_button import Dice
from settings import Setting

def check_events(screen, background, pion, side_panel, dice, rivalpion):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            roller_clicked(screen, background, pion, rivalpion, side_panel, dice, mouse_x, mouse_y)
            return True

def update_screen(screen, background, pion, side_panel, dice, rivalpion):

    screen.fill((255,255,255))

    pion.roll()

    screen.blit(side_panel.image, side_panel.rect)
    dice.drawButton(pion)
    screen.blit(background.image, background.rect)

    pion.update(screen, background, rivalpion)

    pion.checkladderpos(screen, background)

    pygame.display.flip()

def init_screen(screen, background, pion1, pion2, side_panel, dice, turnbox):

    screen.fill((255,255,255))

    turnbox.draw_turnbox()

    screen.blit(side_panel.image, side_panel.rect)
    dice.drawButton(pion1)
    screen.blit(background.image, background.rect)

    pion1.put_in_base(700, 440)
    pion2.put_in_base(700, 500)

    pygame.display.flip()

def checkwin(pion, msg):
    if pion.position == 100:
        print(msg)
        sys.exit()

def roller_clicked(screen, background, pion, rivalpion, side_panel, dice, mouse_x, mouse_y):
    button_clicked = dice.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        update_screen(screen, background, pion, side_panel, dice, rivalpion)

def debugmode(pion):
    pion.position = int(input(""))
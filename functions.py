import sys
import pygame
from dice_button import Dice
from settings import Setting

def check_events(dice):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if roller_clicked(dice, mouse_x, mouse_y):
                return True

def which_pion(pion1, pion2, pion3, pion4):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return pion_clicked(pion1, pion2, pion3, pion4, mouse_x, mouse_y)

def pion_clicked(pion1, pion2, pion3, pion4, mouse_x, mouse_y):
    pion1_clicked = pion1.click_position.collidepoint(mouse_x, mouse_y)
    pion2_clicked = pion2.click_position.collidepoint(mouse_x, mouse_y)
    pion3_clicked = pion3.click_position.collidepoint(mouse_x, mouse_y)
    pion4_clicked = pion4.click_position.collidepoint(mouse_x, mouse_y)
    if pion1_clicked:
        return("Pion1 clicked")
    elif pion2_clicked:
        return("Pion2 clicked")
    elif pion3_clicked:
        return("Pion3 clicked")
    elif pion4_clicked:
        return("Pion4 clicked")

def update_screen(screen, background, pion, side_panel, dice, own_group, rival_group):

    screen.fill((255,255,255))

    pion.adder = dice.value

    screen.blit(side_panel.image, side_panel.rect)

    dice.draw_dice()

    screen.blit(background.image, background.rect)

    pion.update(screen, background, own_group, rival_group)

    pion.checkladderpos(screen, background)

    pygame.display.flip()

def init_screen(screen, background, blue_pions, red_pions, side_panel, dice, turnbox):

    screen.fill((255,255,255))

    turnbox.draw_turnbox()

    screen.blit(side_panel.image, side_panel.rect)
    dice.draw_dice()
    screen.blit(background.image, background.rect)

    x_blue, y_blue = 640, 440
    x_red, y_red = 640, 500
    for pion in blue_pions:
        pion.put_in_base(x_blue, y_blue)
        x_blue += 60

    for pion in red_pions:
        pion.put_in_base(x_red, y_red)
        x_red += 60


    pygame.display.flip()

def dice_roll(dice):
    dice.roll_dice()
    dice.draw_dice()
    pygame.display.flip()

def checkwin(pion, msg):
    if pion.position == 100:
        print(msg)
        sys.exit()

def roller_clicked(dice, mouse_x, mouse_y):
    button_clicked = dice.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        return True

def debugmode(pion):
    pion.position = int(input(""))

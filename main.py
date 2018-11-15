import pygame as py
from pygame.sprite import Group
from settings import Setting
from settings import Background
from pion import Pion
from dice_button import Dice
import functions as func
import time
import os
from turnbox import Turnbox

# Set where the pygame window opens
os.environ['SDL_VIDEO_WINDOW_POS'] = "150,50"

def ludoLadders():
    py.init()

    setting = Setting()
    screen = py.display.set_mode((900, 600))

    gameboard = setting.gameboard
    rollerboard = setting.rollerboard
    turnbox = Turnbox(screen, "Blue goes first!")

    color1 = setting.blues
    color2 = setting.reds

    background = Background(gameboard, [0, 0])
    side_panel = Background(rollerboard, [599, 0])

    dice = Dice(screen)

    pion1 = Pion(screen, setting, color1)
    pion2 = Pion(screen, setting, color1)
    pion3 = Pion(screen, setting, color1)
    pion4 = Pion(screen, setting, color1)

    pion5 = Pion(screen, setting, color2)
    pion6 = Pion(screen, setting, color2)
    pion7 = Pion(screen, setting, color2)
    pion8 = Pion(screen, setting, color2)

    blue_pions = Group()
    red_pions = Group()

    blue_pions.add(pion1,pion2,pion3,pion4)
    red_pions.add(pion5,pion6,pion7,pion8)

    py.display.set_caption("Luddo Ladders")

    func.init_screen(screen, background, blue_pions, red_pions, side_panel, dice, turnbox)

    player = 1

    while True:
        if player == 1:
            turnbox.turn_initiator("Blue's turn!")
            turnbox.draw_turnbox()
            if func.check_events(dice):
                func.dice_roll(dice)
                while True:
                    event = py.event.wait()
                    if event.type == py.MOUSEBUTTONDOWN:
                        if func.which_pion(pion1, pion2, pion3, pion4) == "Pion1 clicked":
                            func.update_screen(screen, background, pion1, side_panel, dice, blue_pions, red_pions)
                            break
                        elif func.which_pion(pion1, pion2, pion3, pion4) == "Pion2 clicked":
                            func.update_screen(screen, background, pion2, side_panel, dice, blue_pions, red_pions)
                            break
                        elif func.which_pion(pion1, pion2, pion3, pion4) == "Pion3 clicked":
                            func.update_screen(screen, background, pion3, side_panel, dice, blue_pions, red_pions)
                            break
                        elif func.which_pion(pion1, pion2, pion3, pion4) == "Pion4 clicked":
                            func.update_screen(screen, background, pion4, side_panel, dice, blue_pions, red_pions)
                            break
                player *= -1
            func.checkwin(pion1, "Blue Wins!")
        if player == -1:
            turnbox.turn_initiator("Red's turn!")
            turnbox.draw_turnbox()
            if func.check_events(dice):
                func.dice_roll(dice)
                while True:
                    event = py.event.wait()
                    if event.type == py.MOUSEBUTTONDOWN:
                        if func.which_pion(pion5, pion6, pion7, pion8) == "Pion1 clicked":
                            func.update_screen(screen, background, pion5, side_panel, dice, red_pions, blue_pions)
                            break
                        elif func.which_pion(pion5, pion6, pion7, pion8) == "Pion2 clicked":
                            func.update_screen(screen, background, pion6, side_panel, dice, blue_pions, red_pions)
                            break
                        elif func.which_pion(pion5, pion6, pion7, pion8) == "Pion3 clicked":
                            func.update_screen(screen, background, pion7, side_panel, dice, blue_pions, red_pions)
                            break
                        elif func.which_pion(pion5, pion6, pion7, pion8) == "Pion4 clicked":
                            func.update_screen(screen, background, pion8, side_panel, dice, blue_pions, red_pions)
                            break
                player *= -1
            func.checkwin(pion2, "Red Wins! ")
        for pion in blue_pions:
            pion.blitme()
        for pion in red_pions:
            pion.blitme()
        py.display.flip()

ludoLadders()

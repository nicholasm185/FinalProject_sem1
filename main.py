import pygame as py
from settings import Setting
from settings import Background
from pion import Pion
from dice_button import Dice
import functions as func
import time
import os
import pygame
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
    pion2 = Pion(screen, setting, color2)

    py.display.set_caption("Luddo Ladders")

    func.init_screen(screen, background, pion1, pion2, side_panel, dice, turnbox)

    player = 1

    while True:
        if player == 1:
            turnbox.turn_initiator("Blue's turn!")
            turnbox.draw_turnbox()
            if func.check_events(screen, background, pion1, side_panel, dice, pion2):
                player *= -1
            func.checkwin(pion1, "Blue Wins!")
        if player == -1:
            turnbox.turn_initiator("Red's turn!")
            turnbox.draw_turnbox()
            if func.check_events(screen, background, pion2, side_panel, dice, pion1):
                player *= -1
            func.checkwin(pion2, "Red Wins! ")
        pion1.blitme()
        pion2.blitme()
        pygame.display.flip()



ludoLadders()

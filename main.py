import pygame as py
from settings import Setting
from settings import Background
from pion import Pion
from dice_button import Dice
import functions as func
import time
import os

# Set where the pygame window opens
os.environ['SDL_VIDEO_WINDOW_POS'] = "150,50"

def ludoLadders():
    py.init()

    setting = Setting()
    gameboard = setting.gameboard
    rollerboard = setting.rollerboard


    background = Background(gameboard, [0,0])
    side_panel = Background(rollerboard, [599,0])
    screen = py.display.set_mode((900,600))

    dice = Dice(screen)

    pion = Pion(screen, setting)
    py.display.set_caption("Luddo Ladders")

    func.init_screen(screen, background, pion, side_panel, dice)

    while True:
        if func.check_events(screen, background, pion, side_panel, dice):
            # func.update_screen(screen, background, pion, side_panel, dice)
            # time.sleep(0.2)
            func.checkwin(pion)

ludoLadders()

import pygame as py
from pygame.sprite import Group
from settings import Setting
from settings import Background
from pion import Pion
from dice_button import Dice
import functions as func
import os
from turnbox import Turnbox
from instruction import Instruction_box
from menu_box import Menu
import sys
from winner_indicator import Winner

# Set where the pygame window opens
os.environ['SDL_VIDEO_WINDOW_POS'] = "150,50"

def ludoLadders():
    py.init()

    #initialize necessary assets for the game
    setting = Setting()
    screen = py.display.set_mode((900, 600))

    gameboard = setting.gameboard
    rollerboard = setting.rollerboard
    menu = Menu(screen, setting)
    turnbox = Turnbox(screen, "")
    instruction_box = Instruction_box(screen, "Roll the dice!")
    winner = Winner(screen)

    color1 = setting.blues
    color2 = setting.reds

    background = Background(gameboard, [0, 0])
    side_panel = Background(rollerboard, [599, 0])

    dice = Dice(screen)

    #initialize pions for each player
    pion1 = Pion(screen, setting, color1)
    pion2 = Pion(screen, setting, color1)
    pion3 = Pion(screen, setting, color1)
    pion4 = Pion(screen, setting, color1)

    pion5 = Pion(screen, setting, color2)
    pion6 = Pion(screen, setting, color2)
    pion7 = Pion(screen, setting, color2)
    pion8 = Pion(screen, setting, color2)

    #initiate groups for the teams
    blue_pions = Group()
    red_pions = Group()

    #putting each pion to their respective teams
    blue_pions.add(pion1,pion2,pion3,pion4)
    red_pions.add(pion5,pion6,pion7,pion8)

    py.display.set_caption("Ludo Ladders")

    func.init_screen(screen, background, blue_pions, red_pions, side_panel, dice, turnbox, instruction_box)

    player = 1
    game_status = False

    while True:
        if game_status == True:
            if player == 1:
                turnbox.turn_initiator("Blue's turn!")
                turnbox.draw_turnbox()
                instruction_box.instruction_change("Roll the dice!")
                instruction_box.draw_instruction()
                if func.check_events(dice):
                    func.dice_roll(dice, blue_pions, red_pions)
                    instruction_box.instruction_change("Choose your pion!")
                    instruction_box.draw_instruction()
                    py.display.flip()
                    while True:
                        event = py.event.wait()
                        if event.type == py.MOUSEBUTTONDOWN:
                            if func.which_pion(pion1, pion2, pion3, pion4) == "Pion1 clicked":
                                func.update_screen(screen, background, pion1, side_panel, dice, blue_pions, red_pions)
                                func.check_eaten(pion1, red_pions)
                                break
                            elif func.which_pion(pion1, pion2, pion3, pion4) == "Pion2 clicked":
                                func.update_screen(screen, background, pion2, side_panel, dice, blue_pions, red_pions)
                                func.check_eaten(pion2, red_pions)
                                break
                            elif func.which_pion(pion1, pion2, pion3, pion4) == "Pion3 clicked":
                                func.update_screen(screen, background, pion3, side_panel, dice, blue_pions, red_pions)
                                func.check_eaten(pion3, red_pions)
                                break
                            elif func.which_pion(pion1, pion2, pion3, pion4) == "Pion4 clicked":
                                func.update_screen(screen, background, pion4, side_panel, dice, blue_pions, red_pions)
                                func.check_eaten(pion4, red_pions)
                                break
                    player *= -1
                func.remove_pion(blue_pions)
                if func.checkwin(blue_pions, "Blue Wins!"):
                    winner.show_winner("Blue Wins!")
                    game_status = False

            elif player == -1:
                turnbox.turn_initiator("Red's turn!")
                turnbox.draw_turnbox()
                instruction_box.instruction_change("Roll the dice!")
                instruction_box.draw_instruction()
                if func.check_events(dice):
                    func.dice_roll(dice, blue_pions, red_pions)
                    instruction_box.instruction_change("Choose your pion!")
                    instruction_box.draw_instruction()
                    py.display.flip()
                    while True:
                        event = py.event.wait()
                        if event.type == py.MOUSEBUTTONDOWN:
                            if func.which_pion(pion5, pion6, pion7, pion8) == "Pion1 clicked":
                                func.update_screen(screen, background, pion5, side_panel, dice, red_pions, blue_pions)
                                func.check_eaten(pion5, blue_pions)
                                break
                            elif func.which_pion(pion5, pion6, pion7, pion8) == "Pion2 clicked":
                                func.update_screen(screen, background, pion6, side_panel, dice, blue_pions, red_pions)
                                func.check_eaten(pion6, blue_pions)
                                break
                            elif func.which_pion(pion5, pion6, pion7, pion8) == "Pion3 clicked":
                                func.update_screen(screen, background, pion7, side_panel, dice, blue_pions, red_pions)
                                func.check_eaten(pion7, blue_pions)
                                break
                            elif func.which_pion(pion5, pion6, pion7, pion8) == "Pion4 clicked":
                                func.update_screen(screen, background, pion8, side_panel, dice, blue_pions, red_pions)
                                func.check_eaten(pion8, blue_pions)
                                break
                    player *= -1
                func.remove_pion(red_pions)
                if func.checkwin(red_pions, "Red Wins! "):
                    winner.show_winner("Red Wins!")
                    game_status = False

            func.draw_pions(blue_pions)
            func.draw_pions(red_pions)
            py.display.flip()

        elif game_status == False:
            menu.draw_menu()
            py.display.flip()
            while True:
                event = py.event.wait()
                if event.type == py.MOUSEBUTTONDOWN:
                    if func.which_button(menu) == 1:
                        print("play")
                        game_status = True
                        blue_pions.add(pion1,pion2,pion3,pion4)
                        red_pions.add(pion5,pion6,pion7,pion8)
                        func.init_screen(screen, background, blue_pions, red_pions, side_panel, dice, turnbox, instruction_box)
                        player = 1
                        break
                    elif func.which_button(menu)== 2:
                        sys.exit()

ludoLadders()

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
    # initialize pygame
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
    pion1 = Pion(screen, color1)
    pion2 = Pion(screen, color1)
    pion3 = Pion(screen, color1)
    pion4 = Pion(screen, color1)

    pion5 = Pion(screen, color2)
    pion6 = Pion(screen, color2)
    pion7 = Pion(screen, color2)
    pion8 = Pion(screen, color2)

    #initiate groups for the teams
    blue_pions = Group()
    red_pions = Group()

    #putting each pion to their respective teams
    blue_pions.add(pion1, pion2, pion3, pion4)
    red_pions.add(pion5, pion6, pion7, pion8)

    # sets window caption
    py.display.set_caption("Ludo Ladders")

    # shows an arranged and clean board before the game starts to avoid a black screen
    func.init_screen(screen, background, blue_pions, red_pions, side_panel, dice, turnbox, instruction_box)

    # initialize the turn and game_status variables
    player = 1
    game_status = False

    while True:
        if game_status == True:
            # this loop goes after the "Play" button in the menu is pressed and is the main loop for the game
            if player == 1:
                # draws the turn sign and instruction
                turnbox.turn_initiator("Blue's turn!")
                turnbox.draw_turnbox()
                instruction_box.instruction_change("Roll the dice!")
                instruction_box.draw_instruction()
                if func.check_events(dice):
                    # rolls the dice and draws a corresponding face while changing the instruction
                    func.dice_roll(dice, blue_pions, red_pions)
                    instruction_box.instruction_change("Choose your pion!")
                    instruction_box.draw_instruction()
                    py.display.flip()
                    while True:
                        # waits for a left mouse button click event
                        event = py.event.wait()
                        if event.type == py.MOUSEBUTTONDOWN:
                            # which_pion checks if the mouse click happens on any of the player's 4 pions
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
                # changes the turn, remove any pions in the 100th tile and checks winning condition
                    player *= -1
                func.remove_pion(blue_pions)
                if func.checkwin(blue_pions, "Blue Wins!"):
                    winner.show_winner("Blue Wins!")
                    game_status = False

            # this is an identical part of the loop for the second player
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

            # draws the pions of each team and updates the screen
            func.draw_pions(blue_pions)
            func.draw_pions(red_pions)
            py.display.flip()

        # this part of the loop allows the display of the menu screen
        elif game_status == False:
            # draws the menu and updates the display
            menu.draw_menu()
            py.display.flip()
            while True:
                # waits for mouse click
                event = py.event.wait()
                if event.type == py.MOUSEBUTTONDOWN:
                    # checks if the "Play" button or "Quit" button has been pressed
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

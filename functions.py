import sys
import pygame

def check_events(dice):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if roller_clicked(dice, mouse_x, mouse_y):
                return True

#return which pion is clicked to the main, allowing for selection of pion
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

#updates the screen but also starts the pion movement function
def update_screen(screen, background, pion, side_panel, dice, own_group, rival_group):

    screen.fill((255,255,255))
    pion.adder = dice.value
    screen.blit(side_panel.image, side_panel.rect)
    dice.draw_dice()
    screen.blit(background.image, background.rect)
    pion.update(screen, background, own_group, rival_group)
    pion.checkladderpos()

    pygame.display.flip()

def init_screen(screen, background, blue_pions, red_pions, side_panel, dice, turnbox, instruction_box):

    screen.fill((255,255,255))

    turnbox.draw_turnbox()
    instruction_box.draw_instruction()

    screen.blit(side_panel.image, side_panel.rect)
    dice.draw_dice()
    screen.blit(background.image, background.rect)

    x_blue, y_blue = 640, 440
    x_red, y_red = 640, 500

    # put pions in respective team in their starting positions
    for pion in blue_pions:
        pion.put_in_base(x_blue, y_blue)
        pion.base_position_x = x_blue
        pion.base_position_y = y_blue
        x_blue += 60

    for pion in red_pions:
        pion.put_in_base(x_red, y_red)
        pion.base_position_x = x_red
        pion.base_position_y = y_red
        x_red += 60

    pygame.display.flip()

def dice_roll(dice, team1, team2):
    dice.roll_dice()
    dice.draw_dice()
    #fixes bug of disappearing pions when clicking dice during movement
    draw_pions(team1)
    draw_pions(team2)

    pygame.display.flip()

#checks the contents of each team's groups, winning condition is when the group is empty
def checkwin(team_group, msg):
    if len(team_group) == 0:
        print(msg)
        return True

#checks if the roller is clicked
def roller_clicked(dice, mouse_x, mouse_y):
    button_clicked = dice.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        return True

# put the pion in an untouchable region of the board to avoid unintended selection of pion
def remove_pion(team_group):
    for pion in team_group:
        if pion.position == 100:
            pion.kill()
            pion.x = -60
            pion.y = -60
            pion.click_position = pygame.Rect(-60, -60, 0, 0)

#refractors pion blitting both in other functions as well as in main
def draw_pions(team_group):
    for pion in team_group:
        pion.blitme()

# returns the eaten pions to their base positions
def check_eaten(pion, rival_group):
    for members in rival_group:
        if members.x == pion.x and members.y == pion.y:
            members.put_in_base(members.base_position_x, members.base_position_y)

def which_button(menu):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return button_clicked(menu, mouse_x, mouse_y)

def button_clicked(menu, mouse_x, mouse_y):
    button1 = menu.play_button_rect.collidepoint(mouse_x, mouse_y)
    button2 = menu.quit_button_rect.collidepoint(mouse_x, mouse_y)
    if button1:
        return 1
    elif button2:
        return 2

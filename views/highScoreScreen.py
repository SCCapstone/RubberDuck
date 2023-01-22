"""summary: running class for high score screen
"""
import pygame
from assets import values
import menuStructure as menuS
import os
from fileio import highScoreIO
import pandas as pd

#from fileio import highScoreIO


# Runs the high score screen
def high_score_screen(noises):
    """summay: running method for screen

    Args:
        noises (SFXHandler): sounds for screen
    """
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "tertiary.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Draw Big Box tall and normal width
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    botLeft = screen.get_height() / 16
    topRight = screen.get_height() / 16 * 15
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (left, botLeft, right - left, topRight - botLeft), 0)

    # Title at top of box centered
    titleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .03))
    title_text_image = titleFont.render("DUCKS IN SPACE", True,
                                        values.COLOR_Purple)
    title_rect = title_text_image.get_rect(center=(screen.get_width() / 2,
                                                   screen.get_height() / 16 *
                                                   2))
    screen.blit(title_text_image, title_rect)

    # Set up font for subtitle
    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .017))
    subtitle_text_image = subtitleFont.render("High Score Board", True,
                                              values.COLOR_Purple)
    subtitle_rect = subtitle_text_image.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 16 * 3))
    screen.blit(subtitle_text_image, subtitle_rect)

    if len(highScoreIO.high_score_board) == 0:
        write_no_high_score(subtitleFont, screen)
    else:
        write_scores_text(subtitleFont, left, right, screen)

    playAgainCords, homeCords, quitCords, widthButton = draw_buttons(
        screen, right, left, subtitleFont)

    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuS.double_click_preventer()
            if event.button == 1:
                # check if mouse is in rect
                if checkCords(playAgainCords, widthButton):
                    noises.playSound("quack")
                elif checkCords(homeCords, widthButton):
                    # go to home screeni
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                elif checkCords(quitCords, widthButton):
                    # quit game
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)


def write_scores_text(subtitleFont, left, right, screen):
    """summary: Prints out all 10 high scores to screen

    Args:
        subtitleFont (Font): Font for high score
        left (float): left cordinate for box
        right (float): right cordinate for box
        screen (Surface): pygame surface to draw on
    """
    # high score board is pd.DataFrame
    # columns are: name, score, date
    # index is 0-9
    #get length of high score board
    length = len(highScoreIO.high_score_board)
    for i in range(length):
        # Put 1-10 in left column
        left_hs_text_image = subtitleFont.render(
            str(i + 1) + ".", True, values.COLOR_Purple)
        # Put name in middle column
        left_2_hs_text_image = subtitleFont.render(
            highScoreIO.high_score_board.iloc[i, 0], True, values.COLOR_Purple)
        # Put score in center column
        center_hs_text_image = subtitleFont.render(
            str(highScoreIO.high_score_board.iloc[i, 1]), True,
            values.COLOR_Purple)
        
        # Put date in right column
        # remove 00:00:00 from date
        date = str(highScoreIO.high_score_board.iloc[i, 2])
        date = date[:10]

        right_hs_text_image = subtitleFont.render(
            str(date), True, values.COLOR_Purple)


        widthOfLeft = left_hs_text_image.get_width() / 2
        widthOfLeftHalf2 = left_2_hs_text_image.get_width() / 2
        widthOfRightHalf = right_hs_text_image.get_width() / 2

        #Position to left of box
        left_hs_rect = left_hs_text_image.get_rect(
            center=(left + 10 + widthOfLeft,
                    screen.get_height() / 16 * (4 + i)))
        left_hs_rect_2 = left_2_hs_text_image.get_rect(
            center=(left + 50 + widthOfLeftHalf2,
                    screen.get_height() / 16 * (4 + i)))
        center_hs_rect = center_hs_text_image.get_rect(
            center=(screen.get_width() / 2,
                    screen.get_height() / 16 * (4 + i)))
        right_hs_rect = right_hs_text_image.get_rect(
            center=(right - 10 - widthOfRightHalf,
                    screen.get_height() / 16 * (4 + i)))

        screen.blit(left_hs_text_image, left_hs_rect)
        screen.blit(left_2_hs_text_image, left_hs_rect_2)
        screen.blit(center_hs_text_image, center_hs_rect)
        screen.blit(right_hs_text_image, right_hs_rect)


def write_no_high_score(subtitleFont, screen):
    """summary: prints out no high scores text

    Args:
        subtitleFont (Font): Font for text
        screen (Surface): Pygame surface to draw on
    """
    hs_text_image = subtitleFont.render("No High Scores", True,
                                        values.COLOR_Purple)
    hs_rect = hs_text_image.get_rect(center=(screen.get_width() / 2,
                                             screen.get_height() / 16 * 4))
    screen.blit(hs_text_image, hs_rect)


def draw_buttons(screen, right, left, subtitleFont):
    """summary: draws 3 buttons for screen

    Args:
        screen (Surface): pygame surface to draw on
        right (float): Right cord for box background
        left (float): Left cord for box background
        subtitleFont (Font): Font for Text

    Returns:
        tuple: cords for play again button
        tuple: cords for home button
        tuple: cords for quit button
        float: width of button
    """
    # Make cordinates for 3 inline buttons
    widthButton = (right - left - 40) / 3
    playAgainCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + playAgainCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    quitCords = (10 + homeCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)

    # Draw Rects for buttons
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (playAgainCords[0], playAgainCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (homeCords[0], homeCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (quitCords[0], quitCords[1], widthButton, 50))

    # Add text to center of buttons
    play_again_text_image = subtitleFont.render("Play Again", True,
                                                values.COLOR_Pink)
    home_text_image = subtitleFont.render("Home", True, values.COLOR_Pink)
    quit_text_image = subtitleFont.render("Quit", True, values.COLOR_Pink)

    screen.blit(play_again_text_image,
                (playAgainCords[0] + widthButton / 2 -
                 play_again_text_image.get_width() / 2, playAgainCords[1] +
                 25 - play_again_text_image.get_height() / 2))
    screen.blit(
        home_text_image,
        (homeCords[0] + widthButton / 2 - home_text_image.get_width() / 2,
         homeCords[1] + 25 - home_text_image.get_height() / 2))
    screen.blit(
        quit_text_image,
        (quitCords[0] + widthButton / 2 - quit_text_image.get_width() / 2,
         quitCords[1] + 25 - quit_text_image.get_height() / 2))

    return playAgainCords, homeCords, quitCords, widthButton


def checkCords(cords, width):
    """summary: Checks if cordinated were clicke

    Args:
        cords (tuple[float,float]): cordinates of button being checked
        width (float): width of a button

    Returns:
        boolean: true if clicked, false if not
    """
    return cords[0] < pygame.mouse.get_pos()[0] < cords[0] + width and cords[
        1] < pygame.mouse.get_pos()[1] < cords[1] + 50

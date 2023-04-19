"""summary: running class for high score screen
"""
import pygame
from assets import values
import menuStructure as menuS
import os
from fileio import highScoreIO
import time
import tkinter
import easygui
from tkinter.filedialog import askdirectory

#from fileio import highScoreIO


# Runs the high score screen
def high_score_screen(noises, gameOver=False, scoreId=-1):
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
    if values.newHighScore:
        title_text_image = titleFont.render("NEW HIGH SCORE", True,
                                            values.COLOR_Red)

    else:
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
        write_scores_text(subtitleFont, left, right, screen, gameOver, scoreId)

    playAgainCords, homeCords, ShareCords, widthButton = draw_buttons(
        screen, right, left, subtitleFont)

    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuS.double_click_preventer()
            if event.button == 1:
                print(event)
                # check if mouse is in rect
                if checkCords(playAgainCords, widthButton):
                    menuS.set_game_menu(menuS.menu.GAME)
                    values.newHighScore = False
                    values.newHighScoreId = -1
                    noises.playSound("quack")
                elif checkCords(homeCords, widthButton):
                    # go to home screeni
                    noises.playSound("quack")
                    values.newHighScore = False
                    values.newHighScoreId = -1
                    menuS.set_game_menu(menuS.menu.HOME)
                elif checkCords(ShareCords, widthButton):
                    noises.playSound("quack")
                    filestring = "high-score-" + time.strftime(
                        "%Y%m%d-%H%M%S") + ".png"
                    # Get Path to save file
                    root = tkinter.Tk()
                    root.withdraw()
                    pygame.display.set_mode(values.SCREEN_SIZE)

                    root.update()
                    #get document path
                    path = askdirectory()

                    high_score_screen(noises, gameOver, scoreId)
                    # check if path is valid
                    if path == "":
                        return
                    path = path + "/" + filestring
                    pygame.image.save(screen, path)
                    easygui.msgbox("Your stats have been saved to " + path,
                                   title="High Score Saved")

        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.HOME)


def write_scores_text(subtitleFont, left, right, screen, gameOver, ScoreId):
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
        Color = values.COLOR_Purple

        if values.newHighScore == True and i == values.newHighScoreId:
            Color = values.COLOR_Red
        elif values.newHighScore == False and i < 3:

            Color = values.COLOR_Red
        # Put 1-10 in left column
        left_hs_text_image = subtitleFont.render(str(i + 1) + ".", True, Color)
        # Put name in middle column
        left_2_hs_text_image = subtitleFont.render(
            highScoreIO.high_score_board.iloc[i, 0], True, Color)
        # Put score in center column
        center_hs_text_image = subtitleFont.render(
            str(highScoreIO.high_score_board.iloc[i, 1]), True, Color)

        # Put date in right column

        #check if date has 00:00:00 if so remove
        #make it string first
        date = str(highScoreIO.high_score_board.iloc[i, 2])
        if date[-8:] == "00:00:00":
            date = date[:-9]

        right_hs_text_image = subtitleFont.render(str(date), True, Color)

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
        tuple: cords for share button
        float: width of button
    """
    # Make cordinates for 3 inline buttons
    widthButton = (right - left - 40) / 3
    playAgainCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + playAgainCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    shareCords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)

    # Draw Rects for buttons
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (playAgainCords[0], playAgainCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (homeCords[0], homeCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (shareCords[0], shareCords[1], widthButton, 50))

    # Add text to center of buttons
    play_again_text_image = subtitleFont.render("Play Again", True,
                                                values.COLOR_Pink)
    home_text_image = subtitleFont.render("Home", True, values.COLOR_Pink)
    share_text_image = subtitleFont.render("Share", True, values.COLOR_Pink)

    screen.blit(play_again_text_image,
                (playAgainCords[0] + widthButton / 2 -
                 play_again_text_image.get_width() / 2, playAgainCords[1] +
                 25 - play_again_text_image.get_height() / 2))
    screen.blit(
        home_text_image,
        (homeCords[0] + widthButton / 2 - home_text_image.get_width() / 2,
         homeCords[1] + 25 - home_text_image.get_height() / 2))
    screen.blit(
        share_text_image,
        (shareCords[0] + widthButton / 2 - share_text_image.get_width() / 2,
         shareCords[1] + 25 - share_text_image.get_height() / 2))

    return playAgainCords, homeCords, shareCords, widthButton


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


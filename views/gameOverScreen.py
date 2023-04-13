#Imports
import datetime
import tkinter
from tkinter.filedialog import askdirectory
import pygame
import os
import menuStructure as menuS
from fileio import settingIO
import time as t
from assets import values
import easygui


def start_screen(noises):
    # Set the background to secondaryScreen (need to work on what will be on
    # Gameover Screen)
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "base_bg.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # font size for Titles = .05
    titleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .05))

    titleFont2 = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .07))

    # font size for subtitle = .03
    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .03))

    # coordinates for drawing
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3

    #GameOver title
    GO_text_image = titleFont2.render("Game Over", True, values.COLOR_Red)
    GOCords = GO_text_image.get_rect(center=(screen.get_width() / 2,
                                             screen.get_height() / 16 * 2))
    screen.blit(GO_text_image, GOCords)

    #4 boxes
    #xCord = screen.get_width() / 3.4
    #yCord = screen.get_height() / 16 * 4
    #width = 700
    #height = 100
    #separation = 50

    # Create 4 bottons with res of screen below
    remainHeight = screen.get_height() - screen.get_height() / 16 * 4
    buttonHeight = (remainHeight - 200) / 4
    buttonWidth = screen.get_width() / 2.3
    buttonX = screen.get_width() / 2 - buttonWidth / 2
    buttonY = screen.get_height() / 16 * 4
    button1 = pygame.Rect(buttonX, buttonY, buttonWidth, buttonHeight)
    button2 = pygame.Rect(buttonX, buttonY + buttonHeight + 50, buttonWidth,
                          buttonHeight)
    button3 = pygame.Rect(buttonX, buttonY + buttonHeight * 2 + 100,
                          buttonWidth, buttonHeight)
    button4 = pygame.Rect(buttonX, buttonY + buttonHeight * 3 + 150,
                          buttonWidth, buttonHeight)

    #Return Home, New Game, Share High Scorem Share Recording

    # Draw the buttons
    pygame.draw.rect(screen, values.COLOR_Pink, button1)
    pygame.draw.rect(screen, values.COLOR_Pink, button2)
    pygame.draw.rect(screen, values.COLOR_Pink, button3)
    pygame.draw.rect(screen, values.COLOR_Pink, button4)

    # Text for buttons
    returnHome_text_image = subtitleFont.render("Return Home", True,
                                                 values.COLOR_Purple)
    #Center on button
    returnHomeCords = returnHome_text_image.get_rect(
        center=(button1.centerx, button1.centery))
    screen.blit(returnHome_text_image, returnHomeCords)

    newGame_text_image = subtitleFont.render("New Game", True,
                                             values.COLOR_Purple)
    #Center on button
    newGameCords = newGame_text_image.get_rect(center=(button2.centerx,
                                                       button2.centery))
    screen.blit(newGame_text_image, newGameCords)

    shareHighScore_text_image = subtitleFont.render("Share Score", True,
                                                    values.COLOR_Purple)

    #Center on button
    shareHighScoreCords = shareHighScore_text_image.get_rect(
        center=(button3.centerx, button3.centery))
    screen.blit(shareHighScore_text_image, shareHighScoreCords)

    shareRecording_text_image = subtitleFont.render("High Score Board", True,
                                                    values.COLOR_Purple)
    #Center on button
    shareRecordingCords = shareRecording_text_image.get_rect(
        center=(button4.centerx, button4.centery))
    screen.blit(shareRecording_text_image, shareRecordingCords)

    # Put Score on right side of screen
    score_text_image = titleFont.render("Score", True, values.COLOR_Red)
    scoreCords = score_text_image.get_rect(center=(button1.left / 2,
                                                   screen.get_height() / 2))
    screen.blit(score_text_image, scoreCords)

    score_val = titleFont.render(str(values.game_score), True,
                                 values.COLOR_Red)
    scoreValCords = score_val.get_rect(center=(button1.left / 2,
                                               scoreCords.bottom + 50))
    screen.blit(score_val, scoreValCords)

    time_text_image = titleFont.render("Time", True, values.COLOR_Red)
    timeCords = time_text_image.get_rect(
        center=((screen.get_width() - button1.right) / 2 + button1.right,
                screen.get_height() / 2))
    screen.blit(time_text_image, timeCords)

    time_val = titleFont.render(str(values.gameTime), True, values.COLOR_Red)
    timeValCords = time_val.get_rect(
        center=((screen.get_width() - button1.right) / 2 + button1.right,
                timeCords.bottom + 50))
    screen.blit(time_val, timeValCords)

    # Coordinates for Home button (removed from top right of screen)
    '''
    homeCords = (values.screenX * .0065, values.screenY * .011)
    if pygame.mouse.get_pos()[0] > homeCords[0] and pygame.mouse.get_pos(
    )[0] < values.screenX * .122 and pygame.mouse.get_pos(
    )[1] > homeCords[1] and pygame.mouse.get_pos()[1] < values.screenY * .06:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Yellow)
    else:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Pink)
    screen.blit(SR_text_image, (homeCords[0], homeCords[1]))
    '''
    
    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuS.double_click_preventer()
            if event.button == 1:
                # check if mouse is in rect
                '''if homeCords[0] < pygame.mouse.get_pos(
                )[0] < homeCords[0] + (right - left - 40) / 3 and homeCords[
                        1] < pygame.mouse.get_pos()[1] < homeCords[1] + 50:
                    # return to home screen
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                '''
                if button1.collidepoint(pygame.mouse.get_pos()):
                    # return home
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                elif button2.collidepoint(pygame.mouse.get_pos()):
                    # new game
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.GAME)
                elif button3.collidepoint(pygame.mouse.get_pos()):
                    # share high score
                    noises.playSound("quack")
                    shareScoreGraphic(values.game_score, values.gameTime)
                elif button4.collidepoint(pygame.mouse.get_pos()):
                    # share recording
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HIGH_SCORE)

        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)

    # Update the screen
    pygame.display.flip()
    pygame.display.update()


def shareScoreGraphic(score, time):
    # Set the screen background
    # Set the background to main.jpg
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "tertiary.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    gameNameFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .075))

    #Center Ducks in Space on Top
    gameName_text_image = gameNameFont.render("Ducks in Space", True,
                                              values.COLOR_White)
    gameNameCords = gameName_text_image.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 4))
    screen.blit(gameName_text_image, gameNameCords)

    # font size for Titles = .05
    titleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .05))

    # Display the score
    score_text_image = titleFont.render("Score: " + str(score), True,
                                        values.COLOR_Yellow)
    scoreCords = score_text_image.get_rect(center=(screen.get_width() / 2,
                                                   screen.get_height() / 2))
    screen.blit(score_text_image, scoreCords)

    # sub info
    subFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .03))

    # Display the time
    time_text_image = subFont.render("Time: " + str(time), True,
                                     values.COLOR_Yellow)
    timeCords = time_text_image.get_rect(center=(screen.get_width() / 2,
                                                 scoreCords.bottom + 50))
    screen.blit(time_text_image, timeCords)

    #Display User
    user_text_image = subFont.render(
        "Player: " + str(settingIO.get_username()), True, values.COLOR_Yellow)
    userCords = user_text_image.get_rect(center=(screen.get_width() / 2,
                                                 timeCords.bottom + 50))
    screen.blit(user_text_image, userCords)

    # Get Date as MM/DD/YYYY HH:MM
    date = datetime.datetime.now().strftime("%m/%d/%Y %H:%M")
    date_text_image = subFont.render("Date: " + str(date), True,
                                     values.COLOR_Yellow)
    dateCords = date_text_image.get_rect(center=(screen.get_width() / 2,
                                                 userCords.bottom + 50))
    screen.blit(date_text_image, dateCords)

    #Clear screen
    filestring = "score-" + t.strftime("%Y%m%d-%H%M%S") + ".png"
    # Get Path to save file
    root = tkinter.Tk()
    root.withdraw()
    pygame.display.set_mode(values.SCREEN_SIZE)

    root.update()
    #make copy of UserSetting.json and move it to desktop
    #get document path
    path = askdirectory()
    # check if path is valid
    if path == "":
        return
    path = path + "/" + filestring

    easygui.msgbox("Your game score have been saved to " + path,
                   title="Score Image Saved")

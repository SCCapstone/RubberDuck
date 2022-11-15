#Imports
import pygame
from assets import values
import menuStructure as menuS
import os
from fileio import highScoreIO

#from fileio import highScoreIO


# TODO - Add a way to load the high scores
def StartLoad():
    pass


# TODO - Add a way to save the high scores
def saveStats():
    pass


# Runs the high score screen
def highScoreScreen(noises):
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
    
    counter = 0
    if len(highScoreIO.getHighScore()) == 0:
        hs_text_image = subtitleFont.render("No High Scores", True,
                                              values.COLOR_Purple)
        hs_rect = hs_text_image.get_rect(
            center=(screen.get_width() / 2, screen.get_height() / 16 * 4))
        screen.blit(hs_text_image,hs_rect)
    else:
        for i in highScoreIO.getHighScore():
        # Positon an Name on Left
            left_hs_text_image = subtitleFont.render(str(i[0]), True,
                                                     values.COLOR_Purple)
            left_2_hs_text_image = subtitleFont.render((i[1]), True,
                                                       values.COLOR_Purple)
            center_hs_text_image = subtitleFont.render(str(i[2]), True,
                                                       values.COLOR_Purple)
            right_hs_text_image = subtitleFont.render(i[3], True,
                                                      values.COLOR_Purple)
            
            widthOfLeft = left_hs_text_image.get_width() / 2
            widthOfLeftHalf2 = left_2_hs_text_image.get_width() / 2
            widthOfRightHalf = right_hs_text_image.get_width() /2
            
            #Position to left of box
            left_hs_rect = left_hs_text_image.get_rect( center=(left + 10 + widthOfLeft , screen.get_height() / 16 * (4 + counter)))
            left_hs_rect_2 = left_2_hs_text_image.get_rect( center=(left + 50 + widthOfLeftHalf2, screen.get_height() / 16 * (4 + counter)))
            center_hs_rect = center_hs_text_image.get_rect( center=(screen.get_width() / 2, screen.get_height() / 16 * (4 + counter)))
            right_hs_rect = right_hs_text_image.get_rect( center=(right - 10 - widthOfRightHalf, screen.get_height() / 16 * (4 + counter)))
        
            screen.blit(left_hs_text_image, left_hs_rect)
            screen.blit(left_2_hs_text_image, left_hs_rect_2)
            screen.blit(center_hs_text_image, center_hs_rect)
            screen.blit(right_hs_text_image, right_hs_rect)
            counter += 1
    

    # Make cordinates for 3 inline buttons
    widthButton = (right - left - 40) / 3
    playAgainCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + playAgainCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    quitCoords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)

    # Draw Rects for buttons
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (playAgainCords[0], playAgainCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (homeCords[0], homeCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (quitCoords[0], quitCoords[1], widthButton, 50))

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
        (quitCoords[0] + widthButton / 2 - quit_text_image.get_width() / 2,
         quitCoords[1] + 25 - quit_text_image.get_height() / 2))
    
   

    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # check if mouse is in rect
                if playAgainCords[0] < pygame.mouse.get_pos(
                )[0] < playAgainCords[0] + widthButton and playAgainCords[
                        1] < pygame.mouse.get_pos(
                        )[1] < playAgainCords[1] + 50:
                    # share stats
                    noises.playSound("quack")
                    pass
                elif homeCords[0] < pygame.mouse.get_pos(
                )[0] < homeCords[0] + widthButton and homeCords[
                        1] < pygame.mouse.get_pos()[1] < homeCords[1] + 50:
                    # go to home screeni
                    noises.playSound("quack")
                    menuS.setGameMenu(menuS.Menu.HOME)
                elif quitCoords[0] < pygame.mouse.get_pos(
                )[0] < quitCoords[0] + widthButton and quitCoords[
                        1] < pygame.mouse.get_pos()[1] < quitCoords[1] + 50:
                    # quit game
                    noises.playSound("quack")
                    menuS.setGameMenu(menuS.Menu.QUIT)
        elif event.type == pygame.QUIT:
            menuS.setGameMenu(menuS.Menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.setGameMenu(menuS.Menu.QUIT)

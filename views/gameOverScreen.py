#Imports
import pygame
import os
import menuStructure as menuS
from assets import values

def start_screen(noises):
    # Set the background to secondaryScreen (need to work on what will be on
    # Gameover Screen)
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "tertiary.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # font size for Titles = .05
    titleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .05))

    # font size for subtitle = .03
    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .03))

    # Draw Big Box tall and normal width
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    botLeft = screen.get_height() / 16
    topRight = screen.get_height() / 16 * 15
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (left, botLeft, right - left, topRight - botLeft), 0)
    
    #GameOver title
    GO_text_image = titleFont.render("Game Over", True, values.COLOR_Red)
    GOCords = GO_text_image.get_rect(center=(screen.get_width() / 2,
                                                   screen.get_height() / 16 *
                                                   2))
    screen.blit(GO_text_image, GOCords)

    #Replay Level
    if pygame.mouse.get_pos()[0] > screen.get_width()/3 +50 and pygame.mouse.get_pos(
    )[0] < screen.get_width()/3 *2 and pygame.mouse.get_pos(
    )[1] > screen.get_height() / 16 * 4 and pygame.mouse.get_pos()[1] < screen.get_height() / 16 * 4 + 60:
        Replay_text_image = subtitleFont.render("Replay Level", True, values.COLOR_Yellow)
    else:
        Replay_text_image = subtitleFont.render("Replay Level", True, values.COLOR_Purple)
    ReplayCords = Replay_text_image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 16 * 4))
    screen.blit(Replay_text_image, ReplayCords)

    #New Game
    if pygame.mouse.get_pos()[0] > screen.get_width()/3 +100 and pygame.mouse.get_pos(
    )[0] < screen.get_width()/3 *2 and pygame.mouse.get_pos(
    )[1] > screen.get_height() / 16 * 6 and pygame.mouse.get_pos()[1] < screen.get_height() / 16 * 6 + 60:
        NewGame_text_image = subtitleFont.render("New Game", True, values.COLOR_Yellow)
    else:
        NewGame_text_image = subtitleFont.render("New Game", True, values.COLOR_Purple)
    NewGameCords = NewGame_text_image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 16 * 6))
    screen.blit(NewGame_text_image, NewGameCords)

    #Share High Score
    if pygame.mouse.get_pos()[0] > screen.get_width()/3 - 50 and pygame.mouse.get_pos(
    )[0] < screen.get_width()/3 *2 and pygame.mouse.get_pos(
    )[1] > screen.get_height() / 16 * 8 and pygame.mouse.get_pos()[1] < screen.get_height() / 16 * 8 + 60:
        high_text_image = subtitleFont.render("Share High Score", True, values.COLOR_Yellow)
    else:
        high_text_image = subtitleFont.render("Share High Score", True, values.COLOR_Purple)
    shareHighCords = high_text_image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 16 * 8))
    screen.blit(high_text_image, shareHighCords)

    #Share Recording
    if pygame.mouse.get_pos()[0] > screen.get_width()/3 -30 and pygame.mouse.get_pos(
    )[0] < screen.get_width()/3 *2 and pygame.mouse.get_pos(
    )[1] > screen.get_height() / 16 * 10 and pygame.mouse.get_pos()[1] < screen.get_height() / 16 * 10 + 60:
        recording_text_image = subtitleFont.render("Share Recording", True, values.COLOR_Yellow)
    else:
        recording_text_image = subtitleFont.render("Share Recording", True, values.COLOR_Purple)
    shareRecordingCords = recording_text_image.get_rect(center=(screen.get_width() / 2, screen.get_height() / 16 * 10))
    screen.blit(recording_text_image, shareRecordingCords)


    # Coordinates Home button
    homeCords = (values.screenX * .0065, values.screenY * .011)
    if pygame.mouse.get_pos()[0] > homeCords[0] and pygame.mouse.get_pos(
    )[0] < values.screenX * .122 and pygame.mouse.get_pos(
    )[1] > homeCords[1] and pygame.mouse.get_pos()[1] < values.screenY * .06:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Yellow)
    else:
        SR_text_image = subtitleFont.render("HOME", True, values.COLOR_Pink)
    screen.blit(SR_text_image, (homeCords[0], homeCords[1]))


    
    # check for mouse click
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menuS.double_click_preventer()
            if event.button == 1:
                # check if mouse is in rect
                if homeCords[0] < pygame.mouse.get_pos(
                )[0] < homeCords[0] + (right - left - 40) / 3 and homeCords[
                        1] < pygame.mouse.get_pos()[1] < homeCords[1] + 50:
                    # return to home screen
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                





        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)

    # Update the screen
    pygame.display.flip()
    pygame.display.update()

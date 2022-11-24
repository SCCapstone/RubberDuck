#Imports
import pygame
import os
import menuStructure as menuS
from assets import values

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
                                                   screen.get_height() / 16 *
                                                   2))
    screen.blit(GO_text_image, GOCords)


    #4 boxes 
    xCord = screen.get_width()/3.4
    yCord = screen.get_height() / 16 * 4
    width = 700
    height = 100
    separation = 50
    
    #Replay Level Box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord,yCord ,width,height ),0)
    #Replay Level text
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord+width and pygame.mouse.get_pos(
    )[1] > yCord and pygame.mouse.get_pos()[1] < yCord + height:
        Replay_text_image = subtitleFont.render("Replay Level", True, values.COLOR_Yellow)
    else:
        Replay_text_image = subtitleFont.render("Replay Level", True, values.COLOR_Purple)
    screen.blit(Replay_text_image, (xCord + 75, yCord + 20))

    #New Game Box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord,yCord + ((height + separation)*1) ,width,height ),0) 
    #New Game text
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord+width and pygame.mouse.get_pos(
    )[1] > (yCord + (height + separation)*1) and pygame.mouse.get_pos()[1] < (yCord+height+ (height + separation)*1):
        NewGame_text_image = subtitleFont.render("New Game", True, values.COLOR_Yellow)
    else:
        NewGame_text_image = subtitleFont.render("New Game", True, values.COLOR_Purple)
    screen.blit(NewGame_text_image, (xCord + 160, yCord +25 +(height + separation)*1 ))

    #Share High Score box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord,yCord + ((height + separation)*2),width,height ),0) 
    #Share High Score text
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord+width and pygame.mouse.get_pos(
    )[1] > (yCord + (height + separation)*2) and pygame.mouse.get_pos()[1] < (yCord+height+ (height + separation)*2):
        high_text_image = subtitleFont.render("Share High Score", True, values.COLOR_Yellow)
    else:
        high_text_image = subtitleFont.render("Share High Score", True, values.COLOR_Purple)
    screen.blit(high_text_image, (xCord , yCord +20 +(height + separation)*2)) 

    #Share Recording Box
    pygame.draw.rect(screen, values.COLOR_Pink,
                     (xCord,yCord + ((height + separation)*3) ,width,height ),0)        
    #Share Recording text
    if pygame.mouse.get_pos()[0] > xCord and pygame.mouse.get_pos(
    )[0] < xCord+width and pygame.mouse.get_pos(
    )[1] > (yCord + (height + separation)*3) and pygame.mouse.get_pos()[1] < (yCord+height+ (height + separation)*3):
        recording_text_image = subtitleFont.render("Share Recording", True, values.COLOR_Yellow)
    else:
        recording_text_image = subtitleFont.render("Share Recording", True, values.COLOR_Purple)
    screen.blit(recording_text_image, (xCord + 10, yCord +20 +(height + separation)*3 ))

    #Show Score
    Score_text = titleFont.render("Score", True, values.COLOR_White)
    screen.blit(Score_text, (values.screenX * .02, yCord +25))
    #TODO Show game score underneath

    #Show Time
    Time_text = titleFont.render("Time", True, values.COLOR_White)
    screen.blit(Time_text, (values.screenX * .75, yCord +25))
    #TODO Show game time underneath


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
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord < pygame.mouse.get_pos()[1] < yCord+height:
                    noises.playSound("quack")
                    #TODO Replay the level
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (height + separation)*1 < pygame.mouse.get_pos()[1] < yCord+height + (height + separation)*1:
                    noises.playSound("quack")
                    #TODO New Game
                    menuS.set_game_menu(menuS.menu.GAME)
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (height + separation)*2 < pygame.mouse.get_pos()[1] < yCord+height + (height + separation)*2:
                    noises.playSound("quack")
                    #TODO Share High Score
                elif xCord < pygame.mouse.get_pos(
                )[0] < xCord + width and yCord + (height + separation)*3< pygame.mouse.get_pos()[1] < yCord+height + (height + separation)*3:
                    noises.playSound("quack")
                    #TODO Share Recording
                





        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.QUIT)

    # Update the screen
    pygame.display.flip()
    pygame.display.update()

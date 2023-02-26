"""summary: FileIO handler for stats
"""
import pygame
from assets import values
import menuStructure as menuS
import os
from fileio import statsIO
from fileio import settingIO
import time
import tkinter
from tkinter.filedialog import askdirectory
import easygui


def start_screen(noises):
    """summary: Starts the stat screen and runs the loop

    Args:
        noises (SFXHandler): SFXHandler object for playing sounds
    """
    # Set the background to main.jpg
    screen = pygame.display.get_surface()

    left, right, subtitleFont = screen_no_button(screen)
    # Make cordinates for 3 inline buttons
    widthButton = (right - left - 40) / 3
    shareCords = (left + 10, screen.get_height() / 16 * 13.5)
    homeCords = (10 + shareCords[0] + widthButton,
                 screen.get_height() / 16 * 13.5)
    quitCoords = (10 + homeCords[0] + widthButton,
                  screen.get_height() / 16 * 13.5)

    # Draw Rects for buttons
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (shareCords[0], shareCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (homeCords[0], homeCords[1], widthButton, 50))
    pygame.draw.rect(screen, values.COLOR_Purple,
                     (quitCoords[0], quitCoords[1], widthButton, 50))

    # Add text to center of buttons
    share_text_image = subtitleFont.render("Share", True, values.COLOR_Pink)
    home_text_image = subtitleFont.render("Home", True, values.COLOR_Pink)
    quit_text_image = subtitleFont.render("Quit", True, values.COLOR_Pink)

    screen.blit(
        share_text_image,
        (shareCords[0] + widthButton / 2 - share_text_image.get_width() / 2,
         shareCords[1] + 25 - share_text_image.get_height() / 2))
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
            menuS.double_click_preventer()
            if event.button == 1:
                # check if mouse is in rect
                if shareCords[0] < pygame.mouse.get_pos(
                )[0] < shareCords[0] + widthButton and shareCords[
                        1] < pygame.mouse.get_pos()[1] < shareCords[1] + 50:
                    # share stats
                    shareStats(screen)
                    noises.playSound("quack")
                elif homeCords[0] < pygame.mouse.get_pos(
                )[0] < homeCords[0] + widthButton and homeCords[
                        1] < pygame.mouse.get_pos()[1] < homeCords[1] + 50:
                    # go to home screeni
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.HOME)
                elif quitCoords[0] < pygame.mouse.get_pos(
                )[0] < quitCoords[0] + widthButton and quitCoords[
                        1] < pygame.mouse.get_pos()[1] < quitCoords[1] + 50:
                    # quit game
                    noises.playSound("quack")
                    menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.QUIT:
            menuS.set_game_menu(menuS.menu.QUIT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menuS.set_game_menu(menuS.menu.HOME)


def shareStats(screen):
    #Clear screen
    filestring = "stat-" + time.strftime("%Y%m%d-%H%M%S") + ".png"
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
    screen.fill(values.COLOR_Black)
    screen_no_button(screen)

    # Put Username where button was
    username = settingIO.Player_Name
    usernameFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .03))
    print(username)
    username_text_image = usernameFont.render(username, True,
                                              values.COLOR_Purple)
    #center text wifth screen

    screen.blit(username_text_image,
                (screen.get_width() / 2 - username_text_image.get_width() / 2,
                 screen.get_height() / 16 * 13.5))
    pygame.image.save(screen, path)
    easygui.msgbox("Your stats have been saved to " + path,
                   title="Stats Saved")


def screen_no_button(screen):
    background = pygame.image.load(
        os.path.join("assets", "backgrounds", "tertiary.jpg"))

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

    subtitleFont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .02))
    subtitle_text_image = subtitleFont.render("Statistics", True,
                                              values.COLOR_Purple)
    subtitle_rect = subtitle_text_image.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 16 * 3))
    screen.blit(subtitle_text_image, subtitle_rect)

    statfont = pygame.font.Font(
        os.path.join("assets", "fonts", "Ethnocentric.ttf"),
        int(values.screenX * .015))

    # Draw the stats on left side of box
    dist_text_image = subtitleFont.render("Distance Traveled", True,
                                          values.COLOR_Red)
    totGames_text_image = subtitleFont.render("Total Games Played", True,
                                              values.COLOR_Red)
    totGameTime_text_image = subtitleFont.render("Total Game Time", True,
                                                 values.COLOR_Red)
    EnemyKills_text_image = subtitleFont.render("Enemy Kills", True,
                                                values.COLOR_Red)
    SpaceKill_text_image = subtitleFont.render("Spaceships Kills", True,
                                               values.COLOR_Red)
    MeteriodKill_text_image = subtitleFont.render("Meteriod Kills", True,
                                                  values.COLOR_Red)
    AllTimeCurrency_text_image = subtitleFont.render("All Time Currency", True,
                                                     values.COLOR_Red)
    AverageGameTime_text_image = subtitleFont.render("Average Game Time", True,
                                                     values.COLOR_Red)
    AveragePoints_text_image = subtitleFont.render("Average Points", True,
                                                   values.COLOR_Red)

    # Draw to screen BELOW STAT lines
    screen.blit(dist_text_image, (left + 10, screen.get_height() / 16 * 4))
    screen.blit(totGames_text_image, (left + 10, screen.get_height() / 16 * 5))
    screen.blit(totGameTime_text_image,
                (left + 10, screen.get_height() / 16 * 6))
    screen.blit(EnemyKills_text_image,
                (left + 10, screen.get_height() / 16 * 7))
    screen.blit(SpaceKill_text_image,
                (left + 10, screen.get_height() / 16 * 8))
    screen.blit(MeteriodKill_text_image,
                (left + 10, screen.get_height() / 16 * 9))
    screen.blit(AllTimeCurrency_text_image,
                (left + 10, screen.get_height() / 16 * 10))
    screen.blit(AverageGameTime_text_image,
                (left + 10, screen.get_height() / 16 * 11))
    screen.blit(AveragePoints_text_image,
                (left + 10, screen.get_height() / 16 * 12))

    # Get Stat Values
    Valdist_text_image = subtitleFont.render(str(statsIO.distanceTravelled),
                                             True, values.COLOR_Red)
    ValtotGames_text_image = subtitleFont.render(str(statsIO.totalGamesPlayed),
                                                 True, values.COLOR_Red)
    #convert to MM:SS
    rounded_total_time = round(statsIO.totalGameTime, 2)
    totTime = time.strftime('%M:%S', time.gmtime(rounded_total_time))
    ValtotGameTime_text_image = subtitleFont.render(str(totTime),
                                                    True, values.COLOR_Red)

    ValEnemyKills_text_image = subtitleFont.render(str(statsIO.enemyDefeated),
                                                   True, values.COLOR_Red)
    ValSpaceKill_text_image = subtitleFont.render(str(statsIO.spaceshipKills),
                                                  True, values.COLOR_Red)
    ValMeteriodKill_text_image = subtitleFont.render(
        str(statsIO.meteroidKills), True, values.COLOR_Red)
    ValAllTimeCurrency_text_image = subtitleFont.render(
        str(statsIO.allTimeCurrency), True, values.COLOR_Red)
    rounded_average_time = round(statsIO.averageGameTime, 2)
    
    avTime = time.strftime('%M:%S', time.gmtime(rounded_average_time))
    ValAverageGameTime_text_image = subtitleFont.render(
        str(avTime), True, values.COLOR_Red)
    rounded_average_points = round(statsIO.averagePoints, 2)
    ValAveragePoints_text_image = subtitleFont.render(
        str(rounded_average_points), True, values.COLOR_Red)

    # Draw to screen RIGHT of STAT lines with 10 buffer on right side
    screen.blit(Valdist_text_image,
                (right - 10 - Valdist_text_image.get_width(),
                 screen.get_height() / 16 * 4))
    screen.blit(ValtotGames_text_image,
                (right - 10 - ValtotGames_text_image.get_width(),
                 screen.get_height() / 16 * 5))
    screen.blit(ValtotGameTime_text_image,
                (right - 10 - ValtotGameTime_text_image.get_width(),
                 screen.get_height() / 16 * 6))
    screen.blit(ValEnemyKills_text_image,
                (right - 10 - ValEnemyKills_text_image.get_width(),
                 screen.get_height() / 16 * 7))
    screen.blit(ValSpaceKill_text_image,
                (right - 10 - ValSpaceKill_text_image.get_width(),
                 screen.get_height() / 16 * 8))
    screen.blit(ValMeteriodKill_text_image,
                (right - 10 - ValMeteriodKill_text_image.get_width(),
                 screen.get_height() / 16 * 9))
    screen.blit(ValAllTimeCurrency_text_image,
                (right - 10 - ValAllTimeCurrency_text_image.get_width(),
                 screen.get_height() / 16 * 10))
    screen.blit(ValAverageGameTime_text_image,
                (right - 10 - ValAverageGameTime_text_image.get_width(),
                 screen.get_height() / 16 * 11))
    screen.blit(ValAveragePoints_text_image,
                (right - 10 - ValAveragePoints_text_image.get_width(),
                 screen.get_height() / 16 * 12))
    return left, right, subtitleFont

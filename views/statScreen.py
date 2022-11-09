import pygame
import json
from assets import values
import menuStructure as menuS
import os
from fileio import statsIO


def StartLoad():
    statsIO.loadStats()


def statScreen():
    # Set the background to main.jpg
    background = pygame.image.load(
        os.path.join(
            "assets",
            "backgrounds",
            "tertiary.jpg"))
    screen = pygame.display.get_surface()
    # scale the background to the screen size
    background = pygame.transform.scale(
        background,
        (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Draw Big Box tall and normal width
    left = screen.get_width() / 4
    right = screen.get_width() / 4 * 3
    botLeft = screen.get_height() / 16
    topRight = screen.get_height() / 16 * 15
    pygame.draw.rect(
        screen,
        values.COLOR_Pink,
        (left,
         botLeft,
         right -
         left,
         topRight -
         botLeft),
        0)

    # Title at top of box centered
    titleFont = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        int(values.screenX * .03))
    title_text_image = titleFont.render(
        "DUCKS IN SPACE", True, values.COLOR_Purple)
    title_rect = title_text_image.get_rect(
        center=(
            screen.get_width() / 2,
            screen.get_height() / 16 * 2))
    screen.blit(title_text_image, title_rect)

    subtitleFont = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        int(values.screenX * .02))
    subtitle_text_image = subtitleFont.render(
        "Statistics", True, values.COLOR_Purple)
    subtitle_rect = subtitle_text_image.get_rect(
        center=(screen.get_width() / 2, screen.get_height() / 16 * 3))
    screen.blit(subtitle_text_image, subtitle_rect)

    statfont = pygame.font.Font(
        os.path.join(
            "assets",
            "fonts",
            "Ethnocentric.ttf"),
        int(values.screenX * .015))

    # Draw the stats on left side of box
    dist_text_image = subtitleFont.render(
        "Distance Traveled", True, values.COLOR_Red)
    totGames_text_image = subtitleFont.render(
        "Total Games Played", True, values.COLOR_Red)
    totGameTime_text_image = subtitleFont.render(
        "Total Game Time", True, values.COLOR_Red)
    EnemyKills_text_image = subtitleFont.render(
        "Enemy Kills", True, values.COLOR_Red)
    SpaceKill_text_image = subtitleFont.render(
        "Spaceships Kills", True, values.COLOR_Red)
    MeteriodKill_text_image = subtitleFont.render(
        "Meteriod Kills", True, values.COLOR_Red)
    AllTimeCurrency_text_image = subtitleFont.render(
        "All Time Currency", True, values.COLOR_Red)
    AverageGameTime_text_image = subtitleFont.render(
        "Average Game Time", True, values.COLOR_Red)
    AveragePoints_text_image = subtitleFont.render(
        "Average Points", True, values.COLOR_Red)

    # Draw to screen BELOW STAT lines
    screen.blit(dist_text_image, (left + 10, screen.get_height() / 16 * 4))
    screen.blit(totGames_text_image, (left + 10, screen.get_height() / 16 * 5))
    screen.blit(
        totGameTime_text_image,
        (left + 10,
         screen.get_height() / 16 * 6))
    screen.blit(
        EnemyKills_text_image,
        (left + 10,
         screen.get_height() / 16 * 7))
    screen.blit(
        SpaceKill_text_image,
        (left + 10,
         screen.get_height() / 16 * 8))
    screen.blit(MeteriodKill_text_image,
                (left + 10, screen.get_height() / 16 * 9))
    screen.blit(AllTimeCurrency_text_image,
                (left + 10, screen.get_height() / 16 * 10))
    screen.blit(AverageGameTime_text_image,
                (left + 10, screen.get_height() / 16 * 11))
    screen.blit(AveragePoints_text_image,
                (left + 10, screen.get_height() / 16 * 12))

    # Get Stat Values
    Valdist_text_image = subtitleFont.render(
        str(statsIO.distanceTravelled), True, values.COLOR_Red)
    ValtotGames_text_image = subtitleFont.render(
        str(statsIO.totalGamesPlayed), True, values.COLOR_Red)
    ValtotGameTime_text_image = subtitleFont.render(
        str(statsIO.totalGameTime), True, values.COLOR_Red)
    ValEnemyKills_text_image = subtitleFont.render(
        str(statsIO.enemyDefeated), True, values.COLOR_Red)
    ValSpaceKill_text_image = subtitleFont.render(
        str(statsIO.spaceshipKills), True, values.COLOR_Red)
    ValMeteriodKill_text_image = subtitleFont.render(
        str(statsIO.meteroidKills), True, values.COLOR_Red)
    ValAllTimeCurrency_text_image = subtitleFont.render(
        str(statsIO.allTimeCurrency), True, values.COLOR_Red)
    ValAverageGameTime_text_image = subtitleFont.render(
        str(statsIO.averageGameTime), True, values.COLOR_Red)
    ValAveragePoints_text_image = subtitleFont.render(
        str(statsIO.averagePoints), True, values.COLOR_Red)

    # Draw to screen RIGHT of STAT lines with 10 buffer on right side
    screen.blit(
        Valdist_text_image,
        (right -
         10 -
         Valdist_text_image.get_width(),
         screen.get_height() /
         16 *
         4))
    screen.blit(
        ValtotGames_text_image,
        (right -
         10 -
         ValtotGames_text_image.get_width(),
         screen.get_height() /
         16 *
         5))
    screen.blit(
        ValtotGameTime_text_image,
        (right -
         10 -
         ValtotGameTime_text_image.get_width(),
         screen.get_height() /
         16 *
         6))
    screen.blit(
        ValEnemyKills_text_image,
        (right -
         10 -
         ValEnemyKills_text_image.get_width(),
         screen.get_height() /
         16 *
         7))
    screen.blit(
        ValSpaceKill_text_image,
        (right -
         10 -
         ValSpaceKill_text_image.get_width(),
         screen.get_height() /
         16 *
         8))
    screen.blit(
        ValMeteriodKill_text_image,
        (right -
         10 -
         ValMeteriodKill_text_image.get_width(),
         screen.get_height() /
         16 *
         9))
    screen.blit(
        ValAllTimeCurrency_text_image,
        (right -
         10 -
         ValAllTimeCurrency_text_image.get_width(),
         screen.get_height() /
         16 *
         10))
    screen.blit(
        ValAverageGameTime_text_image,
        (right -
         10 -
         ValAverageGameTime_text_image.get_width(),
         screen.get_height() /
         16 *
         11))
    screen.blit(
        ValAveragePoints_text_image,
        (right -
         10 -
         ValAveragePoints_text_image.get_width(),
         screen.get_height() /
         16 *
         12))

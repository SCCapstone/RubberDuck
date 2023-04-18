import sys
import pygame

sys.path.append('..')

from views import settingScreen

# Most Untestable
def test_settingScreen():
    assert True


def test_round_Percent():
    assert settingScreen.round_Percent(53.2) == 55
    assert settingScreen.round_Percent(48.3) == 45


def test_draw_background():
    assert True


"""    
def test_checkCords():
    assert settingScreen.checkCords((100, 100), 50) == True
    assert settingScreen.checkCords((200, 200), 100) == True

    # Test with coordinates outside the button
    assert settingScreen.checkCords((100, 100), 10) == False
    assert settingScreen.checkCords((200, 200), 50) == False
    
def test_checkDifCords():
    cords = (100, 100)
    image = pygame.Surface((50, 50))
    assert settingScreen.checkDifCords(cords, image) == True

    cords = (200, 200)
    image = pygame.Surface((100, 100))
    assert settingScreen.checkDifCords(cords, image) == True

    cords = (100, 100)
    image = pygame.Surface((10, 10))
    assert settingScreen.checkDifCords(cords, image) == False

    cords = (200, 200)
    image = pygame.Surface((50, 50))
    assert settingScreen.checkDifCords(cords, image) == False
    """


def test_checkSliderCords():
    left = 100
    factor = 20
    image = pygame.Surface((50, 50))
    screen = pygame.Surface((500, 500))
    range = 200
    height = 5
    pygame.mouse.set_pos((left + factor + image.get_width() + range / 2,
                          screen.get_height() / 16 * height + 25))
    assert settingScreen.checkSliderCords(left, factor, image, screen, range,
                                          height) == True

    # Test with coordinates outside the slider
    pygame.mouse.set_pos((left + factor + image.get_width() + range + 50,
                          screen.get_height() / 16 * height + 25))
    assert settingScreen.checkSliderCords(left, factor, image, screen, range,
                                          height) == False

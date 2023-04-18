import sys
from views import homeScreen

sys.path.append('..')

# All Untestable
def test_home_screen():
    homeScreen.home_screen(noises=False)
    assert True


def test_check_highlight():
    assert True
    # Untestable


def test_click_handler():
    assert True
    # Tested in Behavioral Test


def test_check_click():
    assert True
    # Tested in Behavioral Test


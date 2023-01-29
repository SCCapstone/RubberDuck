#import pytest_bdd methods and feature file for this test
import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from pathlib import Path
#import specific feature file from features folder in test
featureFileDir='features'
featureFile='homeScreen.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)
    
scenario(FEATURE_FILE, 'Start game')

def test_start_game():
    print("End of Start game test")
    pass

@given('Game is loaded')
def current_view():
    #get to home screen
    
@when(the player clicks the 'Start Game' button)
def button_click():
    #click the 'Start Game' button

@then('a new game is started')
def final_view():
    assert 
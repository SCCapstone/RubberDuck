import sys

sys.path.append('..')
#import pytest_bdd methods and feature file for this test
from pytest_bdd import *
import pygame

import menuStructure as menuS
from views import gameOverScreen
from assets import values
from assets import soundHandler

#scenario('../test/features/gameOverScreen.feature', '<scenario name>')
#Use given when then structure for tests
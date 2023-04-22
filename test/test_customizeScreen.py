import sys

from views import customizeScreen
from assets import values
import pygame 
sys.path.append('..')
import os



import pytest

def test_loadAssets():
    # Test that the assets are loaded
    purchaseSize = int(values.screenX * .1504)
    customizeScreen.loadAssets(purchaseSize)
    assert customizeScreen.ownedSkins is not None
    assert customizeScreen.ownedBackgrounds is not None
        
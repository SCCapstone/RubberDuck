import sys

sys.path.append('..')
import os
import pytest

from fileio import customizationIO

def test_load_customization():
    customizationIO.load_new_customization()
    customizationIO.load_customization()
    
    assert customizationIO.skins == []
    assert customizationIO.hats == []
    assert customizationIO.backgrounds == []
    assert customizationIO.coins == 0
    assert customizationIO.current_skin == 0
    assert customizationIO.current_hat == 0
    assert customizationIO.current_background == 0
    
def test_save_customization():
    customizationIO.save_customization()
    assert os.path.exists("fileio\\Customization.json")
    
def test_add_currency():
    customizationIO.load_new_customization()
    customizationIO.add_currency(69)
    assert customizationIO.coins == 69
    

    

    



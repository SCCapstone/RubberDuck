import sys

sys.path.append('..')
import os

from fileio import customizationIO


def test_load_customization():
    # Make backup of customization file
    if os.path.exists("fileio\\Customization.json"):
        os.rename("fileio\\Customization.json",
                  "fileio\\Customization.json.bak")

    customizationIO.load_new_customization()
    customizationIO.load_customization()

    assert customizationIO.skins == []
    assert customizationIO.hats == []
    assert customizationIO.backgrounds == []
    assert customizationIO.coins == 0
    assert customizationIO.current_skin == 0
    assert customizationIO.current_hat == 0
    assert customizationIO.current_background == 0

    # Restore backup of customization file
    if os.path.exists("fileio\\Customization.json.bak"):
        os.remove("fileio\\Customization.json")
        os.rename("fileio\\Customization.json.bak",
                  "fileio\\Customization.json")


def test_load_new_customization():
    if os.path.exists("fileio\\Customization.json"):
        os.rename("fileio\\Customization.json",
                  "fileio\\Customization.json.bak")

    customizationIO.load_new_customization()
    assert customizationIO.skins == []
    assert customizationIO.hats == []
    assert customizationIO.backgrounds == []
    assert customizationIO.coins == 0
    assert customizationIO.current_skin == 0
    assert customizationIO.current_hat == 0
    assert customizationIO.current_background == 0

    if os.path.exists("fileio\\Customization.json.bak"):
        os.remove("fileio\\Customization.json")
        os.rename("fileio\\Customization.json.bak",
                  "fileio\\Customization.json")


def test_save_customization():
    if os.path.exists("fileio\\Customization.json"):
        os.rename("fileio\\Customization.json",
                  "fileio\\Customization.json.bak")

    customizationIO.save_customization()
    assert os.path.exists("fileio\\Customization.json")

    if os.path.exists("fileio\\Customization.json.bak"):
        os.remove("fileio\\Customization.json")
        os.rename("fileio\\Customization.json.bak",
                  "fileio\\Customization.json")


def test_add_currency():
    if os.path.exists("fileio\\Customization.json"):
        os.rename("fileio\\Customization.json",
                  "fileio\\Customization.json.bak")

    customizationIO.load_new_customization()
    customizationIO.add_currency(69)
    assert customizationIO.coins == 69

    if os.path.exists("fileio\\Customization.json.bak"):
        os.remove("fileio\\Customization.json")
        os.rename("fileio\\Customization.json.bak",
                  "fileio\\Customization.json")

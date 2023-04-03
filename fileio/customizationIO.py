import json
import os

global skins, hats, backgrounds
global coins, current_skin, current_hat
global current_background


def load_customization():
    """summary: Loads the customization from the file
    """
    global skins, hats, backgrounds
    global coins, current_skin, current_hat
    global current_background

    try:
        if not os.path.exists("fileio\\Customization.json"):
            load_new_customization()
        data = json.load(open("fileio\\Customization.json"))
        skins = data["skins"]
        hats = data["hats"]
        backgrounds = data["backgrounds"]
        coins = data["coins"]
        current_skin = data["current_skin"]
        current_hat = data["current_hat"]
        current_background = data["current_background"]
    except:
        load_new_customization()


def load_new_customization():
    """summary: Loads the customization from the file
    """
    global skins, hats, backgrounds
    global coins, current_skin, current_hat
    global current_background

    skins = []
    hats = []
    backgrounds = []
    coins = 0
    current_skin = 0
    current_hat = 0
    current_background = 0
    save_customization()


def save_customization():
    """summary: Saves the customization to the file
    """
    global skins, hats, backgrounds
    global coins, current_skin, current_hat
    global current_background
    data = {
        "skins": skins,
        "hats": hats,
        "backgrounds": backgrounds,
        "coins": coins,
        "current_skin": current_skin,
        "current_hat": current_hat,
        "current_background": current_background
    }
    with open("fileio\\Customization.json", "w") as f:
        json.dump(data, f, indent=4)


def add_currency(amount):
    global coins
    coins += amount
    save_customization()

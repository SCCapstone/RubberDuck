"""summary: FileIo handler for settings
"""
import json
import pygame
import shutil
import os
import easygui
import tkinter
from tkinter.filedialog import askopenfilename
from assets import values

global Player_Name, Master_Volume, Music_Volume
global SFX_Volume, Difficulty
global Keymap_Left, Keymap_Right, Keymap_Up
global Keymap_Down, Keymap_Primary_Fire
global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause


def load_settings(path):
    """summary: Loads the settings from the file

    Args:
        path (string): path to the file
    
    Throws:
        IOError: if the file does not exist, will load default settings
    """
    global Player_Name, Master_Volume, Music_Volume
    global SFX_Volume, Difficulty
    global Keymap_Left, Keymap_Right, Keymap_Up
    global Keymap_Down, Keymap_Primary_Fire
    global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause
    try:
        data = json.load(open(path))

        Player_Name = data["Player_Name"]
        Master_Volume = data["Master_Volume"]
        Music_Volume = data["Music_Volume"]
        SFX_Volume = data["SFX_Volume"]
        Difficulty = data["Difficulty"]
        Keymap_Left = data["Keymap_Left"]
        Keymap_Right = data["Keymap_Right"]
        Keymap_Up = data["Keymap_Up"]
        Keymap_Down = data["Keymap_Down"]
        Keymap_Primary_Fire = data["Keymap_Primary_Fire"]
        Keymap_Secondary_Fire = data["Keymap_Secondary_Fire"]
        Keymap_Dash = data["Keymap_Dash"]
        Keymap_Pause = data["Keymap_Pause"]
    except:
        load_default_settings()
        pygame.display.set_caption(
            "Setting File Not Found, Default Setting Loaded")


def save_settings():
    """summary: Saves the settings to the file
    """

    global Player_Name, Master_Volume, Music_Volume
    global SFX_Volume, Difficulty
    global Keymap_Left, Keymap_Right, Keymap_Up
    global Keymap_Down, Keymap_Primary_Fire
    global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause
    data = {
        "Player_Name": Player_Name,
        "Master_Volume": Master_Volume,
        "Music_Volume": Music_Volume,
        "SFX_Volume": SFX_Volume,
        "Difficulty": Difficulty,
        "Keymap_Left": Keymap_Left,
        "Keymap_Right": Keymap_Right,
        "Keymap_Up": Keymap_Up,
        "Keymap_Down": Keymap_Down,
        "Keymap_Primary_Fire": Keymap_Primary_Fire,
        "Keymap_Secondary_Fire": Keymap_Secondary_Fire,
        "Keymap_Dash": Keymap_Dash,
        "Keymap_Pause": Keymap_Pause
    }

    with open("fileio\\UserSetting.json", "w") as f:
        json.dump(data, f, indent=4)


def load_default_settings():
    """summary: Loads the default settings
    """
    global Player_Name, Master_Volume, Music_Volume
    global SFX_Volume, Difficulty
    global Keymap_Left, Keymap_Right, Keymap_Up
    global Keymap_Down, Keymap_Primary_Fire
    global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause

    Player_Name = "Player"
    Master_Volume = 100
    Music_Volume = 100
    SFX_Volume = 100
    Difficulty = "Easy"
    Keymap_Left = pygame.K_a
    Keymap_Right = pygame.K_d
    Keymap_Up = pygame.K_w
    Keymap_Down = pygame.K_s
    Keymap_Primary_Fire = pygame.K_LSHIFT
    Keymap_Secondary_Fire = pygame.K_RSHIFT
    Keymap_Dash = pygame.K_SPACE
    Keymap_Pause = pygame.K_ESCAPE


def import_settings():
    """summary: Imports the settings from the file and asks the user to select the file
    """
    root = tkinter.Tk()
    root.withdraw()
    # Freeze pygame window
    pygame.display.set_mode(values.SCREEN_SIZE)
    filename = askopenfilename()
    root.update()
    if (filename != ""):
        try:
            load_settings(filename)
        except:
            easygui.msgbox("Invalid File", "Error")


def export_settings():
    """_summary_: Exports the settings to the file and asks the user to select the file
    """
    save_settings()

    #make copy of UserSetting.json and move it to desktop
    #get document path
    path = os.path.expanduser("~/Documents")
    path = path + "\\UserSetting.json"
    shutil.copy("fileio\\UserSetting.json", path)

    #display banner message
    easygui.msgbox(
        "UserSetting.json has been exported to your Documents folder",
        "Export Successful")

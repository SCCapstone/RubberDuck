"""summary: FileIo handler for settings
"""
import json
import pygame
import shutil
import easygui
import tkinter
import pygame

from enum import Enum
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from assets import values
from assets import values

global Player_Name, Master_Volume, Music_Volume
global SFX_Volume, DifficultyLevel
global Keymap_Left, Keymap_Right, Keymap_Up
global Keymap_Down, Keymap_Primary_Fire
global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause


class difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


def load_settings(path):
    """summary: Loads the settings from the file

    Args:
        path (string): path to the file
    
    Throws:
        IOError: if the file does not exist, will load default settings
    """
    global Player_Name, Master_Volume, Music_Volume
    global SFX_Volume, DifficultyLevel
    global Keymap_Left, Keymap_Right, Keymap_Up
    global Keymap_Down, Keymap_Primary_Fire
    global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause
    try:
        data = json.load(open(path))

        Player_Name = data["Player_Name"]
        Master_Volume = data["Master_Volume"]
        Music_Volume = data["Music_Volume"]
        SFX_Volume = data["SFX_Volume"]
        Difficulty_pre = data["Difficulty"]
        DifficultyLevel = convertDifficulty(Difficulty_pre)
        Keymap_Left = data["Keymap_Left"]
        Keymap_Right = data["Keymap_Right"]
        Keymap_Up = data["Keymap_Up"]
        Keymap_Down = data["Keymap_Down"]
        Keymap_Primary_Fire = data["Keymap_Primary_Fire"]
        Keymap_Secondary_Fire = data["Keymap_Secondary_Fire"]
        Keymap_Dash = data["Keymap_Dash"]
        Keymap_Pause = data["Keymap_Pause"]
    except:
        print("fialed")
        load_default_settings()
        pygame.display.set_caption(
            "Setting File Not Found, Default Setting Loaded")


def convertDifficulty(difficulty1):
    if difficulty1 == "Easy":
        return difficulty.EASY
    elif difficulty1 == "Medium":
        return difficulty.MEDIUM
    elif difficulty1 == "Hard":
        return difficulty.HARD


def convertDifficultyToText(difficultyE):
    if difficultyE == difficulty.EASY:
        return "Easy"
    elif difficultyE == difficulty.MEDIUM:
        return "Medium"
    elif difficultyE == difficulty.HARD:
        return "Hard"


def save_settings():
    """summary: Saves the settings to the file
    """

    global Player_Name, Master_Volume, Music_Volume
    global SFX_Volume, DifficultyLevel
    global Keymap_Left, Keymap_Right, Keymap_Up
    global Keymap_Down, Keymap_Primary_Fire
    global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause

    dif_text = convertDifficultyToText(DifficultyLevel)

    #Cleans Name Value
    Player_Name = Player_Name.replace("\u001b", "")
    Player_Name = Player_Name.upper()

    data = {
        "Player_Name": Player_Name,
        "Master_Volume": Master_Volume,
        "Music_Volume": Music_Volume,
        "SFX_Volume": SFX_Volume,
        "Difficulty": dif_text,
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
    global Player_Name, Master_Volume, Music_Volume
    global SFX_Volume, DifficultyLevel
    global Keymap_Left, Keymap_Right, Keymap_Up
    global Keymap_Down, Keymap_Primary_Fire
    global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause

    Player_Name = "Player"
    Master_Volume = 100
    Music_Volume = 100
    SFX_Volume = 100
    Difficulty = difficulty.EASY
    Keymap_Left = pygame.K_a
    Keymap_Right = pygame.K_d
    Keymap_Up = pygame.K_w
    Keymap_Down = pygame.K_s
    Keymap_Primary_Fire = pygame.K_LSHIFT
    Keymap_Secondary_Fire = pygame.K_RSHIFT
    Keymap_Dash = pygame.K_SPACE
    Keymap_Pause = pygame.K_ESCAPE


def import_settings():
    root = tkinter.Tk()
    root.withdraw()
    # Freeze pygame window
    pygame.display.set_mode(values.SCREEN_SIZE)
    filename = askopenfilename()
    root.update()
    print(filename)
    if (filename != ""):
        try:
            check_valid_setting_file(filename)
            load_settings(filename)
        except:
            easygui.msgbox("Invalid File", "Error")


def export_settings():
    """_summary_: Exports the settings to the file and asks the user to select the file
    """
    save_settings()

    root = tkinter.Tk()
    root.withdraw()
    pygame.display.set_mode(values.SCREEN_SIZE)
    root.update()
    #make copy of UserSetting.json and move it to desktop
    #get document path
    path = askdirectory()
    path = path + "\\UserSetting.json"
    shutil.copy("fileio\\UserSetting.json", path)

    #display banner message
    easygui.msgbox(
        "UserSetting.json has been exported to" + str(path), 
        "Export Successful")


def check_valid_setting_file(path):

    try:
        if (path == ""):
            easygui.msgbox("Invalid File", "Error")
        if (path[-5:] != ".json"):
            easygui.msgbox("Invalid File Type", "Error")

        #check valid json file
        data = json.load(open(path))
        if (data["Player_Name"] == "" or data["Player_Name"].length() > 10):
            easygui.msgbox("Invalid Player Name", "Error")
        if (data["Master_Volume"] < 0 or data["Master_Volume"] > 100):
            easygui.msgbox("Invalid Master Volume", "Error")
        if (data["Music_Volume"] < 0 or data["Music_Volume"] > 100):
            easygui.msgbox("Invalid Music Volume", "Error")
        if (data["SFX_Volume"] < 0 or data["SFX_Volume"] > 100):
            easygui.msgbox("Invalid SFX Volume", "Error")
        if (data["Difficulty"] != "Easy" and data["Difficulty"] != "Medium" and data["Difficulty"] != "Hard"):
            easygui.msgbox("Invalid Difficulty", "Error")
        if (data["Keymap_Left"] is not int):
            easygui.msgbox("Invalid Keymap Left", "Error")
        if (data["Keymap_Right"] is not int):
            easygui.msgbox("Invalid Keymap Right", "Error")
        if (data["Keymap_Up"] is not int):
            easygui.msgbox("Invalid Keymap Up", "Error")
        if (data["Keymap_Down"] is not int):
            easygui.msgbox("Invalid Keymap Down", "Error")
        if (data["Keymap_Primary_Fire"] is not int):
            easygui.msgbox("Invalid Keymap Primary Fire", "Error")
        if (data["Keymap_Secondary_Fire"] is not int):
            easygui.msgbox("Invalid Keymap Secondary Fire", "Error")
        if (data["Keymap_Dash"] is not int):
            easygui.msgbox("Invalid Keymap Dash", "Error")
        if (data["Keymap_Pause"] is not int):
            easygui.msgbox("Invalid Keymap Pause", "Error")

    except:
        easygui.msgbox("Invalid File", "Error")
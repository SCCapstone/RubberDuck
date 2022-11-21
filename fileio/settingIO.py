import json
import pygame
import shutil
import os
import easygui
import tkinter
from tkinter.filedialog import askopenfilename
import pygame
from assets import values

global Player_Name, Volume, Music, Sound_Effect, Difficulty, Keymap_Left, Keymap_Right, Keymap_Up, Keymap_Down, Keymap_Primary_Fire, Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause


def load_settings(path):
    global Player_Name, Volume, Music, Sound_Effect, Difficulty, Keymap_Left, Keymap_Right, Keymap_Up, Keymap_Down, Keymap_Primary_Fire, Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause
    try:
        data = json.load(open(path))

        Player_Name = data["Player_Name"]
        Volume = data["Volume"]
        Music = data["Music"]
        Sound_Effect = data["Sound_Effect"]
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
    data = {
        "Player_Name": Player_Name,
        "Volume": Volume,
        "Music": Music,
        "Sound_Effect": Sound_Effect,
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


def setPlayerName(name):
    global Player_Name
    Player_Name = name


def setVolume(volume):
    global Volume
    Volume = volume


def setMusic(music):
    global Music
    Music = music


def setSoundEffect(soundEffect):
    global Sound_Effect
    Sound_Effect = soundEffect


def setDifficulty(difficulty):
    global Difficulty
    Difficulty = difficulty


def setKeymapLeft(keymapLeft):
    global Keymap_Left
    Keymap_Left = keymapLeft


def setKeymapRight(keymapRight):
    global Keymap_Right
    Keymap_Right = keymapRight


def setKeymapUp(keymapUp):
    global Keymap_Up
    Keymap_Up = keymapUp


def setKeymapDown(keymapDown):
    global Keymap_Down
    Keymap_Down = keymapDown


def setKeymapPrimaryFire(keymapPrimaryFire):
    global Keymap_Primary_Fire
    Keymap_Primary_Fire = keymapPrimaryFire


def setKeymapSecondaryFire(keymapSecondaryFire):
    global Keymap_Secondary_Fire
    Keymap_Secondary_Fire = keymapSecondaryFire


def setKeymapDash(keymapDash):
    global Keymap_Dash
    Keymap_Dash = keymapDash


def setKeymapPause(keymapPause):
    global Keymap_Pause
    Keymap_Pause = keymapPause


def getPlayerName():
    return Player_Name


def getVolume():
    return Volume


def getMusic():
    return Music


def getSoundEffect():
    return Sound_Effect


def getDifficulty():
    return Difficulty


def getKeymapLeft():
    return Keymap_Left


def getKeymapRight():
    return Keymap_Right


def getKeymapUp():
    return Keymap_Up


def getKeymapDown():
    return Keymap_Down


def getKeymapPrimaryFire():
    return Keymap_Primary_Fire


def getKeymapSecondaryFire():
    return Keymap_Secondary_Fire


def getKeymapDash():
    return Keymap_Dash


def getKeymapPause():
    return Keymap_Pause


def load_default_settings():
    global Player_Name, Volume, Music, Sound_Effect, Difficulty, Keymap_Left, Keymap_Right, Keymap_Up, Keymap_Down, Keymap_Primary_Fire, Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause
    Player_Name = "Player"
    Volume = 100
    Music = True
    Sound_Effect = True
    Difficulty = "Bath Time"
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


def check_valid_setting_file(path):

    try:
        if (path == ""):
            easygui.msgbox("Invalid File", "Error")
        if (path[-5:] != ".json"):
            easygui.msgbox("Invalid File Type", "Error")

        #check valid json file
        data = json.load(open(path))
        if (data["Player_Name"] == ""):
            easygui.msgbox("Invalid File", "Error")
        if (data["Volume"] < 0 or data["Volume"] > 100):
            easygui.msgbox("Invalid File - Volume Invalid Value (Range 1-100)",
                           "Error")
        if (data["Music"] != True and data["Music"] != False):
            easygui.msgbox(
                "Invalid File - Music Invalid Value (TRUE or FALSE)", "Error")
        if (data["Sound_Effect"] != True and data["Sound_Effect"] != False):
            easygui.msgbox(
                "Invalid File - Sound_Effect Invalid Value (TRUE or FALSE)",
                "Error")
        if (data["Difficulty"] != "Bath Time" and data["Difficulty"] != "Easy"
                and data["Difficulty"] != "Normal"
                and data["Difficulty"] != "Hard"):
            easygui.msgbox(
                "Invalid File - Difficulty Invalid Value (\"Bath Time\", \"Easy\", \"Normal\", \"Hard\")",
                "Error")
        if (type(data["Keymap_Left"]) != int):
            easygui.msgbox(
                "Invalid File - Keymap_Left Invalid Value (Integer)", "Error")
        if (type(data["Keymap_Right"]) != int):
            easygui.msgbox(
                "Invalid File - Keymap_Right Invalid Value (Integer)", "Error")
        if (type(data["Keymap_Up"]) != int):
            easygui.msgbox("Invalid File - Keymap_Up Invalid Value (Integer)",
                           "Error")
        if (type(data["Keymap_Down"]) != int):
            easygui.msgbox(
                "Invalid File - Keymap_Down Invalid Value (Integer)", "Error")
        if (type(data["Keymap_Primary_Fire"]) != int):
            easygui.msgbox(
                "Invalid File - Keymap_Primary_Fire Invalid Value (Integer)",
                "Error")
        if (type(data["Keymap_Secondary_Fire"]) != int):
            easygui.msgbox(
                "Invalid File - Keymap_Secondary_Fire Invalid Value (Integer)",
                "Error")
        if (type(data["Keymap_Dash"]) != int):
            easygui.msgbox(
                "Invalid File - Keymap_Dash Invalid Value (Integer)", "Error")
        if (type(data["Keymap_Pause"]) != int):
            easygui.msgbox(
                "Invalid File - Keymap_Pause Invalid Value (Integer)", "Error")
        if (data["Keymap_Left"] == data["Keymap_Right"]
                or data["Keymap_Left"] == data["Keymap_Up"]
                or data["Keymap_Left"] == data["Keymap_Down"]
                or data["Keymap_Left"] == data["Keymap_Primary_Fire"]
                or data["Keymap_Left"] == data["Keymap_Secondary_Fire"]
                or data["Keymap_Left"] == data["Keymap_Dash"]
                or data["Keymap_Left"] == data["Keymap_Pause"]):
            easygui.msgbox(
                "Invalid File - Keymap_Left Invalid Value (Duplicate)",
                "Error")
        if (data["Keymap_Right"] == data["Keymap_Up"]
                or data["Keymap_Right"] == data["Keymap_Down"]
                or data["Keymap_Right"] == data["Keymap_Primary_Fire"]
                or data["Keymap_Right"] == data["Keymap_Secondary_Fire"]
                or data["Keymap_Right"] == data["Keymap_Dash"]
                or data["Keymap_Right"] == data["Keymap_Pause"]):
            easygui.msgbox(
                "Invalid File - Keymap_Right Invalid Value (Duplicate)",
                "Error")
        if (data["Keymap_Up"] == data["Keymap_Down"]
                or data["Keymap_Up"] == data["Keymap_Primary_Fire"]
                or data["Keymap_Up"] == data["Keymap_Secondary_Fire"]
                or data["Keymap_Up"] == data["Keymap_Dash"]
                or data["Keymap_Up"] == data["Keymap_Pause"]):
            easygui.msgbox(
                "Invalid File - Keymap_Up Invalid Value (Duplicate)", "Error")
        if (data["Keymap_Down"] == data["Keymap_Primary_Fire"]
                or data["Keymap_Down"] == data["Keymap_Secondary_Fire"]
                or data["Keymap_Down"] == data["Keymap_Dash"]
                or data["Keymap_Down"] == data["Keymap_Pause"]):
            easygui.msgbox(
                "Invalid File - Keymap_Down Invalid Value (Duplicate)",
                "Error")
        if (data["Keymap_Primary_Fire"] == data["Keymap_Secondary_Fire"]
                or data["Keymap_Primary_Fire"] == data["Keymap_Dash"]
                or data["Keymap_Primary_Fire"] == data["Keymap_Pause"]):
            easygui.msgbox(
                "Invalid File - Keymap_Primary_Fire Invalid Value (Duplicate)",
                "Error")
        if (data["Keymap_Secondary_Fire"] == data["Keymap_Dash"]
                or data["Keymap_Secondary_Fire"] == data["Keymap_Pause"]):
            easygui.msgbox(
                "Invalid File - Keymap_Secondary_Fire Invalid Value (Duplicate)",
                "Error")
        if (data["Keymap_Dash"] == data["Keymap_Pause"]):
            easygui.msgbox(
                "Invalid File - Keymap_Dash Invalid Value (Duplicate)",
                "Error")
    except:
        easygui.msgbox("Invalid File", "Error")

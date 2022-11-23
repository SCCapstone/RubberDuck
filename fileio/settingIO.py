import json
import pygame
import shutil
import os
import easygui

global Player_Name, Master_Volume, Music_Volume
global SFX_Volume, Difficulty
global Keymap_Left, Keymap_Right, Keymap_Up
global Keymap_Down, Keymap_Primary_Fire
global Keymap_Secondary_Fire, Keymap_Dash, Keymap_Pause


def load_settings(path):
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


def setPlayerName(name):
    global Player_Name


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
    #fn = askopenfilename()
    fn = "fileio\\UserSetting.json"
    print("user chose", fn)
    #check if file is valid setting file
    if fn[-5:] != ".json":
        pygame.display.set_caption("Invalid File")
    else:
        load_settings(fn)


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
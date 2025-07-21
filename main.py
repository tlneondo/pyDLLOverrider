import os
import sys
from pathlib import Path
from utils import keyvalues

import requests


#https://medium.com/codex/scraping-information-of-all-games-from-steam-with-python-6e44eb01a299

#expect directory, but if null pass the cwd
gamedir = None


if len(sys.argv = 2):
    gamedir = sys.argv[0]
elif len(sys.argv = 1):
    gamedir = os.getcwd()
else: exit


steamGameID = matchSteamID(gamedir)

def matchSteamID(title):
    """
    Matches the Steam ID of a game title.
    
    THIS IS COPILOT GENERATED WHAT THE FUCK, this is the devil

    :param title: The title of the game to match.
    :return: The Steam ID if found, otherwise None.
    """
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for app in data['applist']['apps']:
            if app['name'].lower() == title.lower():
                return app['appid']
    return None


def matchManifest():
    os.chdir(gamedir)
    oc.chdir("../../")
    acfdir = os.getcwd()



    files = [x for x in os.listdir(acfdir) if x.endswith(".acf")]

    for file in files:
        if (file.find)



        








def matchSteamDepots():


def getVanillaDLLList():


def overrideNewDLLs():





#match to appmanifest file

#match what steam api depos are installed

#filter out pwd level .dll files should be in the folder
#compare to what dll files are in the folder currently 

#query user which dlls need to be overridden
#write DLL overrides to registry or write WINEDLLOVERRIDES env variable in steam launch options

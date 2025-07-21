import os
import sys
from pathlib import Path
from utils import keyvalues

#expect directory, but if null pass the cwd

if len(sys.arv = 2):
    gamedir = sys.argv[0]
elif(sys.arv = 1):
    gamedir = os.getcwd()
else: exit
     




#empty slot for acf file
acffile = None

folderDlls = None


def matchManifest():

    os.chdir('../../')

    for o in path.rglob('*.acf')
        if o.is_file():
            text = o.read_text()
            if gamedir in text:
                println("acf found")
                acffile = o


def matchSteamDepots():

        os.chdir(gamedir)

    for o in path.rglob(".dll")
        if o.is_file():


def getVanillaDLLList():


def overrideNewDLLs():





#match to appmanifest file

#match what steam api depos are installed

#filter out pwd level .dll files should be in the folder
#compare to what dll files are in the folder currently 

#query user which dlls need to be overridden
#write DLL overrides to registry or write WINEDLLOVERRIDES env variable in steam launch options

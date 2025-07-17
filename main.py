import os
from pathlib import Path
from utils import keyvalues

#given working directory which contains the game
#pull directory name
gamedir = os.getcwd()
#empty slot for acf file
acffile = None

#match to appmanifest file

os.chdir('../../')

for o in path.rglob('*.acf')
    if o.is_file():
        text = o.read_text()
            if gamedir in text:
                println("acf found")
                acffile = o
                


#match what steam api depos are installed



#filter out pwd level .dll files should be in the folder


#compare to what dll files are in the folder currently 
 

#query user which dlls need to be overridden


#write DLL overrides to registry or write WINEDLLOVERRIDES env variable in steam launch options

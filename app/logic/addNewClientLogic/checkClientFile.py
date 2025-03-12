from app.logic.readJSONfile import readJSONFile
import os

p = os.path

def checkClientFile():
    pathFile = readJSONFile("app/logic/parameters","pathClientFile")

    if pathFile is None :
        return False
    else :
        if p.exists(pathFile) :
            return True
        else :
            return False
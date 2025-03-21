from app.logic.addNewClientLogic.checkClientFile import checkClientFile
from app.logic.readJSONfile import readJSONFile
from app.logic.addNewClientLogic.createFileStructure import createFileStructure
from app.logic.addNewClientLogic.createPDF import createPDF
from app.logic.changeView import changeView
from app.logic.addGroupInJSONFile import addGroupInJSONFile
from app.logic.addMessage import addMessage
import sys
import os

p = os.path

def addNewClient(groupInfo,stackedWidget,layout):
    
    if checkClientFile is False :
        return "Client File is not or badly defined"
    
    pathFile = readJSONFile("app/logic/parameters","pathClientFile")
    pathFileGroup = pathFile+"/"+groupInfo["groupName"]

    if p.exists(pathFileGroup) :
        sys.exit("Ce client existe déjà")
        addMessage(layout,"Ce client existe déjà.")
    else :
        os.mkdir(pathFileGroup)
        check = addGroupInJSONFile(groupInfo)
        if check["error"] is False :
            createFileStructure(pathFileGroup)
        print(check["message"])
        addMessage(layout,check["message"])


    textPDF = f"""Le groupe {groupInfo["groupName"]}
Fondé en {groupInfo["beginningYear"]}
est composé de :
{"\n".join(groupInfo["members"])}
    """

    createPDF(pathFileGroup+"/Informations_Groupe.pdf",textPDF)

    groupInfo["groupName"] = ""
    groupInfo["beginningYear"] =""
    groupInfo["members"].clear()

    changeView(stackedWidget,"main")



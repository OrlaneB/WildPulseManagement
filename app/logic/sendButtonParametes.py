from app.logic.readJSONfile import readJSONFile
from app.logic.changeView import changeView

def sendButtonParameters(value,stackedWidget) :
    readJSONFile("app/logic/parameters","pathClientFile",value)
    changeView(stackedWidget,"main")

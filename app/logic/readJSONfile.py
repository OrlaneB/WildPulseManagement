import json
from app.logic.getJSONPath import getJSONPath

def readJSONFile (name,path,value=None):
    with open(getJSONPath(),"r",encoding="utf-8") as file:
        data = json.load(file)

    if value is None :
        return data[path]
    else :
        data[path] = value
        print(value)
        with open(getJSONPath(),"w",encoding="utf-8") as file :
            json.dump(data,file,indent=4)
        
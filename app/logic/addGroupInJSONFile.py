import json

def addGroupInJSONFile (groupInfo):
    with open("app/logic/parameters.json","r",encoding="utf-8") as file:
        data = json.load(file)

    print(data)
    groupsJSON = data["groups"]

    #On vérifie que le groupe n'existe pas.
    if any(group.groupName==groupInfo["groupName"] for group in groupsJSON) :
        return {"error":True,"message":"Le groupe existe déjà"}
    
    groupsJSON.append(groupInfo)

    with open("app/logic/parameters.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4)
        return {"error":False,"message":"Nouveau groupe dans paramètres"}


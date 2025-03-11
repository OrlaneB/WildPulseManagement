import json

def readJSONFile (name,path,value=None):
    with open(name+".json","r",encoding="utf-8") as file:
        data = json.load(file)

    if value is None :
        return data[path]
    else :
        data[path] = value
        print(value)
        with open(name+".json","w",encoding="utf-8") as file :
            json.dump(data,file,indent=4)
        print (f"{name} updated successfully !")
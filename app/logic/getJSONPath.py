import sys
import os

def getJSONPath():
    if getattr(sys,"frozen",False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(base_path,"parameters.json")
    print(path)
    return path
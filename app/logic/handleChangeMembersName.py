def handleChangeMembersName (inputFields,groupInfo):
    newMembers = []
    for input in inputFields :
        newMembers.append(input.text())

    groupInfo["members"]=newMembers
def choosingAGroup(group,widget,newWidget,dict):
    for key,value in group.items():
        dict[key]=value
    widget.hide()
    newWidget.show()
    print(dict)
    
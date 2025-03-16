from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QWidget
from app.logic.readJSONfile import readJSONFile
from app.logic.changeView import changeView
from app.logic.addMessage import addMessage
import json

class groupChoice(QWidget):
    def __init__(self,stackedWidget,newClientView,callback,dict,newWidget) :
        super().__init__()
        self.layout = QVBoxLayout()
        self.callback = callback
        self.dict = dict
        self.newWidget = newWidget

        self.layout.addWidget(QLabel("Choisis un groupe"))

        
        newGroupButton = QPushButton("Créer un nouveau client")
        newGroupButton.clicked.connect(lambda:changeView(stackedWidget,newClientView))
        self.layout.addWidget(newGroupButton)

        self.setLayout(self.layout)


    def showEvent(self,event):
        super().showEvent(event)

        while self.layout.count()>1:
            item = self.layout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()


        groups = readJSONFile("app/logic/parameters","groups")

        addMessage(self.layout, json.dumps(groups, indent=2))


        for group in groups:
            button = QPushButton(group["groupName"])
            button.clicked.connect(lambda checked=False, g=group: self.callback(g,self,self.newWidget,self.dict))
            self.layout.addWidget(button)


    

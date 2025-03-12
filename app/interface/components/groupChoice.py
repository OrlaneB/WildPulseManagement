from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QWidget
from app.logic.readJSONfile import readJSONFile
from app.logic.changeView import changeView

class groupChoice(QWidget):
    def __init__(self,stackedWidget,newClientView,callback,dict,newWidget) :
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Choisis un groupe"))

        groups = readJSONFile("app/logic/parameters","groups")

        for group in groups:
            button = QPushButton(group["groupName"])
            button.clicked.connect(lambda checked=False, g=group: callback(g,self,newWidget,dict))
            layout.addWidget(button)

        newGroupButton = QPushButton("Créer un nouveau client")
        newGroupButton.clicked.connect(lambda:changeView(stackedWidget,newClientView))
        layout.addWidget(newGroupButton)

        self.setLayout(layout)

    

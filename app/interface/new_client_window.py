from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from app.logic.changeView import changeView
from app.logic.addNewInput import addNewInput
from app.logic.handleChangeMembersName import handleChangeMembersName
from app.logic.addNewClient import addNewClient

class NewClientWindow(QWidget) :
    def __init__(self,stackedWidget):
        super().__init__()
        self.setWindowTitle("Nouveau client")

        layout = QVBoxLayout()

        backButton = QPushButton("Retour")
        backButton.clicked.connect(lambda:changeView(stackedWidget,"main"))
        layout.addWidget(backButton)

        groupInfo = {
            "groupName":"",
            "members":[],
            "beginningYear":""
        }


        layout.addWidget(QLabel("Nom du groupe"))
        inputGroupName = QLineEdit()
        inputGroupName.setText(groupInfo["groupName"])
        inputGroupName.textChanged.connect(lambda text: groupInfo.__setitem__("groupName", text))
        layout.addWidget(inputGroupName)

        layout.addWidget(QLabel("Année de formation"))
        inputBeginningYear = QLineEdit()
        inputBeginningYear.setText(groupInfo["beginningYear"])
        inputBeginningYear.textChanged.connect(lambda text: groupInfo.__setitem__("beginningYear", text))
        layout.addWidget(inputBeginningYear)



        layout.addWidget(QLabel("Membre(s) du groupe"))

        inputFields = []

        moreButton = QPushButton("Ajouter un membre")
        moreButton.clicked.connect(lambda:addNewInput(layout,groupInfo,inputFields))
        layout.addWidget(moreButton)


        inputMember = QLineEdit()
        inputFields.append(inputMember)
        inputMember.textChanged.connect(lambda: handleChangeMembersName(inputFields,groupInfo))
        layout.addWidget(inputMember)

        sendButton = QPushButton("Créer nouveau client")
        sendButton.clicked.connect(lambda:addNewClient(groupInfo,stackedWidget,layout))
        layout.addWidget(sendButton)

        

        self.setLayout(layout)


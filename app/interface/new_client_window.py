from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from app.logic.changeView import changeView
from app.logic.addNewInput import addNewInput
from app.logic.handleChangeMembersName import handleChangeMembersName
from app.logic.addNewClient import addNewClient
from PySide6.QtCore import Qt

class NewClientWindow(QWidget) :
    def __init__(self,stackedWidget):
        super().__init__()
        self.setWindowTitle("Nouveau client")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        header = QHBoxLayout()
        layout.addLayout(header)

        backButton = QPushButton("Retour")
        backButton.clicked.connect(lambda:changeView(stackedWidget,"main"))
        header.addWidget(backButton)

        header.addStretch(1)

        header.addWidget(QLabel("Créer un nouveau client"))

        groupInfo = {
            "groupName":"",
            "members":[],
            "beginningYear":""
        }

        formLayout = QVBoxLayout()
        formLayout.setAlignment(Qt.AlignHCenter)
        layout.addLayout(formLayout)


        formLayout.addWidget(QLabel("Nom du groupe"))
        inputGroupName = QLineEdit()
        inputGroupName.setText(groupInfo["groupName"])
        inputGroupName.textChanged.connect(lambda text: groupInfo.__setitem__("groupName", text))
        formLayout.addWidget(inputGroupName)

        formLayout.addWidget(QLabel("Année de formation"))
        inputBeginningYear = QLineEdit()
        inputBeginningYear.setText(groupInfo["beginningYear"])
        inputBeginningYear.textChanged.connect(lambda text: groupInfo.__setitem__("beginningYear", text))
        formLayout.addWidget(inputBeginningYear)



        formLayout.addWidget(QLabel("Membre(s) du groupe"))

        inputFields = []

        moreButton = QPushButton("Ajouter un membre")
        moreButton.clicked.connect(lambda:addNewInput(inputMembersLayout,groupInfo,inputFields))
        formLayout.addWidget(moreButton)

        inputMembersLayout = QVBoxLayout()
        formLayout.addLayout(inputMembersLayout)

        inputMember = QLineEdit()
        inputFields.append(inputMember)
        inputMember.textChanged.connect(lambda: handleChangeMembersName(inputFields,groupInfo))
        inputMembersLayout.addWidget(inputMember)

        sendButton = QPushButton("Créer nouveau client")
        sendButton.clicked.connect(lambda:addNewClient(groupInfo,stackedWidget,layout))
        formLayout.addWidget(sendButton)

        

        self.setLayout(layout)


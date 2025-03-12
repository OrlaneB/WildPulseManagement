from PySide6.QtWidgets import QWidget,QVBoxLayout, QLineEdit, QLabel, QPushButton
from app.logic.createContractLogic.createPDF import createPDF
from app.logic.changeView import changeView

class contractInfo(QWidget):
    def __init__(self,contractInfo,stackedWidget):
        super().__init__()
        layout = QVBoxLayout()

        form_data = {
            "contractDate":"Date du contrat",
            "preavis":"Durée du préavis",
            "groupAdress":"Adresse du groupe",
            "commission":"Commission (en %)",
            "specificConditions":"Conditions spécifiques"
        }

        def handleChangeInput(key,value):
            contractInfo[key]=value

        for key,value in form_data.items() :
            layout.addWidget(QLabel(value))
            newInput = QLineEdit()
            newInput.textChanged.connect(lambda text, k=key:handleChangeInput(k,text))
            layout.addWidget(newInput)
            
        def handleClickedButton ():
            createPDF(contractInfo)
            changeView(stackedWidget,"main")


        sendButton = QPushButton("Créer le contrat")
        sendButton.clicked.connect(handleClickedButton)
        layout.addWidget(sendButton)


        self.setLayout(layout)
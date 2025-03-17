from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton,QLabel, QHBoxLayout
from app.logic.changeView import changeView
from app.interface.components.groupChoice import groupChoice
from app.logic.createContractLogic.choosingAGroup import choosingAGroup
from app.interface.components.contractInfo import contractInfo
from PySide6.QtCore import Qt
 
class ContractWindow(QWidget) :
    def __init__(self,stackedWidget,newClientView):
        super().__init__()
        self.setWindowTitle("Nouveau contrat")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        header = QHBoxLayout()
        layout.addLayout(header)

        backButton = QPushButton("Retour")
        backButton.clicked.connect(lambda:changeView(stackedWidget,"main"))
        header.addWidget(backButton)

        header.addStretch(1)

        header.addWidget(QLabel("Nouveau contrat"))

        formLayout = QVBoxLayout()
        formLayout.setAlignment(Qt.AlignHCenter)
        layout.addLayout(formLayout)

        neededInfo = {}

        contractInfoWidget = contractInfo(neededInfo,stackedWidget)
        groupChoiceWidget = groupChoice(stackedWidget,newClientView,choosingAGroup,neededInfo,contractInfoWidget)
        formLayout.addWidget(groupChoiceWidget)
        formLayout.addWidget(contractInfoWidget)
        contractInfoWidget.hide()


        self.setLayout(layout)

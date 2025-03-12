from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton,QLabel
from app.logic.changeView import changeView
from app.interface.components.groupChoice import groupChoice
from app.logic.createContractLogic.choosingAGroup import choosingAGroup
from app.interface.components.contractInfo import contractInfo
 
class ContractWindow(QWidget) :
    def __init__(self,stackedWidget,newClientView):
        super().__init__()
        self.setWindowTitle("Nouveau contrat")

        layout = QVBoxLayout()

        backButton = QPushButton("Retour")
        backButton.clicked.connect(lambda:changeView(stackedWidget,"main"))
        layout.addWidget(backButton)

        layout.addWidget(QLabel("Nouveau contrat"))

        neededInfo = {}

        contractInfoWidget = contractInfo(neededInfo,stackedWidget)
        groupChoiceWidget = groupChoice(stackedWidget,newClientView,choosingAGroup,neededInfo,contractInfoWidget)
        layout.addWidget(groupChoiceWidget)
        layout.addWidget(contractInfoWidget)
        contractInfoWidget.hide()


        self.setLayout(layout)

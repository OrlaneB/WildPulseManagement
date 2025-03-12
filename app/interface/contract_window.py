from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton,QLabel
from app.logic.changeView import changeView

class ContractWindow(QWidget) :
    def __init__(self,stackedWidget):
        super().__init__()
        self.setWindowTitle("Nouveau contrat")

        layout = QVBoxLayout()

        backButton = QPushButton("Retour")
        backButton.clicked.connect(lambda:changeView(stackedWidget,"main"))
        layout.addWidget(backButton)

        layout.addWidget(QLabel("Nouveau contrat"))

        self.setLayout(layout)

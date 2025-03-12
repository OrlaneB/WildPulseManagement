from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel,QPushButton
from app.logic.clickedButtonDemo import clickedButtonDemo
from app.logic.changeView import changeView

def createMainView(stackedWidget, views) :
    mainWidget = QWidget()

    layout = QVBoxLayout()

    # Header
    label = QLabel("Wild Pulse Management")
    layout.addWidget(label)

    paramButton = QPushButton("Paramètres")
    paramButton.clicked.connect(lambda :changeView(stackedWidget,views["paramView"]))
    layout.addWidget(paramButton)

    # Button
    button = QPushButton("Nouveau client")
    button.clicked.connect(lambda: changeView(stackedWidget,views["newClientView"]))
    layout.addWidget(button)

    contractButton = QPushButton("Nouveau contrat")
    contractButton.clicked.connect(lambda: changeView(stackedWidget, views["contractView"]))
    layout.addWidget(contractButton)

    mainWidget.setLayout(layout)
    return mainWidget

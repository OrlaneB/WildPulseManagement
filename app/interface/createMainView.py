from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel,QPushButton, QHBoxLayout
from app.logic.clickedButtonDemo import clickedButtonDemo
from PySide6.QtCore import Qt
from app.logic.changeView import changeView

def createMainView(stackedWidget, views) :
    mainWidget = QWidget()

    layout = QVBoxLayout()

    header = QHBoxLayout()
    layout.setAlignment(Qt.AlignTop)
    layout.addLayout(header)

    # Header
    label = QLabel("Wild Pulse Management")
    label.setProperty("class","TitleFont")
    header.addWidget(label)

    header.addStretch(1)

    paramButton = QPushButton("Paramètres")
    paramButton.clicked.connect(lambda :changeView(stackedWidget,views["paramView"]))
    header.addWidget(paramButton)


    buttonLayout = QVBoxLayout()
    buttonLayout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
    layout.addLayout(buttonLayout)

    # Button
    button = QPushButton("Nouveau client")
    button.clicked.connect(lambda: changeView(stackedWidget,views["newClientView"]))
    buttonLayout.addWidget(button)

    contractButton = QPushButton("Nouveau contrat")
    contractButton.clicked.connect(lambda: changeView(stackedWidget, views["contractView"]))
    buttonLayout.addWidget(contractButton)

    mainWidget.setLayout(layout)
    return mainWidget

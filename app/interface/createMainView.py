from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel,QPushButton
from app.logic.clickedButtonDemo import clickedButtonDemo
from app.logic.changeView import changeView

def createMainView(stackedWidget, paramView) :
    mainWidget = QWidget()

    layout = QVBoxLayout()

    # Header
    label = QLabel("Wild Pulse Management")
    layout.addWidget(label)

    paramButton = QPushButton("Paramètres")
    paramButton.clicked.connect(lambda :changeView(stackedWidget,paramView))
    layout.addWidget(paramButton)

    # Button
    button = QPushButton("Nouveau client")
    button.clicked.connect(clickedButtonDemo)
    layout.addWidget(button)

    mainWidget.setLayout(layout)
    return mainWidget

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout
from app.logic.changeView import changeView
from app.logic.readJSONfile import readJSONFile
from app.logic.sendButtonParametes import sendButtonParameters
from PySide6.QtCore import Qt


class ParameterWindow(QWidget) :
    def __init__(self,stackedWidget):
        super().__init__()
        self.setWindowTitle("Paramètres")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        header = QHBoxLayout()
        layout.addLayout(header)


        backButton = QPushButton("Retour")
        backButton.clicked.connect(lambda:changeView(stackedWidget,"main"))
        header.addWidget(backButton)

        header.addStretch(1)

        title = QLabel("Paramètres app")
        header.addWidget(title)

        formLayout = QVBoxLayout()
        formLayout.setAlignment(Qt.AlignHCenter)
        layout.addLayout(formLayout)

        formLayout.addWidget(QLabel("URL dossier clients"))


        filePathRef = [readJSONFile("app/logic/parameters","pathClientFile")]

        inputFilePath = QLineEdit()
        inputFilePath.setPlaceholderText("C:/Utilisateurs...")
        inputFilePath.setText(filePathRef[0])
        inputFilePath.textChanged.connect(lambda text: handleInputChange(text))
        formLayout.addWidget(inputFilePath)

        sendButton = QPushButton("Envoyer")
        sendButton.clicked.connect(lambda: sendButtonParameters(filePathRef[0],stackedWidget))
        formLayout.addWidget(sendButton)

        def handleInputChange(text):
            filePathRef[0]=text

        
        self.setLayout(layout)
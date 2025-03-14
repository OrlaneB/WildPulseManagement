from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from app.logic.changeView import changeView
from app.logic.readJSONfile import readJSONFile
from app.logic.sendButtonParametes import sendButtonParameters


class ParameterWindow(QWidget) :
    def __init__(self,stackedWidget):
        super().__init__()
        self.setWindowTitle("Paramètres")

        layout = QVBoxLayout()

        backButton = QPushButton("Retour")
        backButton.clicked.connect(lambda:changeView(stackedWidget,"main"))
        layout.addWidget(backButton)

        title = QLabel("Paramètres app")
        layout.addWidget(title)

        layout.addWidget(QLabel("URL dossier clients"))


        filePathRef = [readJSONFile("app/logic/parameters","pathClientFile")]

        inputFilePath = QLineEdit()
        inputFilePath.setPlaceholderText("C:/Utilisateurs...")
        inputFilePath.setText(filePathRef[0])
        inputFilePath.textChanged.connect(lambda text: handleInputChange(text))
        layout.addWidget(inputFilePath)

        sendButton = QPushButton("Envoyer")
        sendButton.clicked.connect(lambda: sendButtonParameters(filePathRef[0],stackedWidget))
        layout.addWidget(sendButton)

        def handleInputChange(text):
            filePathRef[0]=text

        
        self.setLayout(layout)
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon Application PySide")  # Titre de la fenêtre
        self.setGeometry(100, 100, 800, 600)  # Position et taille

        # Contenu de la fenêtre
        layout = QVBoxLayout()
        label = QLabel("Bienvenue dans mon application !")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
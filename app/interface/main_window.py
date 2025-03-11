from PySide6.QtWidgets import QMainWindow, QStackedWidget
from app.interface.parameter_window import ParameterWindow
from app.interface.createMainView import createMainView


#Main Window contains 3 parts : header, right and left

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wild Pulse Management")
        #self.setGeometry(100, 100, 800, 600)  # Position et taille

        self.stackedWidget = QStackedWidget()

        self.paramView = ParameterWindow(self.stackedWidget)
        self.mainView = createMainView(self.stackedWidget,self.paramView)

        self.stackedWidget.addWidget(self.mainView)
        self.stackedWidget.addWidget(self.paramView)

        self.setCentralWidget(self.stackedWidget)



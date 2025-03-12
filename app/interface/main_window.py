from PySide6.QtWidgets import QMainWindow, QStackedWidget
from app.interface.parameter_window import ParameterWindow
from app.interface.createMainView import createMainView
from app.interface.new_client_window import NewClientWindow
from app.interface.contract_window import ContractWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wild Pulse Management")
        #self.setGeometry(100, 100, 800, 600)  # Position et taille

        self.stackedWidget = QStackedWidget()

        self.paramView = ParameterWindow(self.stackedWidget)
        self.newClientView = NewClientWindow(self.stackedWidget)
        self.contractView = ContractWindow(self.stackedWidget)

        views = {
            "paramView":self.paramView,
            "newClientView":self.newClientView,
            "contractView":self.contractView
        }

        self.mainView = createMainView(self.stackedWidget,views)

        self.stackedWidget.addWidget(self.mainView)
        self.stackedWidget.addWidget(self.paramView)
        self.stackedWidget.addWidget(self.newClientView)
        self.stackedWidget.addWidget(self.contractView)

        self.setCentralWidget(self.stackedWidget)



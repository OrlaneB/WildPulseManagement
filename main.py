import sys
from PySide6.QtWidgets import QApplication
from app.interface.main_window import MainWindow

def main() :
    app= QApplication(sys.argv)

    with open("app/style/test.qss","r") as file:
        _style = file.read()
        app.setStyleSheet(_style)
        app.setStyle("Fusion")

    window= MainWindow()
    window.show()
    sys.exit(app.exec())

   


if __name__ == "__main__":
    main()
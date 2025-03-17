from PySide6.QtWidgets import QApplication

def getSizeWindow(self):
    screenSize = QApplication.primaryScreen().size()

    windowWidth = int(screenSize.width() * 0.8)
    windowHeight = int(screenSize.height() * 0.8)

    x = (screenSize.width() - windowWidth) /2
    y = (screenSize.height() - windowHeight) /2

    self.setGeometry(x,y,windowWidth,windowHeight)
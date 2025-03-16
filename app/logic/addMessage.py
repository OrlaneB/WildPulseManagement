from PySide6.QtWidgets import QLabel

def addMessage(layout,message):
    layout.addWidget(QLabel(message))
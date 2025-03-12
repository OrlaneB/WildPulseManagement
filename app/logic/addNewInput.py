from PySide6.QtWidgets import QLineEdit
from app.logic.handleChangeMembersName import handleChangeMembersName

def addNewInput(layout, variable,inputFields):
    newInput = QLineEdit()
    newInput.textChanged.connect(lambda text:handleChangeMembersName(inputFields,variable))
    inputFields.append(newInput)

    layout.addWidget(newInput)
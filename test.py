import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

from components.interface.cards import BicuStatementCard, BicuSvodCard


class BicuStatementBox(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        title = QLabel("Сводная ведомость", self)
        
        layout = QVBoxLayout(self)
        
        layout.addWidget(title)
        layout.addWidget(BicuStatementCard())
        
        self.setLayout(layout)



if __name__ == "__main__": 
    app = QApplication(sys.argv)
    mainWindow = BicuStatementBox()
    mainWindow.show() 
    sys.exit(app.exec_())
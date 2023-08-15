import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

from components.interface.cards import BicuLogCard


class BicuLogBox(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BicuLogCard(self))
        
        self.setLayout(layout)


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    mainWindow = BicuLogBox()
    mainWindow.show() 
    sys.exit(app.exec_())
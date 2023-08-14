from typing import Optional

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from components.interface.cards import ConsemersTotalSvodCard


class Content(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setStyleSheet("QWidget { background-color: #FFFFFF; }")
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        button_1 = ConsemersTotalSvodCard()
        layout.addWidget(button_1)
        layout.addStretch(1)
    
    
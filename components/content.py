from typing import Optional

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from components.interface import ConsumersContent


class Content(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setStyleSheet("QWidget { background-color: #FFFFFF; }")
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        button = QPushButton("Click me")
        button_1 = ConsumersContent()
        layout.addWidget(button)
        layout.addWidget(button_1)
        layout.addStretch(1)
    
    
app = QApplication([])

content = Content()
content.show()

app.exec_()
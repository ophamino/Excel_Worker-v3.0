from typing import Optional
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from components.interface.cards import ConsemersTotalSvodCard, ConsemersCommerceStatementCard, ConsemersCommerceSvodCard, ConsemersIndividualStatementCard, ConsemersIndividualSvodCard, ConsumersLogCard
from components.interface.boxes import ConsemersSvodBox
from components.interface import ConsumersContent, BicuContent

class Content(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setStyleSheet("QWidget { background-color: #FFFFFF; }")
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.content = ConsumersContent()
        self.layout.addWidget(self.content)
        self.layout.addStretch(1)
        

    def change_on_bicu(self):
        content = BicuContent(self)
        layout = QVBoxLayout(self)
        layout.addWidget(content)
        self.setLayout(layout)
        
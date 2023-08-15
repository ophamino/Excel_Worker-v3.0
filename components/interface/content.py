from typing import Optional
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt5.QtGui import QFont
from components.interface.cards import ConsemersTotalSvodCard, ConsemersCommerceStatementCard, ConsemersCommerceSvodCard, ConsemersIndividualStatementCard, ConsemersIndividualSvodCard, ConsumersLogCard


class Content(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.title: str
        self.initUI()
        
    def initUI(self):
        self.setStyleSheet("QWidget { background-color: #FFFFFF; }")
        title = QLabel(self.title)
        title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addStretch(1)
        self.setLayout(layout)


class ConsumersContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        self.title = "Потребители"
        super().__init__(parent)


class BicuContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        self.title = "Бику"
        super().__init__(parent)


class BalanceContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        self.title = "Сводный баланс"
        super().__init__(parent)
        
class ReportsContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        self.title = "Отчеты"
        super().__init__(parent)
        
class HistoryContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        self.title = "История операций"
        super().__init__(parent)


class SettingsContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        self.title = "Настройки"
        super().__init__(parent)


class HelpContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        self.title = "Справка"
        super().__init__(parent)
from typing import Optional

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt5.QtGui import QFont
from components.interface.boxes import ConsumersLogBox, ConsumersStatementBox


class Content(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(Content, self).__init__(parent)
        self.setStyleSheet("QWidget { background-color: #FFFFFF; } QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000 }")

class ContentTitle(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super(ContentTitle, self).__init__(text, parent)


class ConsumersContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsumersContent, self).__init__(parent)
        self.title = "Потребители"
        self.title = QLabel(self.title)
        self.title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        self.title.setFixedHeight(100)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addStretch(1)
        self.setLayout(self.layout)


class BicuContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuContent, self).__init__(parent)
        self.title = "БИКУ"
        self.title = QLabel(self.title)
        self.title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        self.title.setFixedHeight(100)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)


class BalanceContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BalanceContent, self).__init__(parent)
        self.title = "Сводный баланс"
        self.title = QLabel(self.title)
        self.title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        self.title.setFixedHeight(100)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)
        
class ReportsContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ReportsContent, self).__init__(parent)
        self.title = "Отчеты"
        self.title = QLabel(self.title)
        self.title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        self.title.setFixedHeight(100)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)
        
class HistoryContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(HistoryContent, self).__init__(parent)
        self.title = "История операций"
        self.title = QLabel(self.title)
        self.title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        self.title.setFixedHeight(100)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)


class SettingsContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(SettingsContent, self).__init__(parent)
        self.title = "Настройки"
        self.title = QLabel(self.title)
        self.title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        self.title.setFixedHeight(100)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)


class HelpContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(HelpContent, self).__init__(parent)
        self.title = "Справка"
        self.title = QLabel(self.title)
        self.title.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")
        self.title.setFixedHeight(100)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)

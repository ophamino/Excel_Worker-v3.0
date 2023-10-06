from typing import Optional

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from src.components.boxes import (
    ConsumersLogBox,
    ConsumersStatementBox,
    ComsumersSvodBox,
    BicuSvodBox,
    BicuStatementBox,
    BicuLogBox,
    BalanceBox,
    AccrualsBox,
    BypassBox,
    ASCUEBox
    )



class Content(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(Content, self).__init__(parent)
        self.setStyleSheet("QWidget { background-color: #FFFFFF; }")

class ContentTitle(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super(ContentTitle, self).__init__(text, parent)
        self.setFixedHeight(100)
        self.setStyleSheet("QLabel {font-size: 50px; padding: 20px 30px; border-bottom: 3px solid #000; font-family: 'Montserrat';}")


class ConsumersContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsumersContent, self).__init__(parent)
        
        title = ContentTitle("Потребители", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(ComsumersSvodBox(self))
        layout.addWidget(ConsumersStatementBox(self))
        layout.addWidget(ConsumersLogBox(self))
        layout.addWidget(AccrualsBox(self))
        layout.addWidget(BypassBox(self))
        layout.addWidget(ASCUEBox(self))
        layout.addStretch(1)
        
        self.setLayout(layout)


class BicuContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuContent, self).__init__(parent)
        
        title = ContentTitle("БИКУ", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(BicuSvodBox(self))
        layout.addWidget(BicuStatementBox(self))
        layout.addWidget(BicuLogBox(self))
        layout.addStretch(1)
        
        self.setLayout(layout)


class BalanceContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BalanceContent, self).__init__(parent)
        
        title = ContentTitle("Сводный баланс", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(BalanceBox(self))
        layout.addStretch(1)

        self.setLayout(layout)
        
class ReportsContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ReportsContent, self).__init__(parent)
        
        title = ContentTitle("Отчеты", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)
        
        self.setLayout(layout)
        
class HistoryContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(HistoryContent, self).__init__(parent)
        
        title = ContentTitle("История операций", self)

        layout = QVBoxLayout(self)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)
        
        self.setLayout(layout)


class SettingsContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(SettingsContent, self).__init__(parent)
        
        title = ContentTitle("Настройки", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)
        
        self.setLayout(layout)


class HelpContent(Content):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(HelpContent, self).__init__(parent)
        title = ContentTitle("Справка", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)
        
        self.setLayout(layout)

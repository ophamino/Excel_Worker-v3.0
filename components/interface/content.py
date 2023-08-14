from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .boxes import (
    BalanceBox,
    BicuLogBox,
    BicuStatementBox,
    BicuSvodBox,
    ConsumersLogBox,
    ConsemersSvodBox,
    ConsumersStatementBox
    )

class Content(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout()
        self.initUI()
        self.setFixedSize(850, 1200)
        
    def initUI(self) -> None:
        pass


class ConsumersContent(Content):
    def initUI(self):
        self.layout.addWidget(ConsemersSvodBox())
        self.layout.addWidget(ConsumersStatementBox())
        self.layout.addWidget(ConsumersLogBox())


class BicuContent(Content):
    def initUI(self) -> None:
        self.layout.addWidget(BicuSvodBox())
        self.layout.addWidget(BicuStatementBox())
        self.layout.addWidget(BicuLogBox())


class BalanceContent(Content):
    def initUI(self) -> None:
        self.layout.addWidget(BalanceBox())


class HistoryContent(Content):
    pass


class SettingsContent(Content):
    pass


class HelpContent(Content):
    pass

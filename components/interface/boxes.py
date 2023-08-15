from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from .cards import (
    ConsemersCommerceStatementCard,
    ConsemersCommerceSvodCard,
    ConsemersIndividualStatementCard,
    ConsemersIndividualSvodCard,
    ConsemersTotalSvodCard,
    ConsumersLogCard,
    BicuLogCard, 
    BicuStatementCard,
    BicuSvodCard,
    BalanceCard,
    BalanceAnalyticsCard,
    )


class Box(QWidget):
    def __init__(self, title: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.title = title
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.setLayout(self.layout)

    
class ConsemersSvodBox(Box):
    def __init__(self, parent: QWidget | None = None) -> None:
        self.setFixedSize(1200, 100 * 3)
        super().__init__(title="Сводная ведомость", parent=parent)
        
        


class ConsumersStatementBox(Box):
    def initUI(self):
        layoyt = QVBoxLayout()
        layoyt.addWidget(ConsemersIndividualStatementCard(self))
        layoyt.addWidget(ConsemersCommerceStatementCard(self))


class ConsumersLogBox(Box):
    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(ConsumersLogCard())


class BicuSvodBox(Box):
    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(BicuSvodCard())


class BicuStatementBox(Box):
    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(BicuStatementCard())


class BicuLogBox(Box):
    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(BicuLogCard)


class BalanceBox(Box):
    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(BalanceCard())
        layout.addWidget(BalanceAnalyticsCard())

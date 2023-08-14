from PyQt5.QtWidgets import QWidget, QVBoxLayout
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
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.initUI()
        self.setFixedSize(1000, 1000)
    def initUI(self):
        pass
    
class ConsemersSvodBox(Box):
    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(ConsemersIndividualSvodCard())
        layout.addWidget(ConsemersCommerceSvodCard())
        layout.addWidget(ConsemersTotalSvodCard())
        


class ConsumersStatementBox(Box):
    def initUI(self):
        layoyt = QVBoxLayout()
        layoyt.addWidget(ConsemersIndividualStatementCard())
        layoyt.addWidget(ConsemersCommerceStatementCard())


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
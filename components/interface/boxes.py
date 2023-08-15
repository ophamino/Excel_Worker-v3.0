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
        self.title = QLabel(title)
        self.title.setStyleSheet("QLabel {font-size: 20px; border-bottom: 2px solid #000; padding-bottom: 5px;}")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.setLayout(self.layout)

    
class ComsumersSvodBox(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        title = QLabel("Сводная ведомость", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(ConsemersIndividualSvodCard(self))
        layout.addWidget(ConsemersCommerceSvodCard(self))
        layout.addWidget(ConsemersTotalSvodCard(self))
        
        self.setLayout(layout)


class ConsumersStatementBox(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        title = QLabel("Расчетные ведомости", self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(ConsemersIndividualStatementCard(self))
        layout.addWidget(ConsemersCommerceStatementCard(self))
        
        self.setLayout(layout)


class ConsumersLogBox(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(ConsumersLogCard(self))
        
        self.setLayout(layout)


class BicuSvodBox(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BicuSvodCard())
        
        self.setLayout(layout)


class BicuStatementBox(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BicuStatementCard())
        
        self.setLayout(layout)


class BicuLogBox(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BicuLogCard(self))
        
        self.setLayout(layout)


class BalanceBox(Box):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BalanceCard(self))
        layout.addWidget(BalanceAnalyticsCard(self))
        
        self.setLayout(layout)

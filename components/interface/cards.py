from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from .buttons import (
    ConsumersCommerceStatementButton,
    ConsumersCommerceSvodButton,
    ConsumersIndividualStatementButton,
    ConsumersIndividualSvodButton,
    ConsumersTotalSvodButton,
    ConsumersLogButton,
    BalanceAnalyticsButton,
    BalanceButton,
    BicuStatementButton,
    BicuSvodButton,
    BicuLogButton
    )


class CardTitle(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)


class ConsemersIndividualSvodCard(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersIndividualSvodCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        
class ConsemersCommerceSvodCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersCommerceSvodCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class ConsemersTotalSvodCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersTotalSvodCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class ConsemersIndividualStatementCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersIndividualStatementCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class ConsemersCommerceStatementCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersCommerceStatementCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class ConsumersLogCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsumersLogCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class BicuSvodCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BicuSvodCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class BicuStatementCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BicuStatementCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class BicuLogCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BicuLogCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class BalanceCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BalanceCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


class BalanceAnalyticsCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BalanceAnalyticsCard, self).__init__(parent)
        self.button = ConsumersIndividualSvodButton(self)
        self.label = CardTitle("Сводная ведомость бытовых потребитилей",self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from .buttons import (
    ConsumersIndividualSvodButton,
    ConsumersCommerceSvodButton,
    ConsumersTotalSvodButton,
    ConsumersIndividualStatementButton,
    ConsumersCommerceStatementButton,
    ConsumersLogButton,
    BicuSvodButton,
    BicuStatementButton,
    BicuLogButton,
    BalanceButton,
    BalanceAnalyticsButton,
    )


class CardTitle(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)


class ConsemersIndividualSvodCard(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersIndividualSvodCard, self).__init__(parent)
        
        label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        button = ConsumersIndividualSvodButton(self)
        
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
class ConsemersCommerceSvodCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersCommerceSvodCard, self).__init__(parent)
        
        label = CardTitle("Сводная ведомость коммерческих потребитилей", self)
        button = ConsumersCommerceSvodButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsemersTotalSvodCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersTotalSvodCard, self).__init__(parent)
        
        label = CardTitle("Сводная ведомость потребитилей", self)
        button = ConsumersTotalSvodButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsemersIndividualStatementCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersIndividualStatementCard, self).__init__(parent)
        
        label = CardTitle("Расчетная ведомость бытовых потребитилей", self)
        button = ConsumersIndividualStatementButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsemersCommerceStatementCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsemersCommerceStatementCard, self).__init__(parent)
        
        label = CardTitle("Расчетная ведомость коммерческих потребитилей", self)
        button = ConsumersCommerceStatementButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsumersLogCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(ConsumersLogCard, self).__init__(parent)
        
        label = CardTitle("Журнал изменений", self)
        button = ConsumersLogButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BicuSvodCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BicuSvodCard, self).__init__(parent)
        
        label = CardTitle("Сводная ведомость БИКУ", self)
        button = BicuSvodButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BicuStatementCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BicuStatementCard, self).__init__(parent)
        
        label = CardTitle("Расчетная ведомость БИКУ", self)
        button = BicuStatementButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BicuLogCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BicuLogCard, self).__init__(parent)
        
        label = CardTitle("Журнал изменений", self)
        button = BicuLogButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BalanceCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BalanceCard, self).__init__(parent)
        
        label = CardTitle("Сводный баланс", self)
        button = BalanceButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BalanceAnalyticsCard(QWidget):
     def __init__(self, parent: QWidget | None = None) -> None:
        super(BalanceAnalyticsCard, self).__init__(parent)
        
        label = CardTitle("Аналитика сводного баланса",self)
        button = BalanceAnalyticsButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)

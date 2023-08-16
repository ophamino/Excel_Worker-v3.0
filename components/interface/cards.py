from typing import Optional

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
    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        super().__init__(text, parent)
        self.setStyleSheet("QLabel {font-size: 20px; padding: 10px 30px; border-bottom: 1px solid #000; font-family: 'Montserrat';}")


class ContentCard(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ContentCard, self).__init__(parent)
        self.setStyleSheet("QWidget { }")
        self.setFixedHeight(100)


class ConsemersIndividualSvodCard(ContentCard):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsemersIndividualSvodCard, self).__init__(parent)
        
        
        label = CardTitle("Сводная ведомость бытовых потребитилей", self)
        button = ConsumersIndividualSvodButton(self)
        
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
class ConsemersCommerceSvodCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsemersCommerceSvodCard, self).__init__(parent)
        
        label = CardTitle("Сводная ведомость коммерческих потребитилей", self)
        button = ConsumersCommerceSvodButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsemersTotalSvodCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsemersTotalSvodCard, self).__init__(parent)
        
        label = CardTitle("Сводная ведомость потребитилей", self)
        button = ConsumersTotalSvodButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsemersIndividualStatementCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsemersIndividualStatementCard, self).__init__(parent)
        
        label = CardTitle("Расчетная ведомость бытовых потребитилей", self)
        button = ConsumersIndividualStatementButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsemersCommerceStatementCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsemersCommerceStatementCard, self).__init__(parent)
        
        label = CardTitle("Расчетная ведомость коммерческих потребитилей", self)
        button = ConsumersCommerceStatementButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsumersLogCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsumersLogCard, self).__init__(parent)
        
        label = CardTitle("Журнал изменений", self)
        button = ConsumersLogButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BicuSvodCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuSvodCard, self).__init__(parent)
        
        label = CardTitle("Сводная ведомость БИКУ", self)
        button = BicuSvodButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BicuStatementCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuStatementCard, self).__init__(parent)
        
        label = CardTitle("Расчетная ведомость БИКУ", self)
        button = BicuStatementButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BicuLogCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuLogCard, self).__init__(parent)
        
        label = CardTitle("Журнал изменений", self)
        button = BicuLogButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BalanceCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BalanceCard, self).__init__(parent)
        
        label = CardTitle("Сводный баланс", self)
        button = BalanceButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class BalanceAnalyticsCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BalanceAnalyticsCard, self).__init__(parent)
        
        label = CardTitle("Аналитика сводного баланса",self)
        button = BalanceAnalyticsButton(self)
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)

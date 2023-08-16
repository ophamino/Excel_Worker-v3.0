from typing import Optional

from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

from src.components.buttons import (
    ConsumersStatementButton,
    ConsumersSvodButton,
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


class ConsemerslSvodCard(ContentCard):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsemerslSvodCard, self).__init__(parent)
        
        
        label = CardTitle("Сводная ведомость потребитилей", self)
        button = ConsumersSvodButton(self)
        
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)


class ConsemersStatementCard(ContentCard):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsemersStatementCard, self).__init__(parent)
        
        label = CardTitle("Расчетная ведомость потребитилей", self)
        button = ConsumersStatementButton(self)
        
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

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

class Card(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.title: str = None
        self.button: QWidget = None
        self.initUI()
        self.setFixedSize(1400, 150)
    
    def initUI(self):
        title = QLabel(self.title)
        layot = QHBoxLayout()
        layot.addWidget(title)
        layot.addWidget(self.button)
        self.setLayout(layot)

class ConsemersIndividualSvodCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    
    def initUI(self):
        self.button = ConsumersIndividualSvodButton()
        self.title = "Сводная ведомость бытовых потребителей"


class ConsemersCommerceSvodCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
    def initUI(self):
        self.button = ConsumersCommerceSvodButton()
        self.title = "Сводна ведомсть коммерческих потребителеей"


class ConsemersTotalSvodCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def initUI(self):
        self.button = ConsumersTotalSvodButton()
        self.title = "Сводная ведомость потребителей"
        return super().initUI()


class ConsemersIndividualStatementCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
    def initUI(self):
        self.button = ConsumersIndividualStatementButton()
        self.title = "Расчетная ведомость бытовых потребителей"


class ConsemersCommerceStatementCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    
    def initUI(self):
        self.button = ConsumersCommerceStatementButton()
        self.title = "Расчетная ведомость коммерческих потребителей"


class ConsumersLogCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    def initUI(self):
        self.button = ConsumersLogButton()
        self.title = "Журнал изменений"


class BicuSvodCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.button = BicuSvodButton()
        self.title = "Сводная ведомость БИКУ"


class BicuStatementCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.button = BicuStatementButton()
        self.title = "Расчетная ведомость БИКУ"


class BicuLogCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.button = BicuLogButton()
        self.title = "Журнал изменений"


class BalanceCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.button = BalanceButton()
        self.title = "Сводный баланс"


class BalanceAnalyticsCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.button = BalanceAnalyticsButton()
        self.title = "Аналитика сводного баланса"


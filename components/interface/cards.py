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
        # self.setStyleSheet("QWidget {border: 2px solid #000; border-radius: 10px;}")
        self.initUI()
        self.setFixedSize(1400, 120)
    
    def initUI(self):
        title = QLabel(self.title)
        title.setStyleSheet("QLabel {font-size: 20px; padding: 0 30px;}")
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
        return super().initUI()


class ConsemersCommerceSvodCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
    def initUI(self):
        self.button = ConsumersCommerceSvodButton()
        self.title = "Сводна ведомсть коммерческих потребителеей"
        return super().initUI()


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
        return super().initUI()


class ConsemersCommerceStatementCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    
    def initUI(self):
        self.button = ConsumersCommerceStatementButton()
        self.title = "Расчетная ведомость коммерческих потребителей"
        return super().initUI()


class ConsumersLogCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
    def initUI(self):
        self.button = ConsumersLogButton()
        self.title = "Журнал изменений"
        return super().initUI()


class BicuSvodCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.button = BicuSvodButton()
        self.title = "Сводная ведомость БИКУ"
        return super().initUI()


class BicuStatementCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
            
    def initUI(self):
        self.button = BicuStatementButton()
        self.title = "Расчетная ведомость БИКУ"
        return super().initUI()


class BicuLogCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
            
    def initUI(self):
        self.button = BicuLogButton()
        self.title = "Журнал изменений"
        return super().initUI()


class BalanceCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
            
    def initUI(self):
        self.button = BalanceButton()
        self.title = "Сводный баланс"
        return super().initUI()


class BalanceAnalyticsCard(Card):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
            
    def initUI(self):
        self.button = BalanceAnalyticsButton()
        self.title = "Аналитика сводного баланса"
        return super().initUI()


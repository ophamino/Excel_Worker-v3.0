from typing import Optional

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from src.components.cards import (
    ConsemerslSvodCard,
    ConsemersStatementCard,
    ConsumersLogCard,
    BicuSvodCard,
    BicuStatementCard,
    BicuLogCard, 
    BalanceCard,
    BalanceAnalyticsCard,
    AccrualsCard,
    BypassCard,
    ASCUECard
    )


class ContentBox(QWidget):
    
    def __init__(self,parent: Optional[QWidget] = None) -> None:
        super(ContentBox, self).__init__(parent)
      
 
class BoxTitle(QLabel):
    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        super().__init__(text, parent)
        self.setStyleSheet("QLabel {font-size: 25px; padding: 10px 30px; border-bottom: 1px solid #000; font-family: 'Montserrat';}")


class ComsumersSvodBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ComsumersSvodBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(ConsemerslSvodCard(self))
        self.setLayout(layout)


class ConsumersStatementBox(ContentBox):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsumersStatementBox, self).__init__(parent)
    
        
        layout = QVBoxLayout(self)
        layout.addWidget(ConsemersStatementCard(self))
        
        self.setLayout(layout)


class AccrualsBox(ContentBox):
     def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(AccrualsBox, self).__init__(parent)
    
        
        layout = QVBoxLayout(self)
        layout.addWidget(AccrualsCard(self))
        
        self.setLayout(layout)


class ConsumersLogBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ConsumersLogBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(ConsumersLogCard(self))
        
        self.setLayout(layout)


class BicuSvodBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuSvodBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BicuSvodCard())
        
        self.setLayout(layout)


class BicuStatementBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuStatementBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BicuStatementCard())
        
        self.setLayout(layout)


class BicuLogBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BicuLogBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BicuLogCard(self))
        
        self.setLayout(layout)


class BalanceBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BalanceBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BalanceCard(self))
        layout.addWidget(BalanceAnalyticsCard(self))
        
        self.setLayout(layout)


class BypassBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(BypassBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(BypassCard(self))
        
        self.setLayout(layout)
        
        
class ASCUEBox(ContentBox):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(ASCUEBox, self).__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.addWidget(ASCUECard(self))
        
        self.setLayout(layout)
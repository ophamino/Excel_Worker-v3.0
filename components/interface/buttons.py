from typing import Optional

from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class SideaBarButton(QPushButton):
    def __init__(self, name: str, icon: str, parent: Optional[QWidget] = None) -> None:
        super(SideaBarButton, self).__init__(name, parent)
        self.setIcon(QIcon(icon))
        self.setFixedHeight(70)
        self.setFixedWidth(340)
        self.setIconSize(QSize(32, 32))


class MonthButton(QPushButton):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(MonthButton, self).__init__("Сформировать", parent)
        self.setFixedSize(100, 50)
        self.clicked.connect(self.on_button_clicked)
        
    def on_button_clicked(self) -> None:
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        month, ok = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", months)
        
        if ok:
            self.do_something_with_month(month)
    
    def do_something_with_month(self, month) -> None:
        pass


class ConsumersIndividualSvodButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        pass


class ConsumersCommerceSvodButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        pass

class ConsumersTotalSvodButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        pass


class ConsumersCommerceStatementButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        pass

class ConsumersIndividualStatementButton(MonthButton):

    def do_something_with_month(self, month) -> None:
        pass
    

class ConsumersLogButton(MonthButton):
    def do_something_with_month(self, month) -> None:
        pass


class BicuStatementButton(MonthButton):

    def do_something_with_month(self, month) -> None:
        pass


class BicuSvodButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        pass


class BicuLogButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        pass


class BalanceButton(MonthButton):

    def do_something_with_month(self, month) -> None:
        pass

class BalanceAnalyticsButton(MonthButton):

    def do_something_with_month(self, month: str) -> None:
        pass

from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog


class MonthButton(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.initUI()
    
    def initUI(self) -> None:
        self.button = QPushButton("Сформировать", self)
        self.setGeometry(100, 100, 200, 50)
        self.button.clicked.connect(self.on_button_clicked)
        
    def on_button_clicked(self) -> None:
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        month, ok = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", months)
        
        if ok:
            self.do_something_with_month(self, month)
    
    def do_something_with_month(self, month: str) -> None:
        pass


class ConsumersIndividualSvodButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    
    def do_something_with_month(self, month: str) -> None:
        pass


class ConsumersCommerceSvodButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def do_something_with_month(self, month: str) -> None:
        pass

class ConsumersTotalSvodButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    
    def do_something_with_month(self, month: str) -> None:
        pass


class ConsumersCommerceStatementButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    
    def do_something_with_month(self, month: str) -> None:
        pass

class ConsumersIndividualStatementButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def do_something_with_month(self, month: str) -> None:
        pass
    

class ConsumersLogButton(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)


class BicuStatementButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def do_something_with_month(self, month: str) -> None:
        pass


class BicuSvodButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
    
    def do_something_with_month(self, month: str) -> None:
        pass


class BicuLogButton(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)


class BalanceButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def do_something_with_month(self, month: str) -> None:
        pass

class BalanceAnalyticsButton(MonthButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def do_something_with_month(self, month: str) -> None:
        pass

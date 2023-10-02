from enum import Enum
from typing import Optional, Callable

from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QThread, pyqtSignal

from src.service import Balance, BalanceAnalitic, BicuLog, BicuService, ConsumersService, Log, AccrualsCommerceService, AccrualsIndividualService, BypassService
from src.utils.const import MONTH_LIST


class WorkerThread(QThread):
    finished_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self, func: Callable[[], int]):
        func()
        self.finished_signal.emit()


class SideaBarButton(QPushButton):
    def __init__(self, name: str, icon: str, parent: Optional[QWidget] = None) -> None:
        super(SideaBarButton, self).__init__(name, parent)
        self.setIcon(QIcon(icon))
        self.setFixedHeight(70)
        self.setFixedWidth(340)
        self.setIconSize(QSize(32, 32))


class SimpleContentButton(QPushButton):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(SimpleContentButton, self).__init__("Сформировать", parent)
        self.setFixedSize(100, 50)
        self.clicked.connect(self.on_button_clicked)
    
    def on_button_clicked(self) -> None:
         pass


class MonthButton(QPushButton):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(MonthButton, self).__init__("Сформировать", parent)
        self.setFixedSize(100, 50)
        self.clicked.connect(self.on_button_clicked)
        self.myThread = WorkerThread()
        
    def on_button_clicked(self) -> None:
        month, ok = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", MONTH_LIST)
        
        if ok:
            self.do_something_with_month(month)
    
    def do_something_with_month(self, month) -> None:
        pass

class AccrualsButton(MonthButton):
    
    def on_button_clicked(self) -> None:
        category, category_status = QInputDialog.getItem(self, "Выбор ведомости", "Выберите тип ведомости", [
            "Бытовые потребители",
            "Коммерческие потребители",
            ]
        )
        if category_status:
            month, month_status = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", MONTH_LIST)

            if month_status:
                self.do_something_with_month(category, month)
    
    def do_something_with_month(self, category, month) -> None:
        if category == "Бытовые потребители":
            AccrualsIndividualService().insert_values(month)
        if category == "Коммерческие потребители":
            AccrualsCommerceService(month).insertAccruals()


class ConsumersSvodButton(MonthButton):
    
    def on_button_clicked(self) -> None:
        category, category_status = QInputDialog.getItem(self, "Выбор ведомости", "Выберите тип ведомости", [
            "Сводная ведомость бытовых потребителей",
            "Сводная ведомость коммерческих потребителей",
            "Сводная ведомость"
            ]
        )
        if category_status:
            month, month_status = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", MONTH_LIST)

            if month_status:
                self.do_something_with_month(category, month)
    
    def do_something_with_month(self, category, month) -> None:
        if category == "Сводная ведомость бытовых потребителей":
            ConsumersService().collect_individual_svod(month)
        if category == "Сводная ведомость коммерческих потребителей":
            ConsumersService().collect_commerce_svod(month)
        if category == "Сводная ведомость":
            ConsumersService().collect_total_svod(month)


class ConsumersStatementButton(MonthButton):
    
    def on_button_clicked(self) -> None:
        category, category_status = QInputDialog.getItem(self, "Выбор ведомости", "Выберите тип ведомости", [
            "Расчетная ведомость бытовых потребителей",
            "Расчетная ведомость коммерческих потребителей",
            ]
        )
        month, month_status = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", MONTH_LIST)
        
        if category_status and month_status:
            self.do_something_with_month(category, month)
    
    def do_something_with_month(self, category, month) -> None:
        if category == "Расчетная ведомость бытовых потребителей":
            ConsumersService().create_individual_statement(month)

        if category == "Расчетная ведомость бытовых потребителей":
            ConsumersService().create_commerce_statement(month)
                

class ConsumersLogButton(SimpleContentButton):
    def on_button_clicked(self) -> None:
        Log().search_changes()


class BicuStatementButton(MonthButton):

    def do_something_with_month(self, month) -> None:
        BicuService().create_new_statement(month)


class BicuSvodButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        BicuService().collect_data_in_svod(month)


class BicuLogButton(SimpleContentButton):
    def on_button_clicked(self) -> None:
        BicuLog().search_changes()


class BalanceButton(MonthButton):

    def do_something_with_month(self, month) -> None:
        Balance().create_balance(month)

class BalanceAnalyticsButton(MonthButton):

    def do_something_with_month(self, month: str) -> None:
        BalanceAnalitic().create_analytics(month)


class BypassButton(MonthButton):
    
    def on_button_clicked(self) -> None:
        category, category_status = QInputDialog.getItem(self, "Выбор ведомости", "Выберите тип ведомости", [
            "Загрузить",
            "Выгрузить"
            ]
        )
        month, month_status = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", MONTH_LIST)
        
        if category_status and month_status:
            self.do_something_with_month(category, month)
    
    def do_something_with_month(self, category, month) -> None:
        if category == "Загрузить":
            pass

        if category == "Выгрузить":
            BypassService().create_clear_bypass(month)
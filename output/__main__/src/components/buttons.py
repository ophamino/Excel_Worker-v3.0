from enum import Enum
from typing import Optional, Callable

from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, QSize, QThread, pyqtSignal

from src.service import Balance, BalanceAnalitic, BicuLog, BicuService, ConsumersService, Log, AccrualsCommerceService, AccrualsIndividualService, BypassService
from src.service.ascue import insert_values
from src.utils.const import MONTH_LIST




def show_notification(text: str) -> None:
    msgBox = QMessageBox()
    msgBox.setText(text)
    msgBox.setStyleSheet("QMessageBox: { background-color: #fff; font-size: 25px;}")
    msgBox.exec_()


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
            show_notification("Начисления для бытовых потребителей произведены")
        if category == "Коммерческие потребители":
            AccrualsCommerceService(month).insertAccruals()
            show_notification("Начисления для коммерческих потребителей произведены")


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
            show_notification("Сводная ведомость бытовых потребителей сформирована")
            
        if category == "Сводная ведомость коммерческих потребителей":
            ConsumersService().collect_commerce_svod(month)
            show_notification("Сводная ведомость коммерческих потребителей сформирована")
            
        if category == "Сводная ведомость":
            ConsumersService().collect_total_svod(month)
            show_notification("Сводная ведомость потребителей сформирована")


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
            show_notification("Расчетная ведомость бытовых потребителей сформирована")

        if category == "Расчетная ведомость коммерческих потребителей":
            ConsumersService().create_commerce_statement(month)
            show_notification("Расчетная ведомость коммерческих потребителей сформирована")
                

class ConsumersLogButton(SimpleContentButton):
    def on_button_clicked(self) -> None:
        Log().search_changes()
        show_notification("Поиск изменений в реестре потребителей окончен")


class BicuStatementButton(MonthButton):

    def do_something_with_month(self, month) -> None:
        BicuService().create_new_statement(month)
        show_notification("Расчетная ведомость БИКУ сформирована")


class BicuSvodButton(MonthButton):
    
    def do_something_with_month(self, month) -> None:
        BicuService().collect_data_in_svod(month)
        show_notification("Сводная ведомость БИКУ сформирована")


class BicuLogButton(SimpleContentButton):
    def on_button_clicked(self) -> None:
        BicuLog().search_changes()
        show_notification("Поиск изменений в реестре БИКУ окончен")


class BalanceButton(MonthButton):

    def do_something_with_month(self, month) -> None:
        Balance().create_balance(month)
        show_notification("Сводный баланс сформирован")

class BalanceAnalyticsButton(MonthButton):

    def do_something_with_month(self, month: str) -> None:
        BalanceAnalitic().create_analytics(month)
        show_notification("Аналитика сводного баланса сформирован")

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
            BypassService().download_bypass(month)
            show_notification("Обходной лист загружен")

        if category == "Выгрузить":
            BypassService().create_clear_bypass(month)
            show_notification("Обходной лист выгружен")



class ASCUEButton(MonthButton):
    
    def on_button_clicked(self) -> None:
        month, month_status = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", MONTH_LIST)
        
        if month_status:
            self.do_something_with_month(month)
    
    def do_something_with_month(self, month: str) -> None:
        insert_values(month)
        show_notification("Сведения АСКУЭ выгружены")
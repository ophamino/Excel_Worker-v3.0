import sys
import logging 
from typing import Optional
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QTabWidget
from PyQt5.QtGui import QPixmap, QIcon
 
from src.components.buttons import SideaBarButton
from src.components import ConsumersContent, BicuContent, BalanceContent, ReportsContent, HelpContent, HistoryContent, SettingsContent
from src.utils.base import resource_path
 
 
class Application(QMainWindow):
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setStyleSheet("QWidget { background-color: #fff; }")
        self.width = 1200
        self.height = int(0.618 * 1200)
        self.resize(self.width, self.height)
        self.initUI()
        self.setWindowTitle(" ")
        icon = QIcon(resource_path("src\\images\\interface\\qicon.png"))
        self.setWindowIcon(icon)
    
    def initUI(self):
        self.logo = QLabel()
        self.pixmap = QPixmap(resource_path("src/images/interface/logo.png"))
        self.logo.setFixedHeight(340)
        self.logo.setFixedWidth(340)
        self.logo.setScaledContents(True)
        self.logo.setPixmap(self.pixmap)
        
        self.consumers_btn = SideaBarButton(name="Потребители", icon=resource_path("src/images/interface/consumers.png"))
        self.bicu_btn = SideaBarButton(name="БИКУ", icon=resource_path("src/images/interface/bicu.png"))
        self.balance_btn = SideaBarButton(name="Сводный баланс", icon=resource_path("src/images/interface/balance.png"))
        self.reports_btn = SideaBarButton(name="Отчеты", icon=resource_path("src/images/interface/reports.png"))
        self.history_btn = SideaBarButton(name="История операций", icon=resource_path("src/images/interface/history.png"))
        self.config_btn = SideaBarButton(name="Настройки", icon=resource_path("src/images/interface/config.png"))
        self.help_btn = SideaBarButton(name="Справка", icon=resource_path("src/images/interface/help.png"))
        
        self.consumers_btn.clicked.connect(self.change_on_consumers)
        self.bicu_btn.clicked.connect(self.change_on_bicu)
        self.balance_btn.clicked.connect(self.change_on_balance)
        self.reports_btn.clicked.connect(self.change_on_reports)
        self.history_btn.clicked.connect(self.change_on_history)
        self.config_btn.clicked.connect(self.change_on_config)
        self.help_btn.clicked.connect(self.change_on_help)
        
        self.consumers = ConsumersContent(self)
        self.bicu = BicuContent(self)
        self.balance = BalanceContent(self)
        self.reports = ReportsContent(self)
        self.history = HistoryContent(self)
        self.settings = SettingsContent(self)
        self.help = HelpContent(self)
        
        left_layout = QVBoxLayout(self)
        left_layout.addWidget(self.logo)
        left_layout.addWidget(self.consumers_btn)
        left_layout.addWidget(self.bicu_btn)
        left_layout.addWidget(self.balance_btn)
        left_layout.addWidget(self.reports_btn)
        left_layout.addWidget(self.history_btn)
        left_layout.addWidget(self.config_btn)
        left_layout.addWidget(self.help_btn)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        
        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")
        self.right_widget.addTab(self.consumers, "")
        self.right_widget.addTab(self.bicu, "")
        self.right_widget.addTab(self.balance, "")
        self.right_widget.addTab(self.reports, "")
        self.right_widget.addTab(self.history, "")
        self.right_widget.addTab(self.settings, "")
        self.right_widget.addTab(self.help, "")
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('QTabBar::tab{ width: 0; height: 0; margin: 0; padding: 0; border: none; } QTabWidget { border: 10px solid #000000;}')
        
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
    def change_on_consumers(self):
        self.right_widget.setCurrentIndex(0)
        
    def change_on_bicu(self):
        self.right_widget.setCurrentIndex(1)
        
    def change_on_balance(self):
        self.right_widget.setCurrentIndex(2)
        
    def change_on_reports(self):
        self.right_widget.setCurrentIndex(3)
        
    def change_on_history(self):
        self.right_widget.setCurrentIndex(4)
        
    def change_on_config(self):
        self.right_widget.setCurrentIndex(5)
        
    def change_on_help(self):
        self.right_widget.setCurrentIndex(6)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename=resource_path("src\log.log"), filemode="a", encoding="utf-8", format="[%(levelname)s] %(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    app = QApplication(sys.argv)
    mainWindow = Application()
    mainWindow.show() 
    sys.exit(app.exec_())

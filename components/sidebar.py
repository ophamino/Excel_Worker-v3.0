from typing import Optional

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize


class SideBar(QWidget):
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet("QWidget { background-color: #fff; }")
        self.setMinimumWidth(340)
        self.setMaximumWidth(340)
        
        logo = QLabel()
        pixmap = QPixmap("./components/images/logo.png")
        logo.setFixedHeight(340)
        logo.setFixedWidth(340)
        logo.setScaledContents(True)
        logo.setPixmap(pixmap)
        
        consumers_btn = QPushButton("Потребители")
        consumers_btn.setFixedHeight(70)
        consumers_btn.setFixedWidth(340)
        consumers_btn.setIcon(QIcon("./components/images/consumers.png"))
        consumers_btn.setIconSize(QSize(32, 32))
        
        bicu_btn = QPushButton("БИКУ")
        bicu_btn.setFixedHeight(70)
        bicu_btn.setFixedWidth(340)
        bicu_btn.setIcon(QIcon("./components/images/bicu.png"))
        bicu_btn.setIconSize(QSize(32, 32))
        
        balance_btn = QPushButton("Сводный баланс")
        balance_btn.setFixedHeight(70)
        balance_btn.setFixedWidth(340)
        balance_btn.setIcon(QIcon("./components/images/balance.png"))
        balance_btn.setIconSize(QSize(32, 32))
        
        reports_btn = QPushButton("Отчеты")
        reports_btn.setFixedHeight(70)
        reports_btn.setFixedWidth(340)
        reports_btn.setIcon(QIcon("./components/images/reports.png"))
        reports_btn.setIconSize(QSize(32, 32))
        
        history_btn = QPushButton("История операций")
        history_btn.setFixedHeight(70)
        history_btn.setFixedWidth(340)
        
        config_btn = QPushButton("Настройки")
        config_btn.setFixedHeight(70)
        config_btn.setFixedWidth(340)
        config_btn.setIcon(QIcon("./components/images/config.png"))
        config_btn.setIconSize(QSize(32, 32))
        
        
        help_btn = QPushButton("Справка")
        help_btn.setFixedHeight(70)
        help_btn.setFixedWidth(340)
        help_btn.setIcon(QIcon("./components/images/help.png"))
        help_btn.setIconSize(QSize(32, 32))
        help_btn.setStyleSheet("QIcon {margin: 0; padding: 0;}")
    
        layout = QVBoxLayout(self)
        layout.addWidget(logo)
        layout.addWidget(consumers_btn)
        layout.addWidget(bicu_btn)
        layout.addWidget(balance_btn)
        layout.addWidget(reports_btn)
        layout.addWidget(history_btn)
        layout.addWidget(config_btn)
        layout.addWidget(help_btn)
        
        
        layout.addStretch(1)
        self.setLayout(layout)
        
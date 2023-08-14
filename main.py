import sys 
from typing import Optional 
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout 
from PyQt5.QtGui import QIcon 
 
from components.sidebar import SideBar 
from components.content import Content
from components.interface import ConsumersContent
 
 
class MainWindow(QMainWindow): 
 
    def __init__(self, parent: Optional[QWidget] = None) -> None: 
        super().__init__(parent) 
        self.initUI() 
 
    def initUI(self) -> None: 
        self.setWindowTitle(" ") 
        self.setStyleSheet("QMainWindow { background-color: #FFFFFF; }") 
        self.setGeometry(100, 100, 1000, 800) 
        self.showMaximized() 
        self.setWindowIcon(QIcon("./components/images/qicon.png")) 
 
        main_widget = QWidget(self) 
        self.setCentralWidget(main_widget) 
        
        
        
        sidebar = SideBar(main_widget)
        content_widget = Content(main_widget)
        layout = QHBoxLayout(main_widget)
        layout.addWidget(sidebar)
        layout.addWidget(content_widget)
        layout.setStretch(0, 30)
        layout.setStretch(1, 70)
 
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show() 
    sys.exit(app.exec_())
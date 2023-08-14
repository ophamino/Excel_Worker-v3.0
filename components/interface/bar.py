import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ElectroLine")
        self.setStyleSheet("QMainWindow { background-color: #926EAE; }")
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()
        self.

        sidebar = QWidget(self)
        sidebar.setStyleSheet("QWidget { background-color: #926EAE; }")
        sidebar.setMinimumWidth(340)
        sidebar.setMaximumWidth(340)

        content = QWidget(self)
        content.setStyleSheet("QWidget { background-color: #7851A9; border-radius: 15px; }")

        self.addWidget(sidebar)
        self.addWidget(content)
        self.setStretch(0, 40)
        self.setStretch(1, 60)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_button1 = QPushButton("Потребители", sidebar)
        button_style = "QPushButton { color: #FFFFFF; border-radius: 5px; border: 2px solid #fff; height: 50px; width: 150px}"
        sidebar_button1.setStyleSheet(button_style)
        sidebar_button2 = QPushButton("БИКУ", sidebar)
        sidebar_button2.setStyleSheet(button_style)
        sidebar_button1.clicked.connect(self.button1Clicked)
        sidebar_button2.clicked.connect(self.button2Clicked)
        sidebar_layout.addWidget(sidebar_button1)
        sidebar_layout.addWidget(sidebar_button2)
        sidebar_layout.addStretch(1)
        

    def button1Clicked(self):
        
        label = QLabel("Button 1")

    def button2Clicked(self):
        label = QLabel("Button 2")
        # Обработчик нажатия на кнопку 2
        # Можно здесь добавить нужные виджеты в динамически изменяемое содержимое

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt

class CustomWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Установка фона
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(self.rect())

        # Рисование текста
        pen = QPen()
        pen.setColor(QColor(0, 0, 0))
        painter.setPen(pen)
        painter.setFont(QFont('Arial', 16))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication([])
    widget = CustomWidget("Привет, я кастомный виджет!")
    widget.resize(300, 100)
    widget.show()
    app.exec_()
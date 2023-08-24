from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog
from PyQt5.QtCore import QThread, pyqtSignal
from typing import Optional, Callable


class WorkerThread(QThread):
    finished_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self, func: Callable[[], int]):
        func()
        self.finished_signal.emit()

    def do_something_with_month(self):
        pass


class MonthButton(QPushButton):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(MonthButton, self).__init__("Сформировать", parent)
        self.setFixedSize(100, 50)
        self.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self) -> None:
        self.setEnabled(False)  # Делаем кнопку неактивной после нажатия

        month, ok = QInputDialog.getItem(self, "Выбор месяца", "Выберите месяц", ["что-то", "тотото", "Этотот"])

        if ok:
            worker = WorkerThread()
            worker.finished_signal.connect(self.on_worker_finished)
            worker.start()

    def on_worker_finished(self) -> None:
        self.setEnabled(True)  # Делаем кнопку снова активной

app = QApplication([])
button = MonthButton()
button.show()
app.exec()
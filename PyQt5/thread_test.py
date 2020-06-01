import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import QThread


class Loop(QThread):
    def run(self):
        while True:
            print("Estamos no loop")

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.resize(200, 200)
        self.button = QPushButton("Iniciar loop", self)
        self.button.clicked.connect(self.start_loop)
    
    def start_loop(self):
        self.thread_loop = Loop()
        self.thread_loop.start()


root = QApplication(sys.argv)
app = MainWindow()
app.show()
sys.exit(root.exec_())
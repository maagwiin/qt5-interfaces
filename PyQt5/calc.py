import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                            QLineEdit, QGridLayout, QSizePolicy)
from PyQt5.QtGui import QIcon


class Calculadora(QWidget):
    def __init__(self, parent=None):
        super(Calculadora, self).__init__(parent)
        self.settings()
        self.master_layout = QGridLayout()
        self.setLayout(self.master_layout)
        self.create_widgets()
        self.master_layout.addWidget(self.display, 0, 0, 1, 5)
    
    def settings(self):
        self.setFixedSize(400, 600)
        self.setWindowTitle("Magnu Calculator")
        self.setWindowIcon(QIcon("./static/cc.svg"))

    def create_widgets(self):
        # Display:
        self.display = QLineEdit()
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* { background: white; color: black; font-size: 40px; }'
        )
        # Buttons:
        self.btn_add(QPushButton('7'), 1, 0, 1, 1)
        self.btn_add(QPushButton('8'), 1, 1, 1, 1)
        self.btn_add(QPushButton('9'), 1, 2, 1, 1)
        self.btn_add(QPushButton('+'), 1, 3, 1, 1)
        self.btn_add(QPushButton('C'), 1, 4, 1, 1, 
                    lambda: self.display.setText(''),
                    'background: #d51409; color: #fff; font-weight: 700;'
                )

        self.btn_add(QPushButton('4'), 2, 0, 1, 1)
        self.btn_add(QPushButton('5'), 2, 1, 1, 1)
        self.btn_add(QPushButton('6'), 2, 2, 1, 1)
        self.btn_add(QPushButton('-'), 2, 3, 1, 1)
        self.btn_add(QPushButton('<-'), 2, 4, 1, 1,
                    lambda: self.display.setText(
                        self.display.text()[:-1]
                    ),
                    'background: #d5580d; color: #fff; font-weight: 700;'
                )

        self.btn_add(QPushButton('1'), 3, 0, 1, 1)
        self.btn_add(QPushButton('2'), 3, 1, 1, 1)
        self.btn_add(QPushButton('3'), 3, 2, 1, 1)
        self.btn_add(QPushButton('/'), 3, 3, 1, 1)
        self.btn_add(QPushButton('.'), 3, 4, 1, 1)

        self.btn_add(QPushButton(''), 4, 0, 1, 1)
        self.btn_add(QPushButton('0'), 4, 1, 1, 1)
        self.btn_add(QPushButton(''), 4, 2, 1, 1)
        self.btn_add(QPushButton('*'), 4, 3, 1, 1)
        self.btn_add(QPushButton('='), 4, 4, 1, 1,
                    self.eval_ig,
                    'background: #25d80d; color: #fff; font-weight: 700;'
                )



    def btn_add(self, btn, row, col, rowspan, colspan, func=None, style=None):
        self.master_layout.addWidget(btn, row, col, rowspan, colspan)
        if not func:    
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(func)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


    def eval_ig(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('ERRO!')



root = QApplication(sys.argv)
app = Calculadora()
app.show()
sys.exit(root.exec_())
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QLineEdit,
                            QHBoxLayout, QMessageBox, QRadioButton, QGroupBox,
                            QVBoxLayout)
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # Estética:
        self.setWindowTitle("Signal and Slot")
        self.setWindowIcon(QIcon("./static/car_bomb.svg"))
        # Primeiros widgets:
        self.button = QPushButton("Exibir mensagem")
        self.button.clicked.connect(self.exibir)
        self.line_edit = QLineEdit()
        # Group box dos widgets:
        self.groupbox = QGroupBox("Opções de Diálogo")
        # Opções:
        self.option_information = QRadioButton("Information")
        self.option_information.setChecked(True)
        self.option_warning = QRadioButton("Warning")    
        self.option_critical = QRadioButton("Critical")
        # Layout dos itens do groupbox:
        self.layout_options = QVBoxLayout()
        self.layout_options.addWidget(self.option_information)
        self.layout_options.addWidget(self.option_critical)
        self.layout_options.addWidget(self.option_warning)
        self.groupbox.setLayout(self.layout_options)
        # Layout do QPushButton e QLineEdit:
        self.layout_first_widget = QHBoxLayout()
        self.layout_first_widget.addWidget(self.line_edit)
        self.layout_first_widget.addWidget(self.button)
        # Main layout:
        self.layout_master = QVBoxLayout()
        self.layout_master.addLayout(self.layout_first_widget)
        self.layout_master.addWidget(self.groupbox)
        self.setLayout(self.layout_master)
        
    def exibir(self):
        self.text = self.line_edit.text()
        if self.option_information.isChecked():
            self.message_box = QMessageBox.information(self, "Retorno", self.text)
        if self.option_critical.isChecked():
            self.message_box = QMessageBox.critical(self, "Retorno", self.text)
        if self.option_warning.isChecked():
            self.message_box = QMessageBox.warning(self, "Retorno", self.text)


root = QApplication(sys.argv)
app = Window()
app.show()

sys.exit(root.exec_())


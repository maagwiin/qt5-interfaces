from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QLineEdit,
                            QHBoxLayout, QMessageBox, QRadioButton, QGroupBox,
                            QVBoxLayout)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # Estética:
        self.setWindowTitle("Signal and Slot")
 
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




if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = Window()
    app.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
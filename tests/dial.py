import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Meu Programa")

        self.edit = QLineEdit("Escreva seu nome aqui")
        self.button = QPushButton("Mostrar boas vindas")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print ("Olá {}".format(self.edit.text()))



if __name__ == '__main__':
     app = QApplication(sys.argv)
     form = Form()
     form.show()
     sys.exit(app.exec_())


import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot


@Slot()                                 # Usar slot para definir funções
def say_hello():                        # Função que imprime no console
    print("Button clicked, Hello!")


app = QApplication(sys.argv)            # Sempre

button = QPushButton("Click me")        # Cria um QpushBotton
button.clicked.connect(say_hello)       # Cria um conexão do botão com a função
button.show()                           # Mostra o botão
app.exec_()                             # Executa o app

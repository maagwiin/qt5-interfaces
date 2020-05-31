from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl


app = QApplication([])      # Criação do objeto app do tipo QApplication
view = QQuickView()         # Criando a quick view
url = QUrl("view.qml")      # Definindo a url para qqurl

view.setSource(url)         # Definindo source da view
view.show()                 # Mostrando a view
app.exec_()                 # Executando o aplicativo

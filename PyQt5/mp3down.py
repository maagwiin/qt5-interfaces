import sys
import requests
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                            QLineEdit, QFormLayout, QSystemTrayIcon,
                            QFileDialog)
from PyQt5.QtCore import QThread, QRegExp


class DownloaderMusic(QThread):
    def __init__(self, name, url, path):
        super(DownloaderMusic, self).__init__()
        self.path = path
        self.url = url
        self.name = name

    def run(self):
        mescl = self.path+"/"+self.name
        with open(mescl+'.mp3', 'wb') as f:
            f.write(requests.get(self.url).content)



class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.path = None
        self.settings()
        self.create_widgets()
        self.set_layout()
    
    def settings(self):
        self.setFixedSize(300, 120)
        self.setWindowTitle("Mp3 Downloader")

    def create_widgets(self):
        self.edit_name = QLineEdit()
        self.edit_url = QLineEdit()
        self.btn_destino = QPushButton("Select path", self)
        self.btn_destino.clicked.connect(self.select_path)
        self.btn_download = QPushButton("Download mp3", self)
        self.btn_download.clicked.connect(self.download)

    def set_layout(self):
        self.main_layout = QFormLayout()
        self.main_layout.addRow("Nome:", self.edit_name)
        self.main_layout.addRow("Url:", self.edit_url)
        self.main_layout.addRow("Selecionar destino:", self.btn_destino)
        self.main_layout.addRow(self.btn_download)
        self.setLayout(self.main_layout)

    def select_path(self):
        self.path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta")

    def download(self):
        if self.verify_fields():
            self.manage_inteface(False)
            self.thread_qt()

    def verify_fields(self):
        if self.path == None:
            return False
        else:
            strings = [self.edit_url.text(), self.edit_name.text(), self.path]
            regex_validate = QRegExp("*.mp3")
            regex_validate.setPatternSyntax(QRegExp.Wildcard)
            emptys = 0
            for string in strings:
                if len(string.split()) == 0:
                    emptys += 1
            if emptys == 0 and regex_validate.exactMatch(self.edit_url.text()):
                return True
    
    def thread_qt(self):
        url = self.edit_url.text()
        name = self.edit_name.text()
        path = self.path
        self.thre = DownloaderMusic(name, url, path)
        self.thre.finished.connect(self.downfin)
        self.thre.start()

    def manage_inteface(self, state):
        self.btn_download.setEnabled(state)
        self.edit_name.setEnabled(state)
        self.edit_url.setEnabled(state)
        self.btn_destino.setEnabled(state)

    def downfin(self):
        self.notifyIcon = QSystemTrayIcon()
        self.notifyIcon.setVisible(True)
        self.notifyIcon.showMessage(
            "Download finalizado",
            u"O download da sua músoca foi realizado com sucesso.",
            QSystemTrayIcon.Information, 3000)
        self.manage_inteface(True)


root = QApplication(sys.argv)
app = MainWindow()
app.show()
sys.exit(root.exec_())
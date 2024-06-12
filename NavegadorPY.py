# Bibliotecas
from PyQt5.QtCore import *  # Funções centrais
from PyQt5.QtWidgets import *  # Interface gráfica
from PyQt5.QtWebEngineWidgets import *
import sys  # Funções e variáveis do sistema


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):  # Método inicializador
        super(MainWindow, self).__init__(*args, **kwargs)  # Inicializador da classe

        self.setWindowTitle("NavegadorPY")  # Nome da janela

        self.showMaximized()  # Janela Maximizada

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))  # URL principal

        self.setCentralWidget(self.browser)

        self.show()


app = QApplication(sys.argv)
window = MainWindow()  # Instancia

app.exec()

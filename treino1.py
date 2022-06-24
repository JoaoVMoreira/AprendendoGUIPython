import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cima = 200
        self.lado = 420
        self.altura = 500
        self.largura = 500
        self.titulo = "Meu primeiro teste"
        self.Carrega_Janela()

    def Carrega_Janela(self):
        self.setGeometry(self.lado, self.cima, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)
j = JanelaPrincipal()
sys.exit(aplicacao.exec_())
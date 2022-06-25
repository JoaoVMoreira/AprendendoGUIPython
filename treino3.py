import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Jane_Treino(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cima = 100
        self.lado = 200
        self.altura = 600
        self.largura = 400
        self.titulo = "Treino 3"

        primeiro_botao = QPushButton('Botão 1', self)
        primeiro_botao.move(50, 80)
        primeiro_botao.resize(100, 70)
        primeiro_botao.setStyleSheet('QPushButton {background-color: blue; font-size: 15px}')
        primeiro_botao.clicked.connect(self.clicado1)

        self.aparece_janela()


    def aparece_janela(self):
        self.setGeometry(self.lado, self.cima, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def clicado1(self):
        print('Você clicou no primeiro botão')

aplicacao = QApplication(sys.argv)
j = Jane_Treino()
sys.exit(aplicacao.exec_())
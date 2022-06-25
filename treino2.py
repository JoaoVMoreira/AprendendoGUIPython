import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,  QToolTip

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.lado = 200
        self.altura = 500
        self.largura = 500
        self.titulo = 'Treinando criação de botões'

        botao1 = QPushButton('Botão 1', self)
        botao1.move(100, 100)
        botao1.resize(125, 75)
        botao1.setStyleSheet('QPushButton {background-color: red; font-size: 20px}')
        botao1.clicked.connect(self.Botao1_Clicado)

        botao2 = QPushButton('Botão2', self)
        botao2.move(250, 100)
        botao2.resize(125, 75)
        botao2.setStyleSheet('QPushButton {background-color: blue; font-size: 20px}')
        botao2.clicked.connect(self.Botao2_Clicado)

        self.CarregaJanela()

    def CarregaJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def Botao1_Clicado(self):
        print('Você clicou no botão 1')
    
    def Botao2_Clicado(self):
        print('Você clicou no botão 2')


aplicacao = QApplication(sys.argv)
b = Janela()
sys.exit(aplicacao.exec_())
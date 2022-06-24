import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip #importar as classes QPushButton e QToolTip

class Botao(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.lado = 100
        self.altura = 600
        self.largura = 800
        self.titulo = 'Criando meu primeiro botão'

        botao1 = QPushButton('Botão 1', self) # Criando botão
        botao1.move(100, 100) #Definindo local do botao
        botao1.resize(150, 100) # Definindo dimensoes do botao
        botao1.setStyleSheet('QPushButton {background-color: blue; font-size: 20px}') # Formatando botão
        botao1.clicked.connect(self.Botao_clicado)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(250, 250)
        botao2.resize(150, 100)
        botao2.setStyleSheet('QPushButton {background-color: red; font-size: 20px}')
        botao2.clicked.connect(self.Botao_clicado2)

        self.Carregar_Janela()

        

    def Carregar_Janela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def Botao_clicado(self):
        print('Botão 1')
    
    def Botao_clicado2(self):
        print('Botão 2')

aplicacao = QApplication(sys.argv)
b = Botao()
sys.exit(aplicacao.exec_())
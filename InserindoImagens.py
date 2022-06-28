import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui # IMportar QTGui

class Imagens(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.lado = 100
        self.altura = 600
        self.largura = 500
        self.titulo = 'Treinando Labels'

        botao1 = QPushButton('Botão 1', self)
        botao1.move(150, 200)
        botao1.resize(100, 65)
        botao1.setStyleSheet('QPushButton {background-color: red; font-size: 15px}')
        botao1.clicked.connect(self.botao1Clicado)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(270, 200)
        botao2.resize(100, 65)
        botao2.setStyleSheet('QPushButton {background-color: blue; font-size: 15px}')
        botao2.clicked.connect(self.botao2Clicado)

        self.label1 = QLabel(self)
        self.label1.setText('Olá, mundo!')
        self.label1.move(50,100)
        self.label1.setStyleSheet('QLabel {font-size: 20px; color: green; font: bold}')
        self.label1.resize(300, 25)

        self.carro = QLabel(self)
        self.carro.move(50, 400)
        self.resize(300, 100)

        self.CarregaJanela()

    def CarregaJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botao1Clicado(self):
        self.label1.setText('Carro 1')
        self.label1.setStyleSheet('QLabel {font-size: 20px; color: red; font: bold}')
        self.carro.setPixmap(QtGui.QPixmap('carroVermelho.png'))

    def botao2Clicado(self):
        self.label1.setText('Carro 2')
        self.label1.setStyleSheet('QLabel {font-size: 20px; color: blue; font: bold}')
        self.carro.setPixmap(QtGui.QPixmap('carroAzul.png'))

aplicacao = QApplication(sys.argv)
i = Imagens()
sys.exit(aplicacao.exec_())

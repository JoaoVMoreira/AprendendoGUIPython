# Treinando labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel

class Label(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.lado = 100
        self.altura = 600
        self.largura = 500
        self.titulo = 'Treinando Labels'

        botaoa = QPushButton('Botão 1', self)
        botaoa.move(150, 200)
        botaoa.resize(100, 65)
        botaoa.setStyleSheet('QPushButton {background-color: red; font-size: 15px}')
        botaoa.clicked.connect(self.botaoaClicado)

        botaob = QPushButton('Botão 2', self)
        botaob.move(270, 200)
        botaob.resize(100, 65)
        botaob.setStyleSheet('QPushButton {background-color: blue; font-size: 15px}')
        botaob.clicked.connect(self.botaobClicado)

        self.label1 = QLabel(self)
        self.label1.setText('Clique em um botão: ')
        self.label1.move(100, 100)
        self.label1.setStyleSheet('QLabel {font-size: 20px; color: green; font: bold}')
        self.label1.resize(300, 25)

        self.CarregaJanela()
    
    def CarregaJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botaoaClicado(self):
        self.label1.setText('Você clicou no botao 1!')
        self.label1.setStyleSheet('QLabel {font-size: 20px; color: blue; font: bold}')

    def botaobClicado(self):
        self.label1.setText('Você clicou no botao 2!')
        self.label1.setStyleSheet('QLabel {font-size: 20px; color: red; font: bold}')

aplicacao = QApplication(sys.argv)
l = Label()
sys.exit(aplicacao.exec_())
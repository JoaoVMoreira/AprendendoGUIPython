import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit # Adiciona o componente QLineEdit
from PyQt5 import QtGui

class CaixaDeTexto(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.lado = 100
        self.altura = 600
        self.largura = 800
        self.titulo = 'Treinando Labels'

        self.caixa_texto = QLineEdit(self) # Criando uma caixa de texto 
        self.caixa_texto.move(500, 20)
        self.caixa_texto.resize(200, 20)

        botao1 = QPushButton('Botão 1', self)
        botao1.move(150, 200)
        botao1.resize(100, 65)
        botao1.setStyleSheet('QPushButton {background-color: blue; font-size: 15px}')
        botao1.clicked.connect(self.botao1Clicado)

        botao_caixa = QPushButton('Enviar texto', self)
        botao_caixa.move(500, 200)
        botao_caixa.resize(100, 65)
        botao_caixa.setStyleSheet('QPushButton {background-color: green; font-size: 15px}')
        botao_caixa.clicked.connect(self.CaixaTextoCriada)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(270, 200)
        botao2.resize(100, 65)
        botao2.setStyleSheet('QPushButton {background-color: red; font-size: 15px}')
        botao2.clicked.connect(self.botao2Clicado)

        self.label1 = QLabel(self)
        self.label1.move(100, 100)
        self.label1.setText('Olá, mundo!')
        self.label1.setStyleSheet('QLabel {font-size: 20px; font: bold; color: green}')
        self.label1.resize(300, 25)

        self.label_caixa = QLabel(self)
        self.label_caixa.move(500, 100)
        self.label_caixa.setText('Digitou')
        self.label_caixa.setStyleSheet('QLabel {font-size: 20px; font: bold; color: green}')
        self.label_caixa.resize(300, 25)

        self.carro = QLabel(self)
        self.carro.move(50, 400)
        self.resize(100, 400)

        self.CarregaJanela()

    def CarregaJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botao1Clicado(self):
        self.label1.setText('Carro 1')
        self.label1.setStyleSheet('QLabel {font-size: 20px; font: bold; color: blue}')
        self.carro.setPixmap(QtGui.QPixmap('carroAzul.jpg'))

    def CaixaTextoCriada (self):
        conteudo = self.caixa_texto.text()
        self.label_caixa.setText(conteudo)
    
    def botao2Clicado(self):
        self.label1.setText('Carro 2')
        self.label1.setStyleSheet('QLabel {font-size: 20px; font: bold; color: red}')
        self.carro.setPixmap(QtGui.QPixmap('carroVermelho.png'))


aplicacao = QApplication(sys.argv)
c = CaixaDeTexto()
sys.exit(aplicacao.exec_())
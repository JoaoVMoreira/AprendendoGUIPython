import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel #Importar Qlabel

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.lado = 100
        self.altura = 600
        self.largura = 500

        botao1 = QPushButton('Botão 1', self)
        botao1.move(100, 250)
        botao1.resize(100, 65)
        botao1.setStyleSheet('QPushButton {background-color: red; font-size: 15px}')
        botao1.clicked.connect(self.botao1Clicado)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(220, 250)
        botao2.resize(100, 65)
        botao2.setStyleSheet('QPushButton {background-color: blue; font-size: 15px}')
        botao2.clicked.connect(self.botao2Clicado)

        self.label1 = QLabel(self) #Criando a label
        self.label1.setText("Aperte um botão! ")
        self.label1.move(100, 100) #Definindo a posição da label
        self.label1.setStyleSheet('QLabel {font-size: 15px; font: bold; color: green}') # Formatando label
        self.label1.resize(300, 25)



        self.titulo = 'Criando minha primeira Label'

        self.CarregaJanela()

    def CarregaJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botao1Clicado(self):
        self.label1.setText('Você clicou no botão 1') #Definindo o texto da label ao clicar no botão 1
        self.label1.setStyleSheet('QLabel {font-size: 18px; font: bold; color: red}')
    
    def botao2Clicado(self):
        self.label1.setText('Você clicou no botão 2') #Definindo o texto da label ao clicar no botão 1
        self.label1.setStyleSheet('QLabel {font-size: 18px; font: bold; color: blue}')

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
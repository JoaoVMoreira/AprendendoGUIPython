import sys #padrão para PYQT5
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela (QMainWindow): # Cria-se uma classe chamando QMainWindow
    def __init__ (self): #Criando construtor
            super().__init__() #Superclasse chamando o construtor

            self.topo = 100 #Altura onde a janela aparece na tela
            self.esquerda = 100 #Distancia do lado esquerdo da tela
            self.largura = 800 #Definindo largura da janela
            self.altura = 600 #Definindo altura da janela
            self.titulo = "Olá, Mundo!" # Definindo titulo da janela
            self.CarregarJanela()
        
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura) #Criando a janela de acordo com os parâmetros informados anteriormente 
        self.setWindowTitle(self.titulo) #Criar o titulo da janela
        self.show() #Mostrar a janela

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
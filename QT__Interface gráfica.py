import sys
from PyQt4 import QtGui
'''
app = QtGui.QApplication(sys.argv) # inicializa interface gráfica

win = QtGui.QWidget() # cria uma janela
win.resize(250,150) # define o tamanho da janela
win.move(300,300) # define a posição inicial da janela na tela
win.setWindowTitle('Hello World') # define título da janela
win.show() # mostra janela na tela
app.exec_() # executa interface gráfica
'''
'''
_______________________________________________________________________________
'''

class Nome(QtGui.QWidget):
    def __init__(self, nome):
        super(Nome, self).__init__()
        self.resize(250,150)
        self.move(300,300)
        lbl = QtGui.QLabel(nome, self)
        lbl.move(10,10)

class Sobrenome(QtGui.QWidget):
    def __init__(self, sobrenome):
        super(Sobrenome, self).__init__()
        self.resize(250,150)
        self.move(300,300)
        lbl = QtGui.QLabel(sobrenome, self)
        lbl.move(10,10)


class JogoVelha(QtGui.QWidget):
    def __init__(self):
        super(JogoVelha, self).__init__()
        self.resize(500,350)
        self.move(400,200)
        le1 = QtGui.QLineEdit('', self)
        le2 = QtGui.QLineEdit('', self)
        le3 = QtGui.QLineEdit('', self)
        le4 = QtGui.QLineEdit('', self)
        le5 = QtGui.QLineEdit('', self)
        le6 = QtGui.QLineEdit('', self)
        le7 = QtGui.QLineEdit('', self)
        le8 = QtGui.QLineEdit('', self)
        le9 = QtGui.QLineEdit('', self)
        le1.move(10,10)
        le2.move(150,10)
        le3.move(290,10)
        le4.move(10,35)
        le5.move(150,35)
        le6.move(290,35)
        le7.move(10,60)
        le8.move(150,60)
        le9.move(290,60)


class Formulario(QtGui.QWidget):
    def __init__(self):
        super(Formulario, self).__init__()
        self.setGeometry(300,300,250,150)
        layout = QtGui.QGridLayout(self)
        layout.addWidget(QtGui.QPushButton('Um', self))
        layout.addWidget(QtGui.QPushButton('Dois', self))
        layout.addWidget(QtGui.QPushButton('Três', self))
        layout.addWidget(QtGui.QPushButton('Quatro', self))



class ActionClick(QtGui.QWidget):
    def __init__(self):
        super(ActionClick, self).__init__()
        self.setGeometry(300,300,250,150)
        layout = QtGui.QVBoxLayout(self)
        
        botao = QtGui.QPushButton('Clique', self)
        self.texto = QtGui.QLabel('')
        
        botao.clicked.connect(self.handleClicked)
        
              
        
        layout.addWidget(self.texto)
        layout.addWidget(botao)
    
    def handleClicked(self):
        self.texto.setText('Clicado')



class ScrollArea(QtGui.QWidget):
    
    def __init__(self):
        super(ScrollArea, self).__init__()
        self.setGeometry(0,0,250,150)
        self.centerOnScreen()
        self.setMinimumSize(250,150)
        self.setMaximumSize(550,450)
        
        
    def centerOnScreen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move( ( (resolution.width() / 2 ) - (self.frameSize().width() / 2 ) ) , ( (resolution.height() / 2 ) - ( self.frameSize().height() / 2 ) ) )
  






if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    win = Nome('Rodrigo')
    win2 = Sobrenome('Gikas')
    win.show()
    app.exec_()
    win2.show()
    app.exec_()
    
    win3 = JogoVelha()
    win3.show()
    app.exec_()
    
    win4 = Formulario()
    win4.show()
    app.exec_()
    
    win5 = ActionClick()
    win5.show()
    app.exec_()
    
    win6 = ScrollArea()
    win6.show()
    app.exec_()

    
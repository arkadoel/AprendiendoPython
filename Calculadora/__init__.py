#para ejecutarlo 'python3 ./__init__.py'
import sys
from PyQt4 import QtGui, QtCore

class ventana(QtGui.QWidget):

    def __init__(self):
        super(ventana,self).__init__()
        self.setGeometry(150, 150, 250, 200)
        self.setWindowTitle('PyCalculadora')
        self.setWindowIcon(QtGui.QIcon('calcIcon.png'))
        self.setFixedSize(250, 200)

        self.opAnterior=0

        vbox = QtGui.QVBoxLayout()
        self.grid = QtGui.QGridLayout()

        self.texto = QtGui.QLineEdit('', self)
        self.texto.setMinimumSize(100, 35)
        self.texto.setAlignment(QtCore.Qt.AlignRight)

        #fuente Courier, 20, negrita y no italica
        self.fuente = QtGui.QFont("Courier", 16, QtGui.QFont.Bold, False)
        self.texto.setFont(self.fuente)

        vbox.addStrut(10)
        vbox.addWidget(self.texto)

        ''' Falla el tema de las señales
        b = 0
        for i in range(0, 4):
            for j in range(0, 3):
                boton = QtGui.QPushButton(str(b), self)
                boton.clicked.connect(lambda: self.click_boton( str(b)))
                grid.addWidget(boton, i, j)
                b += 1

        '''
        self.initButtons()
        self.init_action_buttons()


        vbox.addLayout(self.grid)
        vbox.addStrut(0)
        self.setLayout(vbox)

    def initButtons(self):
        self.b0 = QtGui.QPushButton('0', self)
        self.b1 = QtGui.QPushButton('1', self)
        self.b2 = QtGui.QPushButton('2', self)
        self.b3 = QtGui.QPushButton('3', self)
        self.b4 = QtGui.QPushButton('4', self)
        self.b5 = QtGui.QPushButton('5', self)
        self.b6 = QtGui.QPushButton('6', self)
        self.b7 = QtGui.QPushButton('7', self)
        self.b8 = QtGui.QPushButton('8', self)
        self.b9 = QtGui.QPushButton('9', self)
        self.bpunto = QtGui.QPushButton(',', self)

        self.b0.setFont(self.fuente)
        self.b1.setFont(self.fuente)
        self.b2.setFont(self.fuente)
        self.b3.setFont(self.fuente)
        self.b4.setFont(self.fuente)
        self.b5.setFont(self.fuente)
        self.b6.setFont(self.fuente)
        self.b7.setFont(self.fuente)
        self.b8.setFont(self.fuente)
        self.b9.setFont(self.fuente)
        self.bpunto.setFont(self.fuente)

        self.b0.clicked.connect(lambda: self.click_boton(0))
        self.b1.clicked.connect(lambda: self.click_boton(1))
        self.b2.clicked.connect(lambda: self.click_boton(2))
        self.b3.clicked.connect(lambda: self.click_boton(3))
        self.b4.clicked.connect(lambda: self.click_boton(4))
        self.b5.clicked.connect(lambda: self.click_boton(5))
        self.b6.clicked.connect(lambda: self.click_boton(6))
        self.b7.clicked.connect(lambda: self.click_boton(7))
        self.b8.clicked.connect(lambda: self.click_boton(8))
        self.b9.clicked.connect(lambda: self.click_boton(9))
        self.bpunto.clicked.connect(lambda: self.click_boton('.'))

        self.grid.addWidget(self.b0, 4, 0)
        self.grid.addWidget(self.b1, 3, 0)
        self.grid.addWidget(self.b2, 3, 1)
        self.grid.addWidget(self.b3, 3, 2)
        self.grid.addWidget(self.b4, 2, 0)
        self.grid.addWidget(self.b5, 2, 1)
        self.grid.addWidget(self.b6, 2, 2)
        self.grid.addWidget(self.b7, 1, 0)
        self.grid.addWidget(self.b8, 1, 1)
        self.grid.addWidget(self.b9, 1, 2)
        self.grid.addWidget(self.bpunto, 4, 1)

    def init_action_buttons(self):
        self.btnAdd = QtGui.QPushButton('+', self)
        self.btnResta = QtGui.QPushButton('-', self)
        self.btnMult = QtGui.QPushButton('x', self)
        self.btnIgual = QtGui.QPushButton('=', self)
        self.btnClear = QtGui.QPushButton('C', self)

        #el simbolo division lo cogemos del unicode
        divi = 247
        self.btndiv = QtGui.QPushButton(''.join(chr(divi)), self)

        self.btnAdd.setFont(self.fuente)
        self.btndiv.setFont(self.fuente)
        self.btnMult.setFont(self.fuente)
        self.btnResta.setFont(self.fuente)
        self.btnIgual.setFont(self.fuente)
        self.btnClear.setFont(self.fuente)

        self.btnAdd.clicked.connect(lambda: self.click_accion('suma'))
        self.btnResta.clicked.connect(lambda: self.click_accion('resta'))
        self.btndiv.clicked.connect(lambda: self.click_accion('divide'))
        self.btnMult.clicked.connect(lambda: self.click_accion('multiplica'))
        self.btnIgual.clicked.connect(self.click_Igual)
        self.btnClear.clicked.connect(lambda: self.click_accion('Clear'))

        self.grid.addWidget(self.btnClear, 0, 3)
        self.grid.addWidget(self.btnAdd, 4, 3)
        self.grid.addWidget(self.btnResta, 3, 3)
        self.grid.addWidget(self.btnMult, 2, 3)
        self.grid.addWidget(self.btndiv, 1, 3)
        self.grid.addWidget(self.btnIgual, 4, 2)

    def click_Igual(self):
        if self.texto.text() != '':
            if self.accion == 'suma':
                opActual = float(self.texto.text())
                resultado = self.opAnterior + opActual
                self.texto.setText(str(resultado))
            elif self.accion == 'resta':
                opActual = float(self.texto.text())
                resultado = self.opAnterior - opActual
                self.texto.setText(str(resultado))
            elif self.accion == 'multiplica':
                opActual = float(self.texto.text())
                resultado = self.opAnterior * opActual
                self.texto.setText(str(resultado))
            elif self.accion == 'divide':
                try:
                    opActual = float(self.texto.text())
                    resultado = self.opAnterior / opActual
                    self.texto.setText(str(resultado))
                except ZeroDivisionError:
                    infinito = 8734
                    self.texto.setText(''.join(chr(infinito)))

    def click_accion(self, name):
        if name != 'clear':
            self.accion = name
            if self.texto.text() != '':
                self.opAnterior = float(self.texto.text())
            else:
                self.opAnterior = 0
        else:
            self.opAnterior = 0
            self.accion = ''

        self.texto.setText('')

    def click_boton(self, name):
        if self.texto.text() == '' and str(name) == '.':
            self.texto.setText('0.')
        elif self.texto.text().__contains__('.') and str(name) == '.':
            #lo ignoramos, ya hay punto
            pass
        else:
            self.texto.setText(self.texto.text() + str(name))



def main():
    app = QtGui.QApplication(sys.argv)

    v = ventana()
    v.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
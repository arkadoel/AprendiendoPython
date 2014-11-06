from PyQt4 import QtGui
import sys

class Ventana(QtGui.QWidget):

    def __init__(self):
        super(Ventana,self).__init__()

        #setGeometry (x,y, ancho, alto)
        self.setGeometry(100,100,500,400)
        self.setWindowTitle('Primera vetana')
        self.setWindowIcon(QtGui.QIcon('qtIcon.png'))

        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    win = Ventana()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


#segunda ventana
from PySide import QtGui
import sys

class Ventana(QtGui.QWidget):

    def __init__(self):
        super(Ventana, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('qtIcon.png'))

        self.show()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    win = Ventana()
    sys.exit(app.exec_())
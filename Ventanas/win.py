#probando pyside
from PySide import QtGui
import sys


def main():
    app = QtGui.QApplication(sys.argv)

    wid = QtGui.QWidget()
    wid.resize(250, 150)
    wid.setWindowTitle('Primera ventana')
    wid.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
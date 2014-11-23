__author__ = "https://github.com/arkadoel"
__version__ = "0.1.2"

"""
    Aplicacion para llevar una agenda telefonica
"""
import sys
from PyQt4 import QtGui
from vprincipal import vPrincipal

def main():
    app = QtGui.QApplication(sys.argv)
    v = vPrincipal()
    v.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

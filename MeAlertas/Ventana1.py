__author__ = 'Arkadoel'
from PyQt4 import QtGui
from Constantes import const

class vPrincipal(QtGui.QDialog):
    def __init__(self, parent=None):
        super(vPrincipal, self).__init__(parent)
        self.setWindowTitle('MeAlertas ' + const.APP_VERSION)
        self.setWindowIcon(QtGui.QIcon(const.ICONO))
        #establecemos el estilo de la ventana
        QtGui.qApp.setStyle('Cleanlooks')
        self.setGeometry(100,100,700,500)
        self.canExit = False

        self.show()

    def closeEvent(self, event):
        # do stuff
        if self.canExit:
            event.accept() # let the window close
        else:
            event.ignore()
            self.hide()


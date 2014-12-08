__author__ = 'Arkadoel'
from PyQt4 import QtGui
from Constantes import const

class vPrincipal(QtGui.QWidget):
    def __init__(self):
        super(vPrincipal, self).__init__()
        self.setWindowTitle('MeAlertas ' + const.__APP_VERSION__)
        #establecemos el estilo de la ventana
        QtGui.qApp.setStyle('Cleanlooks')


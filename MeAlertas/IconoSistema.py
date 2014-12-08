__author__ = 'Arkadoel'
from PyQt4 import QtGui
from PyQt4.QtCore import *

class iconoSistema:

    def __init__(self, parent=None):
        self.icon = QtGui.QIcon("C:/Users/Arkadoel/Pictures/PANZER/cat-icon.png")
        self.iconoSalir = QtGui.QIcon.fromTheme("exit")
        self.tray = QtGui.QSystemTrayIcon(parent = parent)
        self.tray.setIcon(self.icon)

        self.agregarMenu()
        self.tray.show()

    def agregarMenu(self):
        menu = QtGui.QMenu()
        menu.addAction(self.icon, "&Ver Alertas")
        menu.addSeparator()
        exitAccion = menu.addAction(self.iconoSalir, "&Salir")
        exitAccion.triggered.connect(QtCore.QCoreApplication.instante().quit)
        self.tray.setContextMenu(menu)
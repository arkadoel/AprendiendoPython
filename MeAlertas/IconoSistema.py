__author__ = 'Arkadoel'
from PyQt4 import QtGui
from PyQt4.QtCore import *
import threading
from Ventana1 import vPrincipal
from Constantes import const

class IconoSistema():
    SEG_MENSAJE = 5

    def __init__(self, parent=None):
        self.daemon = threading.Thread(target=self.iniciar(parent), name='DemonioReloj')
        self.daemon.setDaemon(True)
        self.padre = parent

    def iniciar(self, parent):
        self.icon = QtGui.QIcon(const.ICONO)
        self.iconoSalir = QtGui.QIcon.fromTheme("exit")
        self.tray = QtGui.QSystemTrayIcon(parent=parent)
        self.tray.setIcon(self.icon)

        self.agregarMenu()

        self.tray.show()

    def agregarMenu(self):
        menu = QtGui.QMenu()
        verAlertasAction= menu.addAction(self.icon, "&Ver Alertas")
        menu.addSeparator()
        exitAction = menu.addAction(self.iconoSalir, "&Salir")

        exitAction.triggered.connect(QCoreApplication.instance().quit)
        verAlertasAction.triggered.connect(lambda: self.verVentanaAlertas())

        self.tray.setVisible(True)

        self.tray.setContextMenu(menu)
        self.showMessage('Aplicacion iniciada')
        const.SYSTRAY = self

    def showMessage(self, mensaje):

        self.tray.showMessage('MeAlertas ' + const.APP_VERSION,
                              mensaje,
                              QtGui.QSystemTrayIcon.Information,
                              self.SEG_MENSAJE * 1000)

    def verVentanaAlertas(self):
        const.v_PRINCIPAL = vPrincipal()
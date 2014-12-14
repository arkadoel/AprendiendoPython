__author__ = 'Arkadoel'
from PyQt4 import QtGui
from PyQt4.QtCore import *
import threading
from Ventana1 import vPrincipal
from Constantes import const

class IconoSistema():
    SEG_MENSAJE = 5 #segundos que permanecerá visible el mensaje

    def __init__(self, parent=None):
        self.daemon = threading.Thread(target=self.iniciar(parent), name='DemonioReloj')
        self.daemon.setDaemon(True)
        self.padre = parent

    def iniciar(self, parent):
        self.icon = QtGui.QIcon(const.ICONO)
        self.iconoSalir = QtGui.QIcon.fromTheme("exit")
        self.iconoLista = QtGui.QIcon(const.ICONO_LISTA)
        self.tray = QtGui.QSystemTrayIcon(parent=parent)
        self.tray.setIcon(self.icon)

        self.agregarMenu()

        self.tray.show()

    def agregarMenu(self):
        menu = QtGui.QMenu()
        ultimaAlertaAction = menu.addAction(self.icon, 'Ver &Ultima alerta')
        verAlertasAction= menu.addAction(self.iconoLista, "&Ver Alertas")
        menu.addSeparator()
        exitAction = menu.addAction(self.iconoSalir, "&Salir")

        exitAction.triggered.connect(QCoreApplication.instance().quit)
        verAlertasAction.triggered.connect(lambda: self.verVentanaAlertas())
        ultimaAlertaAction.triggered.connect(lambda: self.verUltimaAlerta())

        self.tray.activated.connect(self.onTrayIconActivated)

        self.tray.setVisible(True)

        self.tray.setContextMenu(menu)
        self.showMessage('Aplicacion iniciada')
        const.SYSTRAY = self

    def onTrayIconActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
            #ignorar
            pass
        elif reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.verVentanaAlertas()

    def showMessage(self,hora=None, mensaje=None):
        self.ultimaAlerta = (hora, mensaje)
        self.tray.showMessage(hora,
                              mensaje,
                              QtGui.QSystemTrayIcon.Information,
                              self.SEG_MENSAJE * 1000)

    def verVentanaAlertas(self):
        const.v_PRINCIPAL = vPrincipal()
        #const.v_PRINCIPAL = ventana()

    def verUltimaAlerta(self):
        hora = self.ultimaAlerta[0]
        mensaje = self.ultimaAlerta[1]
        self.showMessage(hora, mensaje)
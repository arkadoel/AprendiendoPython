__author__ = 'Arkadoel'
from PyQt4 import QtGui, QtCore
from Constantes import const
from datos.TablaAlerta import tbAlertas, Alerta


class vPrincipal(QtGui.QDialog):
    def __init__(self, parent=None):
        super(vPrincipal, self).__init__(parent)

        #variables
        self.alertaActual = Alerta()

        self.setWindowTitle('MeAlertas ' + const.APP_VERSION)
        self.setWindowIcon(QtGui.QIcon(const.ICONO))

        self.maquetacion()

        #establecemos el estilo de la ventana
        QtGui.qApp.setStyle('Cleanlooks')
        self.setGeometry(100,100,700,500)
        self.canExit = False

        self.show()

    def maquetacion(self):
        self.gridFondo = QtGui.QGridLayout()
        self.gridFondo.setObjectName("gridFondo")
        self.vboxHoras = QtGui.QVBoxLayout()
        self.vboxHoras.setObjectName("vboxHoras")
        self.gridPropiedades = QtGui.QGridLayout()

        self.gridFondo.addLayout(self.vboxHoras, 0, 0, 1, 1)
        self.gridFondo.addLayout(self.gridPropiedades, 0, 2, 1, 1)

        #controles
        self.initControles()
        self.vboxHoras.addWidget(self.lblHoras)
        self.vboxHoras.addWidget(self.lstHoras)

        #zona propiedades
        self.gridPropiedades.addWidget(self.lblHora, 0, 0)
        self.gridPropiedades.addWidget(self.txtHora, 0, 1)

        self.gridPropiedades.addWidget(self.lblMensaje, 1,0, 1, 4)
        self.gridPropiedades.addWidget(self.txtMensaje, 2,0, 1, 4)

        self.gridPropiedades.addWidget(self.lblDiaSemana, 3, 1)
        self.gridPropiedades.addWidget(self.chkLunes, 4, 1)
        self.gridPropiedades.addWidget(self.chkMartes, 5, 1)
        self.gridPropiedades.addWidget(self.chkMiercoles, 6, 1)
        self.gridPropiedades.addWidget(self.chkJueves, 7, 1)
        self.gridPropiedades.addWidget(self.chkViernes, 8, 1)
        self.gridPropiedades.addWidget(self.chkSabado, 9, 1)
        self.gridPropiedades.addWidget(self.chkDomingo, 10, 1)

        self.gridPropiedades.addWidget(self.btnNuevo, 4, 3)
        self.gridPropiedades.addWidget(self.btnGuardar, 5, 3)
        self.gridPropiedades.addWidget(self.btnEliminar, 6, 3)

        self.setLayout(self.gridFondo)

    def initControles(self):
        self.lblHoras = QtGui.QLabel("Horas", self)
        self.lblHoras.setObjectName("lblHoras")

        self.lstHoras = QtGui.QListWidget(self)
        self.lstHoras.setFixedWidth(130)
        self.lstHoras.itemActivated.connect(self.elementoListaSeleccionado)

        self.lblHora = QtGui.QLabel("Hora:", self)
        self.lblHora.setFixedWidth(50)
        self.lblDiaSemana = QtGui.QLabel("Dia de la semana: ", self)

        self.txtHora = QtGui.QLineEdit(self)
        self.txtHora.setFixedWidth(130)
        self.lblMensaje= QtGui.QLabel("Mensaje a mostrar: ", self)
        self.txtMensaje = QtGui.QTextEdit(self)
        self.txtMensaje.setFixedHeight(120)

        self.chkLunes = QtGui.QCheckBox('Lunes', self)
        self.chkMartes = QtGui.QCheckBox('Martes', self)
        self.chkMiercoles = QtGui.QCheckBox('Miercoles', self)
        self.chkJueves = QtGui.QCheckBox('Jueves', self)
        self.chkViernes = QtGui.QCheckBox('Viernes', self)
        self.chkSabado = QtGui.QCheckBox('Sabado', self)
        self.chkDomingo = QtGui.QCheckBox('Domingo', self)
        self.espacioH = QtGui.QLabel(' ',self)
        self.espacioH.setFixedWidth(50)

        self.btnNuevo = QtGui.QPushButton(QtGui.QIcon(const.ICONO_NUEVO), 'Nueva',  self)
        self.btnNuevo.setFixedWidth(120)
        self.btnNuevo.setFixedHeight(30)
        self.btnNuevo.clicked.connect(lambda: self.clickAccion('Add'))

        self.btnGuardar = QtGui.QPushButton(QtGui.QIcon(const.ICONO_GUARDAR),'Guardar', self)
        self.btnGuardar.setFixedWidth(120)
        self.btnGuardar.setFixedHeight(30)
        self.btnGuardar.clicked.connect(lambda: self.clickAccion('Save'))

        self.btnEliminar = QtGui.QPushButton(QtGui.QIcon(const.ICONO_ELIMINAR),'Eliminar', self)
        self.btnEliminar.setFixedWidth(120)
        self.btnEliminar.setFixedHeight(30)
        self.btnEliminar.clicked.connect(lambda: self.clickAccion('Del'))

        self.initListaHoras()
        self.limpiarControles()

        qss = open('media/estilo.qss').read()
        self.setStyleSheet(qss)

    def limpiarControles(self):
        '''
        Limpia los controles de la pantalla de datos anteriores
        '''
        self.txtMensaje.setText('')
        self.txtHora.setText('')
        self.chkLunes.setChecked(False)
        self.chkMartes.setChecked(False)
        self.chkMiercoles.setChecked(False)
        self.chkJueves.setChecked(False)
        self.chkViernes.setChecked(False)
        self.chkSabado.setChecked(False)
        self.chkDomingo.setChecked(False)
        self.alertaActual = None

    def clickAccion(self, accion):
        print( self.alertaActual)
        if accion == 'Add':
            self.limpiarControles()
        elif accion == 'Del':
            if self.alertaActual is not None:
                reply = QtGui.QMessageBox.question(self, 'Seguro',
                    "¿Esta seguro de que quiere eliminar esta alerta?",
                    QtGui.QMessageBox.Yes |
                    QtGui.QMessageBox.No, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                    self.tabla.eliminar(self.alertaActual.id)
                    self.initListaHoras()
        elif accion == 'Save':

            alerta = Alerta()

            if self.alertaActual is not None:
                #como ya existe, ponemos el id
                alerta.id = self.alertaActual.id;

            alerta.hora = self.txtHora.text()
            alerta.mensaje = self.txtMensaje.toPlainText()
            alerta.lunes = self.chkLunes.isChecked()
            alerta.martes = self.chkMartes.isChecked()
            alerta.miercoles = self.chkMiercoles.isChecked()
            alerta.jueves = self.chkJueves.isChecked()
            alerta.viernes = self.chkViernes.isChecked()
            alerta.sabado = self.chkSabado.isChecked()
            alerta.domingo = self.chkDomingo.isChecked()

            self.tabla.agregar(alerta)
            self.initListaHoras()

    def elementoListaSeleccionado(self, item):
        linea = self.lstHoras.currentRow()
        print('indice listview ' + str(linea))
        id = self.lista.__getitem__(linea)

        alerta = self.tabla.getAlertaById(id)
        self.visionarAlerta(alerta)

    def visionarAlerta(self, alerta=None):
        self.limpiarControles()
        self.alertaActual = alerta
        self.txtHora.setText(alerta.hora)
        self.txtMensaje.setText(alerta.mensaje)
        self.chkLunes.setChecked(alerta.lunes)
        self.chkMartes.setChecked(alerta.martes)
        self.chkMiercoles.setChecked(alerta.miercoles)
        self.chkJueves.setChecked(alerta.jueves)
        self.chkViernes.setChecked(alerta.viernes)
        self.chkSabado.setChecked(alerta.sabado)
        self.chkDomingo.setChecked(alerta.domingo)

    def initListaHoras(self):
        self.tabla = tbAlertas()

        self.lstHoras.clear()
        self.lista = []
        tareas = self.tabla.listarHorasAlertas()
        for key, value in tareas.items():
            self.lstHoras.addItem(value[0])
            self.lista.append(key)



    def closeEvent(self, event):
        '''
        Evento de cierre d la ventana
        '''

        if self.canExit:
            event.accept() # let the window close
        else:
            event.ignore()
            self.hide()




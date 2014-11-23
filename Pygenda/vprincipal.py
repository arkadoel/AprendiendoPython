"""
    Ventana principal
"""
from PyQt4 import QtGui, QtCore
from Tablas import tbpersona, tbDepartamentos
from constantes import const
from vDepartamentos import ventanaDepartamentos

class vPrincipal(QtGui.QMainWindow):

    idActual = -1

    def __init__(self, parent=None):
        super(vPrincipal, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('Phone-icon.png'))
        self.setGeometry(100, 100, 780, 500)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("Pygenda " + const.APP_VERSION)

        self.iniciarControles()

        self.ponerEstilos()

        #maquetacion
        hbox = QtGui.QHBoxLayout()

        #barra de titulo
        hbox.addStretch(1)

        #controles centrales
        boxcentral = QtGui.QHBoxLayout()
        boxcentral.addWidget(self.lstPersonas)

        boxPropiedades = QtGui.QVBoxLayout()
        gridProp = QtGui.QGridLayout()
        gridProp.addWidget(self.lblNombre, 0, 0)
        gridProp.addWidget(self.txtNombre, 0, 1, 1, 2)
        gridProp.addWidget(self.lblApellidos, 1, 0)
        gridProp.addWidget(self.txtApellidos, 1, 1, 1, 2)

        gridProp.addWidget(QtGui.QLabel("", self), 2, 0)

        gridProp.addWidget(self.lblFijo, 3, 0)
        gridProp.addWidget(self.lblExtFijo, 3, 1)
        gridProp.addWidget(self.txtFijo, 4, 0)
        gridProp.addWidget(self.txtExtFijo, 4, 1)

        gridProp.addWidget(self.lblMovil, 3, 2)
        gridProp.addWidget(self.lblExtMovil, 3, 3)
        gridProp.addWidget(self.txtMovil, 4, 2)
        gridProp.addWidget(self.txtExtMovil, 4, 3)

        gridProp.addWidget(QtGui.QLabel("", self), 5, 0)
        gridProp.addWidget(self.lblEmail, 6, 0)
        gridProp.addWidget(self.txtEmail, 6, 1, 1, 3)
        gridProp.addWidget(self.lblDepartamento, 7, 0)
        gridProp.addWidget(self.cmbDepartamento, 7, 1, 1, 2)
        gridProp.addWidget(self.btnEditDepart, 7, 3)

        #botones accion
        boxAcciones = QtGui.QHBoxLayout()
        boxAcciones.addStretch(0)
        boxAcciones.addWidget(self.btnNuevo)
        boxAcciones.addWidget(self.btnGuardar)
        boxAcciones.addSpacing(50)
        boxAcciones.addWidget(self.btnEliminar)
        boxAcciones.addStretch(0)

        boxPropiedades.addSpacing(35)
        boxPropiedades.addLayout(gridProp)
        boxPropiedades.addStretch(0)
        boxPropiedades.addLayout(boxAcciones)

        boxcentral.addLayout(boxPropiedades)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(boxcentral)
        self.frame.setLayout(vbox)

        #self.btncerrar.clicked.connect(QCoreApplication.instance().quit)
        self.cargaComboDepartamentos()
        self.setCentralWidget(self.frame)

    def iniciarControles(self):
        self.frame = QtGui.QFrame(parent=self)

        self.tablas = tbpersona()
        self.listaIDS = []

        self.lstPersonas = QtGui.QListWidget(self)
        self.cargarListado()

        self.lstPersonas.setFixedWidth(220)
        self.lstPersonas.itemActivated.connect(self.elementoListaSeleccionado)

        self.lblNombre = QtGui.QLabel("Nombre:", self)
        self.txtNombre = QtGui.QLineEdit(self)
        self.lblApellidos = QtGui.QLabel("Apellidos", self)
        self.txtApellidos = QtGui.QLineEdit(self)

        self.lblFijo = QtGui.QLabel("Tlf Fijo", self)
        self.txtFijo = QtGui.QLineEdit(self)
        self.lblExtFijo = QtGui.QLabel("Ext. Fijo", self)
        self.txtExtFijo = QtGui.QLineEdit(self)

        self.lblMovil = QtGui.QLabel("Tlf Movil", self)
        self.txtMovil = QtGui.QLineEdit(self)
        self.lblExtMovil = QtGui.QLabel("Ext. Movil", self)
        self.txtExtMovil = QtGui.QLineEdit(self)

        self.lblEmail = QtGui.QLabel("Email: ", self)
        self.txtEmail = QtGui.QLineEdit(self)
        self.lblDepartamento = QtGui.QLabel("Departamento: ", self)
        self.cmbDepartamento = QtGui.QComboBox(self)

        self.btnNuevo = QtGui.QPushButton("Nuevo", self)
        self.btnNuevo.clicked.connect(lambda: self.clickAccion('Nuevo'))
        self.btnGuardar = QtGui.QPushButton("Guardar", self)
        self.btnGuardar.clicked.connect(lambda: self.clickAccion('Guardar'))
        self.btnEliminar = QtGui.QPushButton("Eliminar", self)
        self.btnEliminar.clicked.connect(lambda: self.clickAccion('Eliminar'))

        self.btnEditDepart = QtGui.QPushButton("+", self)
        self.btnEditDepart.setFixedWidth(30)
        self.btnEditDepart.clicked.connect(lambda: self.clickAccion('Editar departamentos'))

    def cargarListado(self):
        self.lstPersonas.clear()
        self.listaIDS.clear()

        for key, value in self.tablas.nombresPersonas().items():
            self.lstPersonas.addItem(value)
            self.listaIDS.append(key)

    def cargaComboDepartamentos(self):
        departa = tbDepartamentos()
        self.cmbDepartamento.clear()
        for de in departa.listaDepartamentos():
            self.cmbDepartamento.addItem(de)

    def clickAccion(self, tipo):
        if tipo == 'Nuevo':
            self.limpiarDatos()
            self.idActual = -1
        elif tipo == 'Guardar':
            persona = {'id':-1}

            if self.idActual != -1:
                persona.update({'id':self.idActual})

            persona.update({'Nombre':self.txtNombre.text()})
            persona.update({'Apellidos':self.txtApellidos.text()})
            persona.update({'Fijo':self.txtFijo.text()})
            persona.update({'ExtFijo':self.txtExtFijo.text()})
            persona.update({'Movil':self.txtMovil.text()})
            persona.update({'ExtMovil':self.txtExtMovil.text()})
            persona.update({'Email':self.txtEmail.text()})
            persona.update({'Departamento':self.cmbDepartamento.currentText()})

            self.tablas.guardar(persona)
            self.cargarListado()
        elif tipo == 'Eliminar':
            if self.idActual != -1:
                reply = QtGui.QMessageBox.question(self, 'Seguro',
                    "¿Esta seguro de que quiere eliminar esta ficha?",
                    QtGui.QMessageBox.Yes |
                    QtGui.QMessageBox.No, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                    self.tablas.eliminar(self.idActual)
                    self.cargarListado()
                    self.limpiarDatos()
        elif tipo == 'Editar departamentos':
            v = ventanaDepartamentos(self)
            v.show()

    def limpiarDatos(self):
        self.txtNombre.setText('')
        self.txtApellidos.setText('')
        self.txtFijo.setText('')
        self.txtExtFijo.setText('')
        self.txtMovil.setText('')
        self.txtExtMovil.setText('')
        self.txtEmail.setText('')
        self.cmbDepartamento.setCurrentIndex(-1)

    def elementoListaSeleccionado(self, item):
        #print(item.text())
        #print(self.lstPersonas.currentRow())
        indice = self.lstPersonas.currentRow()
        #pedimos a la DB
        self.verPersona(indice)

    def verPersona(self, id):
        """Pide a la DB una persona y lo muestra """
        print("persona " + str(self.listaIDS[id]))
        persona = self.tablas.personaByID(self.listaIDS[id])

        if persona is not None:
            self.idActual = self.listaIDS[id]
            self.limpiarDatos()
            self.txtNombre.setText(persona['Nombre'])
            self.txtApellidos.setText(persona['Apellidos'])
            self.txtFijo.setText(persona['Fijo'])
            self.txtExtFijo.setText(persona['ExtFijo'])
            self.txtMovil.setText(persona['Movil'])
            self.txtExtMovil.setText(persona['ExtMovil'])
            self.txtEmail.setText(persona['Email'])
            indexcmb = self.cmbDepartamento.findText(persona['Departamento'])
            self.cmbDepartamento.setCurrentIndex(indexcmb)


    def ponerEstilos(self):
        self.frame.setObjectName("myFrame")
        #self.btncerrar.setObjectName("btnCerrar")
        self.lblFijo.setObjectName("lblFijo")
        self.txtFijo.setObjectName("txtFijo")
        self.btnEditDepart.setObjectName("btnEditDepart")

        qss = open('estilo.qss').read()
        self.setStyleSheet(qss)




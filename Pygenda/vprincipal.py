"""
    Ventana principal
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Tablas import tbpersona

class vPrincipal(QMainWindow):

    APP_VERSION = "0.1"

    idActual = -1

    def __init__(self, parent=None):
        super(vPrincipal, self).__init__(parent)
        self.setWindowIcon(QIcon('Phone-icon.png'))
        self.setGeometry(100, 100, 780, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.iniciarControles()

        self.ponerEstilos()

        #maquetacion
        hbox = QHBoxLayout()

        #barra de titulo
        hbox.addWidget(self.lbltitulo)
        hbox.addStretch(1)
        hbox.addWidget(self.btncerrar)

        #controles centrales
        boxcentral = QHBoxLayout()
        boxcentral.addWidget(self.lstPersonas)

        boxPropiedades = QVBoxLayout()
        gridProp = QGridLayout()
        gridProp.addWidget(self.lblNombre, 0, 0)
        gridProp.addWidget(self.txtNombre, 0, 1, 1, 2)
        gridProp.addWidget(self.lblApellidos, 1, 0)
        gridProp.addWidget(self.txtApellidos, 1, 1, 1, 2)

        gridProp.addWidget(QLabel("", self), 2, 0)

        gridProp.addWidget(self.lblFijo, 3, 0)
        gridProp.addWidget(self.lblExtFijo, 3, 1)
        gridProp.addWidget(self.txtFijo, 4, 0)
        gridProp.addWidget(self.txtExtFijo, 4, 1)

        gridProp.addWidget(self.lblMovil, 3, 2)
        gridProp.addWidget(self.lblExtMovil, 3, 3)
        gridProp.addWidget(self.txtMovil, 4, 2)
        gridProp.addWidget(self.txtExtMovil, 4, 3)

        gridProp.addWidget(QLabel("", self), 5, 0)
        gridProp.addWidget(self.lblEmail, 6, 0)
        gridProp.addWidget(self.txtEmail, 6, 1, 1, 3)
        gridProp.addWidget(self.lblDepartamento, 7, 0)
        gridProp.addWidget(self.txtDepartamento, 7, 1, 1, 2)

        #botones accion
        boxAcciones = QHBoxLayout()
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

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(boxcentral)
        self.frame.setLayout(vbox)

        self.btncerrar.clicked.connect(QCoreApplication.instance().quit)

        self.setCentralWidget(self.frame)

    def iniciarControles(self):
        self.frame = QFrame(parent=self)

        self.btncerrar = QPushButton('X', self)
        self.btncerrar.setFixedWidth(30)

        self.lbltitulo = QLabel("Pygenda " + self.APP_VERSION, self)

        self.tablas = tbpersona()
        self.listaIDS = []

        self.lstPersonas = QListWidget(self)
        self.cargarListado()

        self.lstPersonas.setFixedWidth(220)
        self.lstPersonas.itemActivated.connect(self.elementoListaSeleccionado)

        self.lblNombre = QLabel("Nombre:", self)
        self.txtNombre = QLineEdit(self)
        self.lblApellidos = QLabel("Apellidos", self)
        self.txtApellidos = QLineEdit(self)

        self.lblFijo = QLabel("Tlf Fijo", self)
        self.txtFijo = QLineEdit(self)
        self.lblExtFijo = QLabel("Ext. Fijo", self)
        self.txtExtFijo = QLineEdit(self)

        self.lblMovil = QLabel("Tlf Movil", self)
        self.txtMovil = QLineEdit(self)
        self.lblExtMovil = QLabel("Ext. Movil", self)
        self.txtExtMovil = QLineEdit(self)

        self.lblEmail = QLabel("Email: ", self)
        self.txtEmail = QLineEdit(self)
        self.lblDepartamento = QLabel("Departamento: ", self)
        self.txtDepartamento = QLineEdit(self)

        self.btnNuevo = QPushButton("Nuevo", self)
        self.btnNuevo.clicked.connect(lambda: self.clickAccion('Nuevo'))
        self.btnGuardar = QPushButton("Guardar", self)
        self.btnGuardar.clicked.connect(lambda: self.clickAccion('Guardar'))
        self.btnEliminar = QPushButton("Eliminar", self)
        self.btnEliminar.clicked.connect(lambda: self.clickAccion('Eliminar'))

    def cargarListado(self):
        self.lstPersonas.clear()

        for key, value in self.tablas.nombresPersonas().items():
            self.lstPersonas.addItem(value)
            self.listaIDS.append(key)

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
            persona.update({'Departamento':self.txtDepartamento.text()})

            self.tablas.guardar(persona)
            self.cargarListado()
        elif tipo == 'Eliminar':
            if self.idActual != -1:
                reply = QMessageBox.question(self, 'Seguro',
                    "¿Esta seguro de que quiere eliminar esta ficha?",
                    QMessageBox.Yes |
                    QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    self.tablas.eliminar(self.idActual)
                    self.cargarListado()
                    self.limpiarDatos()



    def limpiarDatos(self):
        self.txtNombre.setText('')
        self.txtApellidos.setText('')
        self.txtFijo.setText('')
        self.txtExtFijo.setText('')
        self.txtMovil.setText('')
        self.txtExtMovil.setText('')
        self.txtEmail.setText('')
        self.txtDepartamento.setText('')

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
            self.txtDepartamento.setText(persona['Departamento'])


    def ponerEstilos(self):
        self.frame.setObjectName("myFrame")
        self.btncerrar.setObjectName("btnCerrar")
        self.lblFijo.setObjectName("lblFijo")
        self.txtFijo.setObjectName("txtFijo")

        qss = open('estilo.qss').read()
        self.setStyleSheet(qss)




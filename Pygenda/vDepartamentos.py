
from PyQt4 import QtGui, QtCore
from Tablas import tbDepartamentos


class ventanaDepartamentos(QtGui.QMainWindow):

    def __init__(self, parent):
        super(ventanaDepartamentos, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Edicion de departamentos")
        self.setGeometry(100, 100, 300, 300)
        self.setFixedSize(300, 300)

        self.listaDepartamentos =[]
        self.tablaDep = tbDepartamentos()

        self.initControles()
        self.initMaquetacion()

    def initControles(self):
        self.lstDepartamentos = QtGui.QListWidget(self)

        self.btnAdd = QtGui.QPushButton("+", self)
        self.btnAdd.setFixedWidth(30)
        self.btnAdd.clicked.connect(lambda: self.clickAccion('Add'))

        self.btnDelete = QtGui.QPushButton("-", self)
        self.btnDelete.setFixedWidth(30)
        self.btnDelete.clicked.connect(lambda: self.clickAccion('Del'))

        self.txtDepartamento = QtGui.QLineEdit(self)
        self.lblDep = QtGui.QLabel("Lista de departamentos")

        self.cargaDepartamentos()

    def initMaquetacion(self):
        self.frame = QtGui.QFrame(parent=self)
        self.frame.setObjectName("myFrame")
        grid = QtGui.QGridLayout()

        grid.addWidget(self.lblDep, 0, 0, 1, 3)
        grid.addWidget(self.lstDepartamentos, 1, 0, 5, 3)
        grid.addWidget(self.txtDepartamento, 6, 0)
        grid.addWidget(self.btnAdd, 6, 1)
        grid.addWidget(self.btnDelete, 6, 2)

        self.frame.setLayout(grid)
        self.setCentralWidget(self.frame)

    def cargaDepartamentos(self):

        self.lstDepartamentos.clear()
        self.listaDepartamentos.clear()

        for de in self.tablaDep.listaDepartamentos():
            self.lstDepartamentos.addItem(de)
            self.listaDepartamentos.append(de)

    def clickAccion(self, tipo):
        if tipo == 'Add':
            departamento = self.txtDepartamento.text()
            if departamento not in self.listaDepartamentos:
                #agregar a la DB
                self.tablaDep.guardar(departamento)
                self.cargaDepartamentos()
                self.txtDepartamento.setText('')
                self.parent.cargarListado()
                self.recargarPadre()

        elif tipo == 'Del':
            departamento = self.lstDepartamentos.currentItem().text()
            print('Eliminar: ' + departamento)
            #borrar de la dB
            self.tablaDep.eliminar(departamento)
            self.cargaDepartamentos()
            self.recargarPadre()

    def recargarPadre(self):
        self.parent.cargaComboDepartamentos()
        self.parent.cargarListado()
        self.parent.limpiarDatos()


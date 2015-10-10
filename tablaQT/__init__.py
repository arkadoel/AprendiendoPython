""" Codigo con el que se busca probar las tablas en
    QT4
"""
from PyQt4 import QtGui
import sys
import Datos
from Datos import Persona

class Ventana(QtGui.QWidget):

    def __init__(self):
        super(Ventana, self).__init__()
        self.resize(750, 450)
        self.move(200, 200)
        self.setWindowTitle('Prueba de tabla')
        self.datos = Datos.Modelo()

        self.init_gui()


    def init_gui(self):
        vbox = QtGui.QVBoxLayout()

        num_col = len(self.datos.columnas) + 2
        num_rows = len(self.datos.lista_personas)

        self.tabla = QtGui.QTableWidget(self)
        self.tabla.setColumnCount(num_col)
        self.tabla.setRowCount(num_rows)

        ''' por si se pone tonto a la hora de agregar

        if self.tabla.rowCount() < num_rows:
            for i in range(num_rows):
                self.tabla.insertRow(i)
        '''

        self.tabla.setHorizontalHeaderLabels(self.datos.columnas)
        self.tabla.setSortingEnabled(True)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        #self.tabla.resizeColumnsToContents()
        #self.tabla.resizeRowsToContents()



        i = 0
        j = 0

        for persona in self.datos.lista_personas:

            self.tabla.setItem(i, 0, QtGui.QTableWidgetItem(persona.nombre))
            self.tabla.setItem(i, 1, QtGui.QTableWidgetItem(persona.apellidos))
            self.tabla.setItem(i, 2, QtGui.QTableWidgetItem('%s' % persona.edad))

            combobox = QtGui.QComboBox()
            combobox.addItem('Varon')
            combobox.addItem('Mujer')
            self.tabla.setCellWidget(i, 3, combobox)

            dia = QtGui.QDateEdit()
            dia.setCalendarPopup(True)
            self.tabla.setCellWidget(i, 4, dia)

            i += 1

        vbox.addWidget(self.tabla)

        #resto de controles
        self.boton = QtGui.QPushButton('Ver', self)
        self.boton.clicked.connect(lambda: self.clickAction(accion='Ver'))
        vbox.addWidget(self.boton)

        self.btnGuardar = QtGui.QPushButton('Guardar', self)
        self.btnGuardar.clicked.connect(lambda: self.clickAction(accion='Guardar'))


        grid = QtGui.QGridLayout()

        self.txtNombre = QtGui.QLineEdit(self)
        self.txtApe = QtGui.QLineEdit(self)
        grid.addWidget(self.txtNombre, 0, 0)
        grid.addWidget(self.txtApe, 1, 0)

        vbox.addLayout(grid)
        vbox.addWidget(self.btnGuardar)
        self.setLayout(vbox)

    def ver_calendario(self, sender=None):
        assert isinstance(sender, QtGui.QDateEdit)
        sender.showNormal()

    def clickAction(self, accion=''):

        if accion != '':
            if 'Ver' in accion:
                ''' Vamos a ver las filas seleccionadas
                '''
                fila = self.tabla.currentItem().row()

                if fila is not None:
                    self.txtNombre.setText( self.tabla.item(fila, 0).text())
                    self.txtApe.setText(self.tabla.item(fila, 1).text())
                else:
                    print('No seleccionado')

            elif 'Guardar' in accion:
                pass



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())


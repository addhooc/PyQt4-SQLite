from ingresarCliente import *
import sys
import os
import sqlite3
from PyQt4 import QtCore, QtGui


class Clientes(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # Ui_MainWindow --> Main Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Seteo de cuotas al iniciar el programa
        # self.ui.lineCuotaP.setText('2')
        # self.ui.linePorcP.setFocus()


        # Tab order
        # self.setTabOrder(self.ui.lineCuotaP, self.ui.linePorcP)
        
        # Click Events
        self.click_metodo(self.ui.btn_Ingresar, self.ingresar_cliente)


    # Metodoss

    def click_metodo(self, boton, metodo):
        '''Recibe un botón y el método que se
        ejecuta al clicar dicho botón.
        Retorna el retorno del método solicitado'''
        self.boton = boton
        self.metodo = metodo
        return QtCore.QObject.connect(self.boton,QtCore.SIGNAL('clicked()'), self.metodo)

            
    def ingresar_cliente(self):

        id = self.ui.lineID.text()
        carp = self.ui.lineCarpeta.text()
        ap = self.ui.lineApellido.text()
        nom = self.ui.lineNombre.text()
        doc = self.ui.lineDocumento.text()
        tel = self.ui.lineTelefono.text()
        em = self.ui.lineEmail.text()

        query = ("INSERT INTO Clientes (ID, Carpeta, Apellido, Nombre, Documento, Telefono, Email) VALUES('%s','%s','%s','%s','%s', '%s', '%s')" % (id, carp, ap, nom, doc, tel, em))

        # Iniciamos una conexion con la BBDD
        self.conn = sqlite3.connect('C:/Users/Tincho/Desktop/Git/PyQt_Sqlite/Insert/clientes.sqlite')

        # Definimos un cursor
        self.c = self.conn.cursor()

        # Ejecutamos el query
        self.c.execute(query)

        # Seteamos los campos luego de ingresados los datos
        self.ui.lineID.setText('')
        self.ui.lineCarpeta.setText('')
        self.ui.lineApellido.setText('')
        self.ui.lineNombre.setText('')
        self.ui.lineDocumento.setText('')
        self.ui.lineTelefono.setText('')
        self.ui.lineEmail.setText('')

        mensaje = 'Cliente ' + ap + ', ' + nom + ' ingresado con éxito.'

        # Comunicamos el ingreso de los datos
        self.ui.plainTextEdit.appendPlainText(mensaje)

        
        # Ubicamos el cursor grafico sobre primer Line Edit
        self.ui.lineID.setFocus()

        # Cerramos el cursor, hacemos un commit y cerramos la conexion a la BBDD
        self.c.close()
        self.conn.commit()
        self.conn.close()

    def mis_clientes(self):
        p = Sql()
        clientes = p.query("SELECT ID_Rector, Carpeta, NomCliente FROM Clientes ORDER BY 3")

        self.columnas = 'ID Rector\tNro.Carpeta\t\tNombre\n'
        self.ui.plainCuotas.appendPlainText(self.columnas)

        for c in clientes:
            caja = c[0] + '\t' + c[1] + '\t\t' + c[2] + '\n'
            self.ui.plainCuotas.appendPlainText(caja)

        p.close_cursor()
        p.close_conn()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Clientes()
    myapp.show()
    sys.exit(app.exec_())

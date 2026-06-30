import web
import sqlite3

render = web.template.render('views')

class ListaContactos:
    def conectar(self):
        try:
            conexion = sqlite3.connect("sql/agenda.sqlite")
            conexion.row_factory = sqlite3.Row
            return conexion
        except Exception as error:
            print(f"Error 100: {error.args}")
            return None

    def listaContactos(self):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            sql = "SELECT * FROM contactos"
            cursor.execute(sql)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado: 
                contacto= {
                    "id_contacto": fila[0],
                    "nombre": fila[1],
                    "primer_apellido": [2],
                    "segundo_apellido": [3],
                    "email":fila[4],
                    "telefono": fila[5]
                }
                datos.append(contacto)
            conexion.close()
            print(datos)
            return datos
        
        except Exception as error:
            print(f"Error 101: {error.args}")
            return None

    def GET(self):
        contactos = self.listaContactos()
        return render.lista_contactos(contactos)
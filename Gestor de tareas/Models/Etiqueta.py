import mysql.connector

class ModeloEtiqueta:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestor_tareas"
        )
        self.cursor = self.conn.cursor()

    def crear_etiqueta(self, nombre):
            consulta = "INSERT INTO etiquetas (nombre) VALUES (%s)"
            self.cursor.execute(consulta, (nombre,))
            self.conn.commit()

    def ver_etiquetas(self):
        self.cursor.execute(
            "SELECT * FROM etiquetas"
        )
        return self.cursor.fetchall()

    def actualizar_etiqueta(self, id_etiqueta, nombre):
        consulta = "UPDATE etiquetas SET nombre = %s WHERE id = %s"
        self.cursor.execute(consulta, (nombre, id_etiqueta))
        self.conn.commit()

    def eliminar_etiqueta(self, id_etiqueta):
        consulta = "DELETE FROM etiquetas WHERE id = %s"
        self.cursor.execute(consulta, (id_etiqueta,))
        self.conn.commit()

    
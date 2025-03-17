import mysql.connector

class ModeloTarea:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestor_tareas"
        )
        self.cursor = self.conn.cursor()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(255) NOT NULL,
                descripcion TEXT,
                estado ENUM('pendiente', 'completada') DEFAULT 'pendiente'
            )
        """)
        self.conn.commit()

    def agregar_tarea(self, titulo, descripcion):
        consulta = "INSERT INTO tareas (titulo, descripcion) VALUES (%s, %s)"
        self.cursor.execute(consulta, (titulo, descripcion))
        self.conn.commit()

    def obtener_tareas_etiquetas(self):
        self.cursor.execute("""SELECT t.id, t.titulo, t.descripcion, t.estado, GROUP_CONCAT(e.nombre SEPARATOR ', ') AS etiqueta
            FROM tareas AS t
            JOIN tareas_etiquetas AS te ON t.id = te.id_tarea
            JOIN etiquetas AS e ON te.id_etiqueta = e.id
            GROUP BY t.id
            """)
        return self.cursor.fetchall()

    def obtener_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        return self.cursor.fetchall()

    def actualizar_tarea(self, id_tarea, estado):
        consulta = "UPDATE tareas SET estado = %s WHERE id = %s"
        self.cursor.execute(consulta, (estado, id_tarea))
        self.conn.commit()

    def eliminar_tarea(self, id_tarea):
        consulta_relaciones = "DELETE FROM tareas_etiquetas WHERE id_tarea = %s"
        self.cursor.execute(consulta_relaciones, (id_tarea,))
        consulta = "DELETE FROM tareas WHERE id = %s"
        self.cursor.execute (consulta, (id_tarea,))
        self.conn.commit()

    def agregar_etiqueta(self, id_tarea, id_etiqueta):
        consulta = "INSERT INTO tareas_etiquetas (id_tarea, id_etiqueta) VALUES (%s, %s)"
        self.cursor.execute(consulta, (id_tarea, id_etiqueta))
        self.conn.commit()

    def ver_etiquetas(self):
        self.cursor.execute("SELECT * FROM etiquetas")
        return self.cursor.fetchall()

    def ultimo_id(self):
        consulta = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(consulta)
        return self.cursor.fetchone()[0]

    
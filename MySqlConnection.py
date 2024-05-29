import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'usuariosED'
        self.user = 'root'
        self.password = 'noch392lq17?'

    def save_to_database(self, username, password):
        try:
            # Establecer la conexión
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )

            if connection.is_connected():
                # Crear un cursor para realizar operaciones en la base de datos
                cursor = connection.cursor()

                # Ejecutar la inserción en la tabla usuarios
                query = "INSERT INTO usuarios (usuario, password) VALUES (%s, %s)"
                data = (username, password)
                cursor.execute(query, data)

                # Confirmar la transacción
                connection.commit()

                print("Usuario guardado en la base de datos")

        except Error as e:
            print("Error al guardar usuario en la base de datos:", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("La conexión a la base de datos se ha cerrado")

    def retrieve_from_database(self, encrypted_username):
        try:
            # Establecer la conexión
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )

            if connection.is_connected():
                # Crear un cursor para realizar operaciones en la base de datos
                cursor = connection.cursor()

                # Ejecutar la consulta para obtener el usuario y contraseña asociados al username encriptado
                query = "SELECT usuario, password FROM usuarios WHERE usuario = %s"
                cursor.execute(query, (encrypted_username,))
                record = cursor.fetchone()

                if record:
                    return record[0], record[1]  # Retorna usuario y contraseña

        except Error as e:
            print("Error al recuperar datos de la base de datos:", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("La conexión a la base de datos se ha cerrado")

        return None, None

if __name__ == "__main__":

    db_manager = DatabaseManager()

    # Prueba de guardado en la base de datos
    db_manager.save_to_database("usuario_prueba", "password_prueba")

    # Prueba de recuperación de la base de datos
    stored_username, stored_password = db_manager.retrieve_from_database("usuario_prueba")
    print("Usuario recuperado:", stored_username)
    print("Contraseña recuperada:", stored_password)

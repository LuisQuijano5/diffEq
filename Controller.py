

import sys
from PySide6 import QtWidgets
from AppView import SignUpLoginView
from Chen import chen
from Lorenz import lorenz
from Username import encrypt, decrypt
from Encrypting import  generate_password_hash
from Encrypting import encrypt as encrypt_pass
from MySqlConnection import DatabaseManager


class SignUpLoginController:
    def __init__(self, app):
        self.app = app
        self.ventana = SignUpLoginView()
        self.ventana.show()

        # Instanciamos el gestor de base de datos
        self.db_manager = DatabaseManager()

        # Conectar eventos de la interfaz gráfica a la lógica
        self.ventana.submit_button.clicked.connect(self.signup)
        self.ventana.login_button.clicked.connect(self.login)

    def signup(self):
        username = self.ventana.username_signup.text()
        initial_conditions = [
            float(self.ventana.initial_condition1.text()),  # Convertir el texto a float
            float(self.ventana.initial_condition2.text()),  # Convertir el texto a float
            float(self.ventana.initial_condition3.text())  # Convertir el texto a float
        ]

        T = 50
        dt = 0.01

        # Encriptar el nombre de usuario
        encrypted_username = encrypt(username, initial_conditions, T, dt, lorenz)

        # Generar una contraseña en texto claro y cifrarla
        encrypted_password, password = generate_password_hash()

        # Guardar en la base de datos
        self.db_manager.save_to_database(username, encrypted_password)

        # Seguimiento en consola
        print(f"Encrypted Username: {encrypted_username}")
        print(f"Password: {password}")

    def login(self):
        encrypted_username = self.ventana.username_login.text()
        password = self.ventana.password_login.text()
        initial_conditions = [
            float(self.ventana.initial_condition1_login.text()),  # Convertir el texto a float
            float(self.ventana.initial_condition2_login.text()),  # Convertir el texto a float
            float(self.ventana.initial_condition3_login.text())  # Convertir el texto a float
        ]

        T = 50
        dt = 0.01

        # Desencriptar el nombre de usuario almacenado
        decrypted_username = decrypt(encrypted_username, initial_conditions, T, dt, lorenz)

        # Encriptar la contraseña proporcionada por el usuario
        encrypted_input_password = encrypt_pass(password)

        # Recuperar datos de la base de datos
        stored_username, stored_password = self.db_manager.retrieve_from_database(decrypted_username)

        if stored_username is None or stored_password is None:
            print("Login Failed: User not found")
            return

        # Comparar los datos ingresados con los almacenados
        if str(encrypted_input_password) == stored_password:
            if decrypted_username == stored_username:
                print("Login Successful")
            else:
                print("Login Failed: Username does not match")
        else:
            print("Login Failed: Password does not match")


    def run(self):
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = SignUpLoginController(app)
    controller.run()

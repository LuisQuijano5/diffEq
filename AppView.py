# SignUpLoginView.py
import os
import sys

from PySide6 import QtWidgets, QtGui, QtCore

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
stylesheet_path = os.path.join(current_dir, 'styleSheet.css')

class SignUpLoginView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Sign Up and Log In")
        self.setGeometry(100, 100, 800, 600)

        # Cargar los estilos CSS
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, 'styleSheet.css')
        with open(stylesheet_path, 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        # Layout principal
        layout = QtWidgets.QVBoxLayout()

        # Sección de Sign Up
        self.signup_group = QtWidgets.QGroupBox("Sign Up")
        self.signup_layout = QtWidgets.QFormLayout()

        self.username_signup = QtWidgets.QLineEdit()
        self.initial_condition1 = QtWidgets.QLineEdit()
        double_validator = QtGui.QDoubleValidator()
        self.initial_condition1.setValidator(double_validator)
        self.initial_condition2 = QtWidgets.QLineEdit()
        self.initial_condition2.setValidator(double_validator)
        self.initial_condition3 = QtWidgets.QLineEdit()
        self.initial_condition3.setValidator(double_validator)

        self.signup_layout.addRow("Username:", self.username_signup)
        self.signup_layout.addRow("Initial Condition 1:", self.initial_condition1)
        self.signup_layout.addRow("Initial Condition 2:", self.initial_condition2)
        self.signup_layout.addRow("Initial Condition 3:", self.initial_condition3)

        self.submit_button = QtWidgets.QPushButton("Submit")
        self.signup_layout.addRow(self.submit_button)

        self.signup_group.setLayout(self.signup_layout)
        layout.addWidget(self.signup_group)

        # Sección de Log In
        self.login_group = QtWidgets.QGroupBox("Log In")
        self.login_layout = QtWidgets.QFormLayout()

        self.username_login = QtWidgets.QLineEdit()
        self.initial_condition1_login = QtWidgets.QLineEdit()
        self.initial_condition1_login.setValidator(double_validator)
        self.initial_condition2_login = QtWidgets.QLineEdit()
        self.initial_condition2_login.setValidator(double_validator)
        self.initial_condition3_login = QtWidgets.QLineEdit()
        self.initial_condition3_login.setValidator(double_validator)
        self.password_login = QtWidgets.QLineEdit()

        self.login_layout.addRow("Username:", self.username_login)
        self.login_layout.addRow("Password:", self.password_login)
        self.login_layout.addRow("Initial Condition 1:", self.initial_condition1_login)
        self.login_layout.addRow("Initial Condition 2:", self.initial_condition2_login)
        self.login_layout.addRow("Initial Condition 3:", self.initial_condition3_login)


        self.login_button = QtWidgets.QPushButton("Log In")
        self.login_layout.addRow(self.login_button)

        self.login_group.setLayout(self.login_layout)
        layout.addWidget(self.login_group)

        # Widget central
        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("Biseccion")
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = SignUpLoginView()
    ventana.show()
    sys.exit(app.exec())

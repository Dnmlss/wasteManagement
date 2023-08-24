# Importamos la libreria 
from flask_sqlalchemy import SQLAlchemy

# Inicializamos la extension SQLAlchemy
db = SQLAlchemy()

# Definimos una clase que representa una tabla en la base de datos
class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    cedula = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String, nullable=False)
    contraseña = db.Column(db.String, nullable=False)

    # Funcion constructora de la base de datos
    def __init__(self, nombre, apellido, cedula, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.contraseña = contraseña

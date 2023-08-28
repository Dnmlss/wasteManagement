# Importamos la libreria 
from flask_sqlalchemy import SQLAlchemy

# Inicializamos la extension SQLAlchemy
db = SQLAlchemy()

# Definimos una clase que representa una tabla en la base de datos
class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    cedula = db.Column(db.Integer, nullable=False, unique=True) # Hacemos que la cedula sea unica
    # puntos = db.Column(db.Integer, nullable=False)

    # Funcion constructora de la base de datos
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        # self.puntos = puntos
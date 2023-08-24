from flask import render_template, request, redirect, url_for
from connection import app, db
from models import Registro


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        cedula = request.form["cedula"]
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]

        datos_usuarios = Registro(nombre, apellido, cedula, correo, contraseña)

        db.session.add(datos_usuarios)
        db.session.commit()

        return render_template("login.html")
    
    return render_template("login.html")


@app.route("/opciones")
def opciones():
    return render_template("opciones.html")

# CRUD CREATE - READ - UPDATE - DELETE

@app.route("/vidrio")
def vidrio():
    return render_template("vidrio.html")

@app.route("/papel")
def papel():
    return render_template("papel.html")

@app.route("/plastico")
def plastico():
    return render_template("plastico.html")

@app.route("/baterias")
def baterias():
    return render_template("baterias.html")
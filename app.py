from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html")

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
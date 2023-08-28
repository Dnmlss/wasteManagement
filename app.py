from flask import render_template, request, redirect, url_for, Response
from connection import app, db
from models import Registro
from PIL import Image
from io import BytesIO
import qrcode


#CRUD - CREAT / CARGAR - READ / MOSTRAR - UPDATE / ACTUALIZAR - DELETE / ELIMINAR

# Crear
@app.route("/ingresar", methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]

        datos_usuarios = Registro(nombre, cedula)

        db.session.add(datos_usuarios)
        db.session.commit()

        return render_template("ingresar.html")
    
    return render_template("ingresar.html")



# Mostrar datos
@app.route("/mostrar_datos", methods = ["GET", "POST"])
def mostrar_datos():

        #Creamos el nuevo objeto que contiene la lista total de nuestra base de datos
        lista_ci_puntos = Registro.query.all()

        return render_template("mostrar_datos.html", lista_ci_puntos=lista_ci_puntos)



# Actualizar
@app.route("/actualizar/<int:usuario_id>", methods = ["GET", "POST"])
def actualizar(usuario_id):

    usuario_actualizado = Registro.query.get(usuario_id) # Creamos un nuevo objeto donde obtenemos los datos de un usuario en especifico

    if request.method == "POST": # Obtenemos los datos del formulario (nombre,cedula,puntos)
        nombre = request.form['nombre']
        cedula = request.form['cedula']

        # Actualizamos los datos obtenidos del formulario instanciado del nuevo objeto
        usuario_actualizado.nombre = nombre
        usuario_actualizado.cedula = cedula

        db.session.commit() # Conmmiteamos la actualizacion de los datos

        return redirect(url_for("mostrar_datos")) # Redireccionamos a la pagina una vez actualizado los datos
    
    return render_template('actualizar.html', usuario_actualizado=usuario_actualizado)



# Eliminar
@app.route("/eliminar", methods = ["GET", "POST"])
def eliminar():
    if request.method == "POST":

        id = request.form['usuario_id'] #Guardamos en la variable id los datos obtenidos del formulario
        usuario_a_eliminar = Registro.query.filter_by(id=id).first() #Realizamos la consulta a nuestra base de datos para obtener los datos del usuario en referencia y creamos un nuevo objeto guardando en la variable

        db.session.delete(usuario_a_eliminar) # Eliminamos los datos del usuario
        db.session.commit() # Commiteamos la eliminacion

        return redirect(url_for("mostrar_datos")) # Redireccionamos a la pagina para mostrar los datos de la base de datos


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

def qr_generator(url):
    # Crea un objeto QRCode con las configuraciones deseadas
    qr = qrcode.QRCode(
        version=7,  # Versión del QR (1-40). Aumentar para admitir más datos.
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel de corrección de errores (L, M, Q, H).
        box_size=10,  # Tamaño de cada caja en el QR.
        border=1,  # Tamaño del borde.
    )
    # Generamos la ruta a la que nuestro código QR va a redireccionar
    qr.add_data(url)

    # Genera el código QR con el ajuste fit=True para que se adapte automáticamente al tamaño de los datos
    qr.make(fit=True)

    # Pasamos los parámetros de color que tendrá nuestro QR
    qrcolor = 'Black'

    # Crea una imagen PIL (Pillow) del código QR con los colores especificados
    qrimg = qr.make_image(fill_color=qrcolor, back_color="green").convert('RGB')

    # Guarda el código QR generado en un objeto BytesIO para su posterior uso
    img_buffer = BytesIO()
    qrimg.save(img_buffer, format="PNG")

    # Devolvemos los bytes de la imagen como respuesta
    return img_buffer.getvalue()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_qr')
def generar_qr():
    # Define la IP y la URL que deseas codificar en el código QR
    ip = '192.168.1.174'
    url = 'www.youtube.com/'  # Corregimos la URL
    # Llama a la función qr_generator para generar el código QR con la URL proporcionada
    qr_image = qr_generator(url)
    # Devuelve la imagen del código QR como una respuesta HTTP con el tipo de contenido 'image/png'
    return Response(qr_image, content_type="image/png")

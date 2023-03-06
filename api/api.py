from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session
import secrets
from controlador.roles import CL_Roles
from controlador.fuentes_noticias import CL_FuentesNoticias
from controlador.usuarios import CL_Usuario
import json
app = Flask(__name__)
app.secret_key = '7ca057fab5edfb90831da61d0c3cc5bd'

# Errors handler
@app.errorhandler(401)
def page_not_authorization(e):
    # note that we set the 401 status explicitly
    return render_template('Errors/401.html'), 401

#Al correr kafka inicia por esta función esperando una ruta para iniciar el sistema
@app.route("/")
def root():
    return ('Fuentes de noticias')

###########################################################################################################################################
#USUARIOS

#Función que utiliza el post para el registro de un usuario en la base de datos
@app.route("/usuario/", methods=['POST'])
def usuario():
    return CL_Usuario().FN_Usuario()

###########################################################################################################################################
#ROLES

#Función para obtener todos los roles de usuario
@app.route("/roles/", methods=['GET'])
def roles():
    json_data = json.dumps(CL_Roles().FN_ObtenerRoles())
    return json_data

###########################################################################################################################################

@app.route("/xml/", methods=['GET'])
def xml():
    return CL_FuentesNoticias().xml()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
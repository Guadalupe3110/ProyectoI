from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session, jsonify
from flask_jwt import JWT, jwt_required, current_identity
import secrets
from datetime import timedelta
from controlador.roles import CL_Roles
from controlador.fuentes_noticias import CL_FuentesNoticias
from controlador.usuarios import CL_Usuario
from modelo.db_usuarios import CL_UsuarioDB
from controlador.categorias import CL_Categorias
import json
import datetime
from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.secret_key = '7ca057fab5edfb90831da61d0c3cc5bd'
app.config['JWT_SECRET_KEY'] = '123456' # Agregas la clave secreta
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)
jwt = JWTManager(app)
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
    print(session['user'])
    return CL_Usuario().FN_Usuario()

#Acá al poner url, dirige al login
@app.route("/session/drop")
def session_drop():
    session.pop('user', None)
    return redirect(url_for('login'))

#Función que verifica el correo y contraseña al loguearse en la base de datos
@app.route('/login/', methods=['POST'])
def login():
    if request.method == 'POST':
            contenido = request.get_json(force = True)
            session.pop('user', None)
            validar_sesion = CL_UsuarioDB().FN_Login(contenido['email'], contenido['password'])
            if validar_sesion != False:
                access_token = create_access_token(identity=validar_sesion['idUsers'], expires_delta=timedelta(days=1))
                validar_sesion['token'] = access_token
                session['user']  = validar_sesion
                CL_Usuario().FN_ModificarToken(validar_sesion)
                return jsonify({'access_token': access_token, 'user_id': validar_sesion['idUsers']})
    if 'user' in session:
        return "200 OK: Inicio de sesión correctamente"
    return "error"

# Función protegida por JWT que solo es accesible si se proporciona un token de acceso válido
@app.route('/protected/', methods=['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    print(jsonify(logged_in_as=user_id))
    return jsonify(logged_in_as=user_id), 200

###########################################################################################################################################
#ROLES

#Función para obtener todos los roles de usuario
@app.route("/roles/", methods=['GET'])
def roles():
    json_data = json.dumps(CL_Roles().FN_ObtenerRoles())
    return json_data

###########################################################################################################################################
#CATEGORIAS
#Función que utiliza el get para el obtener todas las categorias 
@app.route("/categorias/", methods=['GET'])
def categorias():
    return CL_Categorias().FN_ObtenerCategorias()

#Función que utiliza el post para el registro de una categoria en la base de datos
@app.route("/categoria/", methods=['POST'])
def categoria():
    return CL_Categorias().FN_InsertarCategoria()

#Función que utiliza el delete para el eliminar una categoria en la base de datos
@app.route("/categoria/<id>/", methods=['GET','PATCH'])
def categoria_modificar(id):
    return CL_Categorias().FN_ModificarCategoria(id)

#Función que utiliza el get para saber si una categoria esta relacionadad a una fuente de noticia o noticia en la base de datos
@app.route("/verificarcategoria/<id>/", methods=['GET'])
def verficar_categoria_eliminar(id):
    return CL_Categorias().FN_VerificarEliminar(id)

#Función que utiliza el delete para el eliminar una categoria en la base de datos
@app.route("/categoria/<id>/", methods=['DELETE'])
def categoria_eliminar(id):
    return CL_Categorias().FN_EliminarCategoria(id)

###########################################################################################################################################




@app.route("/xml/", methods=['GET'])
def xml():
    return CL_FuentesNoticias().xml()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
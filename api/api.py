from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session
import secrets
from controlador.roles import CL_Roles


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

#Prueba de conexion
@app.route("/prueba/", methods=['GET'])
def prueba():
    print(CL_Roles().prueba())
    return CL_Roles().prueba()

#Prueba de conexion
@app.route("/noticias/", methods=['GET'])
def prueba2():
    print(CL_Roles().prueba2())
    return CL_Roles().prueba2()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
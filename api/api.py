from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session
import secrets

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
from flask import Flask, redirect, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos (reemplaza 'sqlite:///site.db' con la URI de tu base de datos)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Definición del modelo de la base de datos (por ejemplo, una tabla de usuarios)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define aquí los campos que necesites para tu aplicación

# Ruta principal que muestra el enlace de afiliado de Amazon y maneja la cookie
@app.route('/')
def index():
    # Obtener el valor de la cookie (si existe)
    affiliate_cookie = request.cookies.get('affiliate')
    
    # Lógica para manipular la cookie (por ejemplo, guardar el valor en la base de datos)
    # Si el usuario no tiene la cookie configurada, puedes hacer alguna acción (por ejemplo, registrar en la base de datos)

    # Redirigir a tu enlace de afiliado de Amazon
    response = make_response(redirect("https://www.amazon.es/?&linkCode=ll2&tag=lucky0d40-21&linkId=41ac6f9699889794e5cf61725cd669a9&language=es_ES&ref_=as_li_ss_tl"))

    # Establecer la cookie con el valor de afiliado (puedes personalizar esto según tus necesidades)
    response.set_cookie('affiliate', 'lucky0d40-21')

    return response

if __name__ == '__main__':
    # Crear las tablas en la base de datos antes de ejecutar la aplicación
    with app.app_context():
        db.create_all()
    # Ejecutar la aplicación en el puerto 5000 en modo debug
    app.run(debug=True, port=8000)


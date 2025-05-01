# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime

# Inicializar la app Flask
app = Flask(__name__)

# 🔐 Clave secreta para sesiones
app.config['SECRET_KEY'] = 'clave-super-secreta-123456'

# 📦 Configuración de PostgreSQL — CAMBIA esto por los datos de tu Render DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:clave@host:5432/nombre_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos y login
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# 📌 Importar modelos (importan solo, no hacen nada más aquí)
from models.cliente import Cliente
from models.credito import Credito
from models.usuario import Usuario
from models.inventario import ItemInventario

# 📌 Cargar rutas (cuando las tengamos definidas)
from routes import auth
# app.register_blueprint(auth_bp)

# 🔧 Crear las tablas automáticamente si no existen
@app.before_first_request
def crear_tablas():
    db.create_all()

# Ruta de prueba para ver que la app funciona
@app.route('/')
def home():
    return "<h2>Bienvenido a la nueva versión de tu sistema de crédito ✨</h2>"

# Solo si ejecutas localmente (Render usa gunicorn)
if __name__ == '__main__':
    app.run(debug=True)

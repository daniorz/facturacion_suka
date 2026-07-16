from flask import Flask
from config import Config
from models import db
from flask import render_template
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

from routes.productos import productos_bp
from routes.clientes import clientes_bp
from routes.ventas import ventas_bp
from models.producto import Producto
from models.inventario import Inventario
from models.tipo_prenda import TipoPrenda
from models.material import Material
from models.manga import Manga
from models.talla import Talla

app.register_blueprint(productos_bp)
app.register_blueprint(clientes_bp)
app.register_blueprint(ventas_bp)

#with app.app_context():
#    
#    print(db.metadata.tables.keys())
#
#    db.create_all()
#
#    print("=== TABLAS CREADAS ===")

@app.route("/")
def inicio():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from config import Config
from models import db
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes.productos import productos_bp
from routes.clientes import clientes_bp
from routes.ventas import ventas_bp

app.register_blueprint(productos_bp)
app.register_blueprint(clientes_bp)
app.register_blueprint(ventas_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
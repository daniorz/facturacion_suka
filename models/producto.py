from models import db


class Producto(db.Model):

    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)

    tipo_prenda = db.Column(db.String(50), nullable=False)
    
    material = db.Column(db.String(100), nullable=False)

    manga = db.Column(db.String(50))

    talla = db.Column(db.String(10))

    precio_compra = db.Column(db.Numeric(10,2))

    precio_venta = db.Column(db.Numeric(10,2))

    stock = db.Column(db.Integer, default=0)

    stock_minimo = db.Column(db.Integer, default=5)

    fecha_registro = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
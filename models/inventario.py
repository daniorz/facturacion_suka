from models import db

class Inventario(db.Model):

    __tablename__ = "inventario"

    id = db.Column(db.Integer, primary_key=True)

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey("productos.id"),
        nullable=False
    )

    talla_id = db.Column(
        db.Integer,
        db.ForeignKey("tallas.id"),
        nullable=False
        )

    stock = db.Column(
        db.Integer,
        default=0
    )

    fecha_actualizacion = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    talla = db.relationship(
        "Talla",
        backref="inventarios"
    )

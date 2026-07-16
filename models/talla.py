from models import db


class Talla(db.Model):

    __tablename__ = "tallas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )

    activo = db.Column(
        db.Boolean,
        default=True
    )

    fecha_registro = db.Column(
    db.DateTime,
    server_default=db.func.now()
    )
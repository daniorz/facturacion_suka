from models import db


class Material(db.Model):

    __tablename__ = "materiales"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(80),
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
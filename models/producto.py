from models import db


class Producto(db.Model):

    __tablename__ = "productos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    tipo_prenda_id = db.Column(
        db.Integer,
        db.ForeignKey("tipos_prenda.id"),
        nullable=False
    )

    material_id = db.Column(
        db.Integer,
        db.ForeignKey("materiales.id"),
        nullable=False
    )

    manga_id = db.Column(
        db.Integer,
        db.ForeignKey("mangas.id"),
        nullable=True
    )

    precio_compra = db.Column(
        db.Numeric(10,2)
    )

    precio_venta = db.Column(
        db.Numeric(10,2)
    )

    activo = db.Column(
        db.Boolean,
        default=True
    )

    fecha_registro = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

     # Relaciones

    tipo_prenda = db.relationship(
        "TipoPrenda",
        backref="productos"
    )

    material = db.relationship(
        "Material",
        backref="productos"
    )

    manga = db.relationship(
        "Manga",
        backref="productos"
    )

    inventarios = db.relationship(
        "Inventario",
        backref="producto",
        cascade="all, delete-orphan"
    )
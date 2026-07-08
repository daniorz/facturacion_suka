from models import db
from models.producto import Producto


def registrar_producto(datos):

    producto = Producto(

        tipo_prenda=datos["tipo_prenda"],

        material=datos["material"],

        manga=datos["manga"],

        talla=datos["talla"],

        precio_compra=datos["precio_compra"],

        precio_venta=datos["precio_venta"],

        stock=datos["stock"]

    )

    db.session.add(producto)

    db.session.commit()
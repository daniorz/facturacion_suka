from models import db
from models.producto import Producto
from models.inventario import Inventario


def registrar_producto(datos):

    producto = Producto(

        tipo_prenda_id=datos["tipo_prenda"],

        material_id=datos["material"],

        manga_id=datos["manga"],

        precio_compra=datos["precio_compra"],

        precio_venta=datos["precio_venta"]

    )

    db.session.add(producto)

    db.session.commit()
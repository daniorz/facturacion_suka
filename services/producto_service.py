from models import db
from models.producto import Producto
from models.inventario import Inventario


def registrar_producto(datos):

    producto = Producto.query.filter_by(

        tipo_prenda_id=datos["tipo_prenda"],

        material_id=datos["material"],

        manga_id=datos["manga"] or None

    ).first()

    if producto:
        print("Producto encontrado")

        inventario = Inventario.query.filter_by(

        producto_id=producto.id,

        talla_id=datos["talla"]

        ).first()

        if inventario:

            inventario.stock += int(datos["stock"])
            db.session.commit()

        else:

            inventario = Inventario(

                producto_id=producto.id,

                talla_id=datos["talla"],

                stock=datos["stock"]

            )

            db.session.add(inventario)

            db.session.commit()        

    else:

        producto = Producto(        #crear producto

            tipo_prenda_id=datos["tipo_prenda"],

            material_id=datos["material"],

            manga_id=datos["manga"] or None,

            precio_compra=datos["precio_compra"],

            precio_venta=datos["precio_venta"]

        )

        db.session.add(producto)

        db.session.commit() #flush() envía el producto a la base para obtener el ID, pero aún no confirma la transacción.

    inventario = Inventario(

        producto_id=producto.id,

        talla_id=datos["talla"],

        stock=datos["stock"]

    )

    db.session.add(inventario)

    db.session.commit()
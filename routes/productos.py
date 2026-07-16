from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.producto import Producto
from models.tipo_prenda import TipoPrenda
from models.material import Material
from models.manga import Manga
from models.talla import Talla

from services.producto_service import registrar_producto

productos_bp = Blueprint(
    "productos",
    __name__,
    url_prefix="/productos"
)


@productos_bp.route("/")
def listar():

    productos = Producto.query.order_by(
        Producto.id.desc()
    ).all()

    tipos_prenda = TipoPrenda.query.filter_by(
        activo=True
    ).order_by(
        TipoPrenda.nombre
    ).all()

    materiales = Material.query.filter_by(
        activo=True
    ).order_by(
        Material.nombre
    ).all()

    mangas = Manga.query.filter_by(
        activo=True
    ).order_by(
        Manga.nombre
    ).all()

    tallas = Talla.query.filter_by(
        activo=True
    ).order_by(
        Talla.nombre
    ).all()

    print("Tipos:", len(tipos_prenda))
    print("Materiales:", len(materiales))
    print("Mangas:", len(mangas))
    print("Tallas:", len(tallas))

    return render_template(
        "productos.html",
        productos=productos,
        tipos_prenda=tipos_prenda,
        materiales=materiales,
        mangas=mangas,
        tallas=tallas
    )

@productos_bp.route("/nuevo", methods=["POST"])
def nuevo():

    registrar_producto(request.form)

    return redirect(
        url_for("productos.listar")
    )
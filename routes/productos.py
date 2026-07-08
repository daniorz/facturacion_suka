from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.producto import Producto

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

    return render_template(
        "productos.html",
        productos=productos
    )


@productos_bp.route("/nuevo", methods=["POST"])
def nuevo():

    registrar_producto(request.form)

    return redirect(
        url_for("productos.listar")
    )
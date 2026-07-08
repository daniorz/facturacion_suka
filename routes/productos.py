from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models import db
from models.producto import Producto

productos_bp = Blueprint(
    "productos",
    __name__,
    url_prefix="/productos"
)

@productos_bp.route("/")
def listar():

    productos = Producto.query.order_by(Producto.id.desc()).all()

    return render_template("productos.html", productos=productos)

@productos_bp.route("/nuevo", methods=["POST"])
def nuevo():

    producto = Producto(
        codigo=request.form["codigo"],
        material=request.form["material"],
        manga=request.form["manga"],
        talla=request.form["talla"],
        precio_compra=request.form["precio_compra"],
        precio_venta=request.form["precio_venta"],
        stock=request.form["stock"]
    )

    db.session.add(producto)

    db.session.commit()

    return redirect(url_for("productos.listar"))
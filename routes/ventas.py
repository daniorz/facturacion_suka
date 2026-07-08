from flask import Blueprint, render_template

ventas_bp = Blueprint(
    "ventas",
    __name__,
    url_prefix="/ventas"
)

@ventas_bp.route("/")
def listar():
    return render_template("ventas.html")
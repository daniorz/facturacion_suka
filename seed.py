from app import app

from models import db

from models.tipo_prenda import TipoPrenda
from models.material import Material
from models.manga import Manga
from models.talla import Talla

def cargar_catalogo(lista, modelo, nombre_catalogo):

    for nombre in lista:

        existe = modelo.query.filter_by(
            nombre=nombre
        ).first()

        if not existe:

            db.session.add(
                modelo(
                    nombre=nombre
                )
            )

    db.session.commit()

    print(f"✅ {nombre_catalogo} cargados.")

with app.app_context():

    print("🌱 Poblando catálogos...")

    tipos_prenda = [
        "Polo",
        "Blusa",
        "Casaca",
        "Cafarena",
        "Saco",
        "Pantalón",
        "Palazo",
        "Jogger",
        "Short",
        "Vestido",
        "Falda",
        "Chompa",
        "Conjunto",
        "Prenda a Rayas"
    ]

    materiales = [
        "Algodón Pima",
        "Franela",
        "Jean",
        "Scuba",
        "Jacquard",
        "Licra",
        "Rib",
        "Rib Panameño",
        "Rib Americano",
        "Suplex",
        "Angora",
        "Darlon",
        "Chompero",
        "Chompero Trenzado",
        "Waffle",
        "Villela",
        "Paño"
    ]

    mangas = [
        "Sin manga",
        "Manga corta",
        "Manga 3/4",
        "Manga larga"
    ]

    tallas = [
        "Niño(a)",
        "M",
        "L",
        "XL",
        "XXL",
        "Oversize"
    ]

    cargar_catalogo(

    tipos_prenda,

    TipoPrenda,

    "Tipos de prenda"

    )

    cargar_catalogo(

    materiales,

    Material,

    "Materiales"

    )

    cargar_catalogo(

    mangas,

    Manga,

    "Mangas"

    )

    cargar_catalogo(

    tallas,

    Talla,

    "Tallas"

    )
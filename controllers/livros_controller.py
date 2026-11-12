from flask import Blueprint, render_template, request
from services.livro_service import buscar_livros

livros_bp = Blueprint("livros", __name__)


@livros_bp.route("/livros")
def consultar_livros():
    termo = request.args.get("q", "").strip()

    resultados = buscar_livros(termo) if termo else []

    return render_template(
        "livros.html",
        termo=termo,
        livros=resultados
    )
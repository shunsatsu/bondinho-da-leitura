
from flask import Blueprint, render_template

from services.conteudo_service import (
    listar_servicos,
    listar_atividades
)

conteudo_bp = Blueprint("conteudo", __name__)


@conteudo_bp.route("/servicos")
def consultar_servicos():
    servicos = listar_servicos()

    return render_template(
        "servicos.html",
        servicos=servicos
    )


@conteudo_bp.route("/programacao")
def consultar_programacao():
    atividades = listar_atividades()

    return render_template(
        "programacao.html",
        atividades=atividades
    )

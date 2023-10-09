# Importação de bibliotecas
from flask import Blueprint, render_template

# Importação de módulos
from src.domain.use_cases.preenche_cardapio import RecebeFormulario
from src.domain.use_cases.recebe_clientes import RecebeClientes
from src.infrastructure.repository.repositorio_cardapio import RepositorioInsercao


user_route_bp = Blueprint("user_routes", __name__)

# -----------------------------------------------ROTAS PARA PÁGINAS HTML DA CAMADA WEB-------------------------------------------
@user_route_bp.route("/")
def index():
    return render_template("index.html")


@user_route_bp.route("/additens")
def additens():
    return render_template("additens.html")


@user_route_bp.route("/lanches", methods=["GET"])
def lanches():
    session = RepositorioInsercao()
    lista_lanche = session.listar_dados()
    return render_template("lanches.html", lista_lanche=lista_lanche)


@user_route_bp.route("/bebidas")
def bebidas():
    session = RepositorioInsercao()
    lista_bebida = session.listar_bebida()
    return render_template("bebidas.html", lista_bebida=lista_bebida)


@user_route_bp.route("/acompanhamentos")
def acompanhamentos():
    session = RepositorioInsercao()
    lista_acompanhamento = session.listar_acompanhamento()
    return render_template(
        "acompanhamentos.html", lista_acompanhamento=lista_acompanhamento
    )


@user_route_bp.route("/sobremesas")
def sobremesas():
    session = RepositorioInsercao()
    lista_sobremesa = session.listar_sobremesa()
    return render_template("sobremesas.html", lista_sobremesa=lista_sobremesa)


# -----------------------------------------------ROTAS PARA CAMADA USE_CASES-------------------------------------------


@user_route_bp.route("/adicionar_lanche", methods=["GET", "POST"])
def adicionar_lanche():
    form = RecebeFormulario()
    dados_do_formulario = form.preenche()
    session = RepositorioInsercao()
    registra = session.inserir_dados(dados_do_formulario)
    if registra:
        return render_template("additens.html")
    else:
        return render_template("erro_de_registro.html")


@user_route_bp.route("/adicionar_bebida", methods=["GET", "POST"])
def adicionar_bebida():
    form = RecebeFormulario()
    dados_do_formulario = form.preenche()
    session = RepositorioInsercao()
    registra = session.inserir_bebida(dados_do_formulario)
    if registra:
        return render_template("additens.html")
    else:
        return render_template("erro_de_registro.html")


@user_route_bp.route("/adicionar_acompanhamento", methods=["GET", "POST"])
def adicionar_acompanhamento():
    form = RecebeFormulario()
    dados_do_formulario = form.preenche()
    session = RepositorioInsercao()
    registra = session.inserir_acompanhamento(dados_do_formulario)
    if registra:
        return render_template("additens.html")
    else:
        return render_template("erro_de_registro.html")


@user_route_bp.route("/adicionar_sobremesa", methods=["GET", "POST"])
def adicionar_sobremesa():
    form = RecebeFormulario()
    dados_do_formulario = form.preenche()
    session = RepositorioInsercao()
    registra = session.inserir_sobremesas(dados_do_formulario)
    if registra:
        return render_template("additens.html")
    else:
        return render_template("erro_de_registro.html")


@user_route_bp.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    form = RecebeClientes()
    dados_do_formulario = form.recebe_clientes()
    session = RepositorioInsercao()
    registra = session.inserir_clientes(dados_do_formulario)
    if registra:
        return render_template("lanches.html")
    else:
        return render_template("erro_de_registro.html")


@user_route_bp.route("/validar-cpf", methods=["GET", "POST"])
def validar_cpf():
    session = RepositorioInsercao()
    registra = session.validar_cliente()
    if registra:
        return render_template("lanches.html")
    else:
        return render_template("erro_de_registro.html")

from flask import request, redirect
from sqlalchemy import text
from src.infrastructure.database.settings.base import ItemAcompanhamento
from src.infrastructure.database.settings.base import ItemCardapio
from src.infrastructure.database.settings.base import ItemBebida
from src.infrastructure.database.settings.base import ItemSobremesa
from src.infrastructure.database.settings.base import ClienteNovo
from src.infrastructure.database.interface.repositorio_cardapio_int import (
    RepositorioCardapioInterface,
)
from src.infrastructure.database.settings.conexao import DBConnectionHandler


# ------------------------------------------------LANCHES------------------------------------------------
class RepositorioInsercao(RepositorioCardapioInterface):
    def inserir_dados(self, dados_do_formulario) -> None:
        with DBConnectionHandler() as database:
            try:
                item_novo = ItemCardapio(
                    item=dados_do_formulario["item"],
                    preco=dados_do_formulario["preco"],
                    descricao=dados_do_formulario["descricao"],
                    arquivo=dados_do_formulario["arquivo"],
                )
                database.session.add(item_novo)
                database.session.commit()

                return True
            except Exception as mensagem_erro:
                print(f"Erro durante a inserção: {str(mensagem_erro)}")
                database.session.rollback()
                return False

    def listar_dados(self):
        with DBConnectionHandler() as database:
            try:
                dados = database.session.query(ItemCardapio).all()
                return dados
            except Exception as mensagem_erro:
                print(f"Erro ao listar dados: {str(mensagem_erro)}")
                return []

    # ------------------------------------------------BEBIDAS------------------------------------------------
    def inserir_bebida(self, dados_do_formulario) -> None:
        with DBConnectionHandler() as database:
            try:
                item_novo = ItemBebida(
                    item=dados_do_formulario["item"],
                    preco=dados_do_formulario["preco"],
                    descricao=dados_do_formulario["descricao"],
                    arquivo=dados_do_formulario["arquivo"],
                )
                database.session.add(item_novo)
                database.session.commit()

                return True
            except Exception as mensagem_erro:
                print(f"Erro durante a inserção: {str(mensagem_erro)}")
                database.session.rollback()
                return False

    def listar_bebida(self):
        with DBConnectionHandler() as database:
            try:
                dados = database.session.query(ItemBebida).all()
                return dados
            except Exception as mensagem_erro:
                print(f"Erro ao listar dados: {str(mensagem_erro)}")
                return []

    # ------------------------------------------------ACOMPANHAMENTOS------------------------------------------------

    def inserir_acompanhamento(self, dados_do_formulario) -> None:
        with DBConnectionHandler() as database:
            try:
                item_novo = ItemAcompanhamento(
                    item=dados_do_formulario["item"],
                    descricao=dados_do_formulario["descricao"],
                    preco=dados_do_formulario["preco"],
                    arquivo=dados_do_formulario["arquivo"],
                )
                database.session.add(item_novo)
                database.session.commit()

                return True
            except Exception as mensagem_erro:
                print(f"Erro durante a inserção: {str(mensagem_erro)}")
                database.session.rollback()
                return False

    def listar_acompanhamento(self):
        with DBConnectionHandler() as database:
            try:
                dados = database.session.query(ItemAcompanhamento).all()
                return dados
            except Exception as mensagem_erro:
                print(f"Erro ao listar dados: {str(mensagem_erro)}")
                return []

    # ------------------------------------------------SOBREMESAS------------------------------------------------

    def inserir_sobremesas(self, dados_do_formulario) -> None:
        with DBConnectionHandler() as database:
            try:
                item_novo = ItemSobremesa(
                    item=dados_do_formulario["item"],
                    preco=dados_do_formulario["preco"],
                    descricao=dados_do_formulario["descricao"],
                    arquivo=dados_do_formulario["arquivo"],
                )
                database.session.add(item_novo)
                database.session.commit()

                return True
            except Exception as mensagem_erro:
                print(f"Erro durante a inserção: {str(mensagem_erro)}")
                database.session.rollback()
                return False

    def listar_sobremesa(self):
        with DBConnectionHandler() as database:
            try:
                dados = database.session.query(ItemSobremesa).all()
                return dados
            except Exception as mensagem_erro:
                print(f"Erro ao listar dados: {str(mensagem_erro)}")
                return []

    def inserir_clientes(self):
        with DBConnectionHandler() as database:
            try:
                dados = database.session.query(ClienteNovo).all()
                return dados
            except Exception as mensagem_erro:
                print(f"Erro ao gravar dados: {str(mensagem_erro)}")
                return []

    def validar_cliente(self):
        with DBConnectionHandler() as database:
            cpf = request.form["cpf"]
            sql = text("SELECT * FROM clientes WHERE cpf = :cpf")
            result = database.session.execute(sql, {"cpf": cpf}).fetchall()

            if result:
                return redirect("/lanches")
            else:
                return "Erro durante a validação, favor revisar as informações"

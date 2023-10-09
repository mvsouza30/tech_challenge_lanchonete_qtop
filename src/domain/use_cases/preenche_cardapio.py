from typing import Dict
import os
from flask import request
from src.domain.models.cardapio import Cardapio


class InvalidDataException(Exception):
    pass


class RecebeFormulario:
    def preenche(self) -> Dict:
        item = request.form.get("item")
        preco = float(request.form.get("preco"))
        descricao = request.form.get("descricao")
        arquivo = request.files.get("arquivo")

        if arquivo:
            nome_arquivo = arquivo.filename
            caminho_arquivo = os.path.join("/app/src/static", nome_arquivo)
            arquivo.save(caminho_arquivo)

        else:
            nome_arquivo = None

        if not item or not preco or not descricao:
            raise InvalidDataException("Todos os campos são obrigatórios")

        return {
            "item": item,
            "preco": preco,
            "descricao": descricao,
            "arquivo": nome_arquivo,
        }


class PreencheCardapio:
    def __init__(self, formulario_parser, file_manager):
        self.formulario_parser = formulario_parser
        self.file_manager = file_manager

    def recebe_item(self) -> Dict:
        try:
            dados_formulario = self.formulario_parser.parse()
            self.file_manager.save_file(
                request.files.get("arquivo"), dados_formulario["arquivo"]
            )

            cardapio = Cardapio(
                item=dados_formulario["item"],
                preco=dados_formulario["preco"],
                descricao=dados_formulario["descricao"],
                arquivo=dados_formulario["arquivo"],
            )

            return {
                "item": cardapio.item,
                "preco": cardapio.preco,
                "descricao": cardapio.descricao,
                "arquivo": cardapio.arquivo,
            }

        except InvalidDataException as dados_nao_enviados:
            raise InvalidDataException(
                "Houve problemas no envio do formulário"
            ) from dados_nao_enviados

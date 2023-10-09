import io
import tempfile
import pytest
from flask import Flask
from flask_testing import TestCase
from werkzeug.datastructures import FileStorage
from .preenche_cardapio import RecebeFormulario, InvalidDataException


class TestRecebeFormulario(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config["TESTING"] = True
        return app

    def teste_recebe_dados_validos(self):
        parser = RecebeFormulario()
        with self.app.test_request_context("/"):
            arquivo = FileStorage(
                stream=io.BytesIO(b"conteudo_do_arquivo"),
                filename="arquivo.jpg",
                content_type="image/jpg",
            )
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(arquivo.read())
                temp_file_name = temp_file.name

            self.client.post(
                "/",
                data={
                    "item": "Item de teste",
                    "preco": "10.5",
                    "descricao": "Descrição de teste",
                    "arquivo": (open(temp_file_name, "rb"), "arquivo.jpg"),
                },
                content_type="multipart/form-data",
                buffered=True,
                content_length=len(b"conteudo_do_arquivo"),
                environ_overrides={"wsgi.input": arquivo.stream},
            )

            assert arquivo.filename == "arquivo.jpg"
            assert arquivo.content_type == "image/jpg"
            assert arquivo.read() is not None
            arquivo.stream.seek(0)

            parsed_data = parser.parse()

            assert parsed_data["item"] == "Item de teste"
            assert parsed_data["preco"] == 10.5
            assert parsed_data["descricao"] == "Descrição de teste"
            assert parsed_data["arquivo"] == "arquivo.jpg"

    def teste_faltando_dados(self):
        parser = RecebeFormulario()
        with self.app.test_request_context("/"):
            self.client.post(
                "/",
                data={
                    # Faltando alguns dados
                    "item": "Item de teste",
                    "descricao": "Descrição de teste",
                },
                content_type="multipart/form-data",
                buffered=True,
            )

        with pytest.raises(InvalidDataException):
            parser.parse()

    def teste_preco_invalido(self):
        parser = RecebeFormulario()
        with self.app.test_request_context("/"):
            self.client.post(
                "/",
                data={
                    "item": "Item de teste",
                    "preco": "invalido",
                    "descricao": "Descrição de teste",
                },
                content_type="multipart/form-data",
                buffered=True,
            )

        with pytest.raises(InvalidDataException):
            parser.parse()

from typing import Dict
from flask import request


class InvalidDataException(Exception):
    pass


class RecebeClientes:
    def recebe_clientes(self) -> Dict:
        nome = request.form.get("nome")
        cpf = float(request.form.get("cpf"))
        email = request.form.get("email")

        if not nome or not cpf or not email:
            raise InvalidDataException("Todos os campos são obrigatórios")

        return {"nome": nome, "cpf": cpf, "email": email}

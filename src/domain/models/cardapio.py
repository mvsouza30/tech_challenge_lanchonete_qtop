# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

# Representação dos dados no banco de dados
class Cardapio:
    def __init__(self, item: str, preco: float, descricao: str, arquivo: str) -> None:
        self.item = item
        self.preco = preco
        self.descricao = descricao
        self.arquivo = arquivo

# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

# Representação dos dados no banco de dados
class Pedidos:
    def __init__(
        self, nome_cliente: str, item: str, preco: float, descricao: str, arquivo: str
    ) -> None:
        self.nome_cliente = nome_cliente
        self.item = item
        self.preco = preco
        self.descricao = descricao
        self.arquivo = arquivo

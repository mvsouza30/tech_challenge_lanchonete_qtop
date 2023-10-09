from abc import ABC, abstractmethod


class RepositorioCardapioInterface(ABC):
    def insert_user(
        self, item: str, preco: float, descricao: str, arquivo: str
    ) -> None:
        pass

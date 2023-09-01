from abc import ABC, abstractmethod
from typing import Dict

# Como uma interface, não posso ter instâncias desta classe.
# Esta classe apenas descreve a funcionalidade do processo.
class UserFinder(ABC):

    @abstractmethod # Precisa ser implementado em todas as classes que herdarem o UserFinder
    def find(self, first_name: str) -> Dict:
        pass
        # Apenas com o primeiro nome, vou retornar todas as informações do usuário compactadas em dicionário
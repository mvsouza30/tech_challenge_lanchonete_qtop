import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(
    reason="Sensitive test"
)  # Decorador para evitar ficar "mexendo" no banco de dados. Quando necessário testar, basta tirar o decorador.
def test_create_database_engine():
    db_connection_handle = DBConnectionHandler()
    engine = db_connection_handle.get_engine()

    assert engine is not None  # é uma validação IF

import pytest
from .conexao import DBConnectionHandler


@pytest.fixture
def conexao():
    conexao = DBConnectionHandler()
    yield conexao


def test_conexao_mysql(conexao):
    engine = conexao.get_engine()
    assert engine is not None

    session = None

    with conexao as db:
        session = db.session
        assert session is not None

    conexao.__exit__(None, None, None)

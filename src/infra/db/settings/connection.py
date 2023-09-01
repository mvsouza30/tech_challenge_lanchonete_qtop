from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
)  # Trabalhar com sessões no banco de dados, adicionar dados de forma segura


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql",
            "root",
            "myconnect",
            "127.0.0.1",
            "3306",
            "clean_database"
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(
            bind=self.__engine
        )  # Iniciando uma sessão baseada com o mecanismo de conexão
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # Encerra sessão

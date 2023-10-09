from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RepositorioBase(Base):
    __tablename__ = "cardapio"

    id = Column(Integer, primary_key=True)
    item = Column(String)
    preco = Column(Float)
    descricao = Column(String)
    arquivo = Column(String)

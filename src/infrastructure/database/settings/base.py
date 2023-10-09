from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ItemCardapio(Base):
    __tablename__ = "cardapio"

    id = Column(Integer, primary_key=True)
    item = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String(255), nullable=False)
    arquivo = Column(String(255), nullable=False)


class ItemBebida(Base):
    __tablename__ = "bebidas"

    id = Column(Integer, primary_key=True)
    item = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String(255), nullable=False)
    arquivo = Column(String(255), nullable=False)


class ItemAcompanhamento(Base):
    __tablename__ = "acompanhamentos"

    id = Column(Integer, primary_key=True)
    item = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String(255), nullable=False)
    arquivo = Column(String(255), nullable=False)


class ItemSobremesa(Base):
    __tablename__ = "sobremesas"

    id = Column(Integer, primary_key=True)
    item = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String(255), nullable=False)
    arquivo = Column(String(255), nullable=False)


class ClienteNovo(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    cpf = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

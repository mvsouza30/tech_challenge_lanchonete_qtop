# O sqlalchemy precisa entender o que temos no banco de dados.
# Então construo uma base de declaração

from sqlalchemy.orm import declarative_base

Base = declarative_base()

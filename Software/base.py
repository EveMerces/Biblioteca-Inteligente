from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from abc import ABCMeta

class BaseMeta(DeclarativeMeta, ABCMeta):
    pass

Base = declarative_base(metaclass=BaseMeta)

engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

def criar_tabelas():
    from classes.pessoa import Pessoa
    from classes.livro import Livro
    from classes.autor import Autor
    from classes.cliente import Cliente
    from classes.emprestimo import Emprestimo
    from classes.livro_autor import Livro_Autor
    Base.metadata.create_all(engine)
from sqlalchemy import Column, Integer, String, Date
from base import Base
from abc import abstractmethod

class Pessoa(Base):
    __abstract__ = True

    __tablename__ = 'pessoas'

    matricula = Column(Integer, primary_key=True)
    nome = Column(String)
    documento = Column(Integer)
    data_nascimento = Column(Date)
    email = Column(String)
    telefone = Column(Integer)
    
    def __init__(self, matricula, nome, documento, data_nascimento, email, telefone):
        self.matricula = matricula
        self.nome = nome
        self.documento = documento
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone

    @staticmethod
    @abstractmethod
    def exibir_detalhes():
        pass
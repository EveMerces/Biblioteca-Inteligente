from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from classes.pessoa import Pessoa
from datetime import *

class Cliente(Pessoa):
    __tablename__ = 'clientes'

    endereco = Column(String)
    data_registro = Column(Date)

    emprestimos = relationship("Emprestimo", back_populates="clientes")

    def __init__(self, matricula, nome, documento, data_nascimento, email, telefone, endereco):
        super().__init__(matricula, nome, documento, data_nascimento, email, telefone)
        self.endereco = endereco
        self.data_registro = date.today()

    @staticmethod
    def exibir_detalhes():
        print("\nBem-vindo(a) à nossa biblioteca!")
        print("Você está no menu de Cliente.")
        print("Este software foi desenvolvido por Alex Junior, Evelyn Mercês, Paulo Henrique e Paula Silveira.")
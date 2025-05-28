from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from classes.pessoa import Pessoa

class Autor(Pessoa):
    __tablename__ = 'autores'

    nacionalidade = Column(String)

    livros = relationship('Livro', secondary='livros_autores', back_populates='autores')

    def __init__(self, matricula, nome, documento, data_nascimento, email, telefone, nacionalidade):
        super().__init__(matricula, nome, documento, data_nascimento, email, telefone)
        self.nacionalidade = nacionalidade

    @staticmethod
    def exibir_detalhes():
        print("\nBem-vindo(a) à nossa biblioteca!")
        print("Você está no menu de Autor.")
        print("Este software foi desenvolvido por Alex Junior, Evelyn Mercês, Paulo Henrique e Paula Silveira.")
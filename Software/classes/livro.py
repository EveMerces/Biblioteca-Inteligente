from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from biblioteca import Base

class Livro(Base):
    __tablename__ = 'livros'

    isbn = Column (Integer, primary_key=True)
    titulo = Column(String)
    ano_publicacao = Column(String)
    genero = Column(String)
    _status = Column('status', Boolean)

    autores = relationship('Autor', secondary='livros_autores', back_populates='livros')
    emprestimos = relationship("Emprestimo", back_populates="livros")

    def __init__(self, isbn, titulo, ano_publicacao, genero, status=True):
        self.isbn = isbn
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.set_status(status)

    def get_status(self):
        if self._status:
            return 'Disponível'
        else:
            return 'Emprestado'

    def set_status(self, status):
        self._status = status
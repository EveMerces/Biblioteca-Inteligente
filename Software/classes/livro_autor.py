from sqlalchemy import Column, Integer, ForeignKey
from biblioteca import Base

class Livro_Autor(Base):
    __tablename__ = 'livros_autores'

    matricula = Column(Integer, ForeignKey('autores.matricula'), primary_key=True)
    isbn = Column(Integer, ForeignKey('livros.isbn'), primary_key=True)

    def __init__(self,matricula, isbn):
        self.matricula = matricula
        self.isbn = isbn
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from biblioteca import Base

class Emprestimo(Base):
    __tablename__ = 'emprestimos'

    id_emprestimo = Column(Integer, primary_key=True, autoincrement=True)
    data_emprestimo = Column(DateTime)
    data_devolucao = Column(DateTime)
    matricula = Column(Integer, ForeignKey('clientes.matricula'))
    isbn = Column(Integer, ForeignKey('livros.isbn'))

    clientes = relationship('Cliente', back_populates='emprestimos')
    livros = relationship('Livro', back_populates='emprestimos')

    def __init__ (self, data_emprestimo, data_devolucao, matricula, isbn):
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.matricula = matricula
        self.isbn = isbn
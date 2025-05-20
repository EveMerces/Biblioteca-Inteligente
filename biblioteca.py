from base import *
from classes.pessoa import Pessoa
from classes.livro import Livro
from classes.autor import Autor
from classes.cliente import Cliente
from classes.emprestimo import Emprestimo
from classes.livro_autor import Livro_Autor
from abc import ABCMeta
from datetime import datetime

class Biblioteca:
    def __init__(self, session):
        self.session = session

    # ------ Autor ------
    def criar_autor(self, matricula, nome, documento, data_nascimento, email, telefone, nacionalidade):
        autor = Autor(matricula, nome, documento, data_nascimento, email, telefone, nacionalidade)

        autor_existente = session.query(Autor).filter_by(matricula=autor.matricula).first()
        
        try:
            if autor_existente:
                print(f'\nAutor {autor.matricula} já cadastrado!')
                return
            
            autor.data_nascimento = datetime.strptime(autor.data_nascimento, "%d-%m-%Y").date()
        except ValueError as error:
            print(f'Data de nascimento no formato incorreto! Utilize DD-MM-YYYY')
            return     
        except Exception as error:
            print(f'Erro inesperado: {error}')
        
        session.add(autor)
        session.commit()
        print(f'\nAutor {autor.nome} cadastrado com sucesso!')
        
    def listar_autor(self, matricula):
        autor = session.query(Autor).filter_by(matricula=matricula).first()
        print(f'Nome do Autor: {autor.nome} | Matrícula: {autor.matricula} | Documento: {autor.documento} | Nacionalidade: {autor.nacionalidade}')

    # ------ Cliente ------
    def criar_cliente(self):
        pass

    def listar_cliente(self):
        pass

    # ------ Livro ------
    def criar_livro(self):
        pass

    def listar_livro(self):
        pass

    # ------ Empréstimo ------
    def criar_emprestimo(self):
        pass

    def listar_emprestimo(self):
        pass

    # ------ Livro Autor ------
    def associar_livro_autor(self):
        pass

    
from base import *
from classes.livro import Livro
from classes.autor import Autor
from classes.cliente import Cliente
from classes.emprestimo import Emprestimo
from classes.livro_autor import Livro_Autor
from datetime import *

class Biblioteca:
    nome_biblioteca = 'Biblioteca Inteligente'
    
    def __init__(self, session):
        self.session = session

    # ------ Biblioteca ------
    @classmethod
    def get_biblioteca(cls):
        return cls.nome_biblioteca

    @classmethod
    def set_biblioteca(cls, novo_nome):
        cls.nome_biblioteca = novo_nome
        print(f'\nNome da Biblioteca alterado para {cls.nome_biblioteca} com sucesso!')

    # ------ Autor ------
    def criar_autor(self, matricula, nome, documento, data_nascimento, email, telefone, nacionalidade):
        try:
            autor = Autor(matricula, nome, documento, data_nascimento, email, telefone, nacionalidade)

            autor_existente = session.query(Autor).filter_by(matricula=autor.matricula).first()

            if autor_existente:
                print(f'\nAutor {autor.matricula} já cadastrado!')
                return
            
            autor.data_nascimento = datetime.strptime(autor.data_nascimento, "%d/%m/%Y").date()

        except ValueError:
            print(f'\nData de nascimento no formato incorreto! Utilize DD/MM/YYYY')
            return     
        
        except Exception as error:
            print(f'\nErro inesperado: {error}')
        
        else:
            session.add(autor)
            session.commit()
            print(f'\nAutor {autor.nome} cadastrado com sucesso!')

        
    def listar_autor(self, matricula):
        try:
            if matricula == 0:
                autor = session.query(Autor).all()
                for autores in autor:
                    print(f'\nNome do Autor: {autores.nome} | Matrícula: {autores.matricula} | Documento: {autores.documento} | Nacionalidade: {autores.nacionalidade}')
            
            else:
                autor = session.query(Autor).filter_by(matricula=matricula).first()

                if autor:
                    print(f'\nNome do Autor: {autor.nome} | Matrícula: {autor.matricula} | Documento: {autor.documento} | Nacionalidade: {autor.nacionalidade}')

                else:
                    print(f'\nAutor {matricula} não encontrado!')
                    return 
                
        except Exception as error:
            print(f'\nErro inesperado: {error}')

    def atualizar_autor(self, matricula, novo_nome=None, novo_documento=None, novo_data_nascimento=None, novo_email=None, novo_telefone=None, novo_nacionalidade=None):
        try:
            autor = session.query(Autor).filter_by(matricula=matricula).first()

            if not autor:
                print(f'\nAutor {matricula} não encontrado!')
                return
            
            if novo_nome:
                autor.nome = novo_nome
            
            if novo_documento:
                autor.documento = novo_documento

            if novo_data_nascimento:
                autor.data_nascimento = novo_data_nascimento

            if novo_email:
                autor.email = novo_email
            
            if novo_telefone:
                autor.telefone = novo_telefone

            if novo_nacionalidade:
                autor.nacionalidade = novo_nacionalidade
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')  

        else:
            session.commit() 
            print(f'\nAutor {autor.nome} atualizado com sucesso!')


    def deletar_autor(self, matricula):
        try:
            autor = session.query(Autor).filter_by(matricula=matricula).first()

            if not autor:
                print(f'\nAutor {matricula} não encontrado!') 
                return 
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.delete(autor)
            session.commit()
            print(f'\nAutor {autor.matricula} removido com sucesso!')

    
    def listar_livros_autor(self, matricula):
        try:
            autor = session.query(Autor).filter_by(matricula=matricula).first()
            associacao = session.query(Livro_Autor).filter_by(matricula=matricula).first()

            if not autor:
                print(f'\nAutor {matricula} não encontrado!')
                return
            
            if not associacao:
                print(f'\nAutor {matricula} não tem livros associados!')
                return

            livros_autor = session.query(Livro).join(Livro_Autor, Livro_Autor.isbn == Livro.isbn).filter(Livro_Autor.matricula == matricula).all()

            for livros in livros_autor:
                print(f'\nISBN do Livro: {livros.isbn} | Nome do Livro: {livros.titulo} | Gênero: {livros.genero} | Ano de publicação: {livros.ano_publicacao}')
        
        except Exception as error:
            print(f'\nErro inesperado: {error}')



    # ------ Cliente ------
    def criar_cliente(self, matricula, nome, documento, data_nascimento, email, telefone, endereco):      
        try:
            cliente = Cliente(matricula, nome, documento, data_nascimento, email, telefone, endereco)

            cliente_existente = session.query(Cliente).filter_by(matricula=cliente.matricula).first()

            if cliente_existente:
                print(f'\nCliente {cliente.matricula} já cadastrado!')
                return
            
            cliente.data_nascimento = datetime.strptime(cliente.data_nascimento, "%d/%m/%Y").date()

        except ValueError:
            print(f'\nData de nascimento no formato incorreto! Utilize DD/MM/YYYY')
            return     
        
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.add(cliente)
            session.commit()
            print(f'\nCliente {cliente.nome} cadastrado com sucesso!')


    def listar_cliente(self, matricula):
        try:
            if matricula == 0:
                cliente = session.query(Cliente).all()
                for clientes in cliente:
                    print(f'\nNome do Cliente: {clientes.nome} | Matrícula: {clientes.matricula} | Documento: {clientes.documento} | Endereço: {clientes.endereco} | Data de registro: {clientes.data_registro}')
            
            else:
                cliente = session.query(Cliente).filter_by(matricula=matricula).first()

                if cliente:
                    print(f'\nNome do Cliente: {cliente.nome} | Matrícula: {cliente.matricula} | Documento: {cliente.documento} | Endereço: {cliente.endereco} | Data de registro: {cliente.data_registro}')

                else:
                    print(f'\nCliente {matricula} não encontrado!')
                    return
                
        except Exception as error:
            print(f'\nErro inesperado: {error}')

    def atualizar_cliente(self, matricula, novo_nome=None, novo_documento=None, novo_data_nascimento=None, novo_email=None, novo_telefone=None, novo_endereco=None):
        try:
            cliente = session.query(Cliente).filter_by(matricula=matricula).first()

            if not cliente:
                print(f'\nCliente {matricula} não encontrado!')
                return
            
            if novo_nome:
                cliente.nome = novo_nome
            
            if novo_documento:
                cliente.documento = novo_documento

            if novo_data_nascimento:
                cliente.data_nascimento = novo_data_nascimento

            if novo_email:
                cliente.email = novo_email
            
            if novo_telefone:
                cliente.telefone = novo_telefone

            if novo_endereco:
                cliente.endereco = novo_endereco
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')  

        else:
            session.commit() 
            print(f'\nCliente {cliente.nome} atualizado com sucesso!')


    def deletar_cliente(self, matricula):
        try:
            cliente = session.query(Cliente).filter_by(matricula=matricula).first()

            if not cliente:
                print(f'\nCliente {matricula} não encontrado!') 
                return 
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.delete(cliente)
            session.commit()
            print(f'\nCliente {cliente.matricula} removido com sucesso!')
        

    def listar_emprestimos_cliente(self, matricula):
        try:
            cliente = session.query(Cliente).filter_by(matricula=matricula).first()
            emprestimo = session.query(Emprestimo).filter_by(matricula=matricula).all()

            if not cliente:
                print(f'\nCliente {matricula} não encontrado!') 
                return 
            
            if not emprestimo:
                print(f'\nEmpréstimo do Cliente {cliente.matricula} não encontrado!') 
                return
            
            for emprestimos in emprestimo:
                data_devolucao = emprestimos.data_devolucao.strftime('%Y-%m-%d %H:%M:%S') if emprestimos.data_devolucao else "Ainda não devolvido"
                print(f"\nID empréstimo: {emprestimos.id_emprestimo} | Data empréstimo: {emprestimos.data_emprestimo.strftime('%Y-%m-%d %H:%M:%S')} | Data devolução: {data_devolucao}")

        except Exception as error:
            print(f'\nErro inesperado: {error}')

    # ------ Livro ------
    def criar_livro(self, isbn, titulo, ano_publicacao, genero):    
        try:
            livro = Livro(isbn, titulo, ano_publicacao, genero)

            livro_existente = session.query(Livro).filter_by(isbn=livro.isbn).first()

            if livro_existente:
                print(f'\nLivro {livro.isbn} já cadastrado!')
                return
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.add(livro)
            session.commit()
            print(f'\nLivro {livro.titulo} cadastrado com sucesso!')


    def listar_livro(self, isbn):
        try:
            if isbn == 0:
                livro = session.query(Livro).all()
                for livros in livro:
                    print(f'\nNome do Livro: {livros.titulo} | ISBN: {livros.isbn} | Ano de publicação: {livros.ano_publicacao} | Gênero: {livros.genero} | Status: {livros.get_status()}')

            else:
                livro = session.query(Livro).filter_by(isbn=isbn).first()

                if livro:
                    print(f'\nNome do Livro: {livro.titulo} | ISBN: {livro.isbn} | Ano de publicação: {livro.ano_publicacao} | Gênero: {livro.genero} | Status: {livro.get_status()}')

                else:
                    print(f'\nLivro {isbn} não encontrado!')
                    return
                
        except Exception as error:
            print(f'\nErro inesperado: {error}')

            
    def atualizar_livro(self, isbn, novo_titulo=None, novo_ano_publicacao=None, novo_genero=None):
        try:
            livro = session.query(Livro).filter_by(isbn=isbn).first()

            if not livro:
                print(f'\nLivro {isbn} não encontrado!')
                return
            
            if novo_titulo:
                livro.titulo = novo_titulo
            
            if novo_ano_publicacao:
                livro.ano_publicacao = novo_ano_publicacao

            if novo_genero:
                livro.genero = novo_genero
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')  

        else:
            session.commit() 
            print(f'\nLivro {livro.titulo} atualizado com sucesso!')


    def deletar_livro(self, isbn):
        try:
            livro = session.query(Livro).filter_by(isbn=isbn).first()

            if not livro:
                print(f'\nLivro {isbn} não encontrado!') 
                return 
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.delete(livro)
            session.commit()
            print(f'\nLivro {livro.isbn} removido com sucesso!')


    def emprestar_livro(self, matricula, isbn):     
        try:
            cliente = session.query(Cliente).filter_by(matricula=matricula).first() 
            livro = session.query(Livro).filter_by(isbn=isbn).first()

            if not cliente and not livro:
                print(f'\nCliente {matricula} e Livro {isbn} não encontrados!')
                return

            elif not cliente:
                print(f'\nCliente {matricula} não encontrado!')
                return

            elif not livro:
                print(f'\nLivro {isbn} não encontrado!')
                return
            
            if livro.get_status() == 'Emprestado':
                print(f'\nO Livro {livro.titulo} já está emprestado!')
                return
             
            emprestimo = Emprestimo(
                data_emprestimo = datetime.today(),
                data_devolucao = None,
                matricula = matricula,
                isbn = isbn
            )
                
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            livro.set_status(False)
            session.add(emprestimo)
            session.commit()
            print(f'\nLivro {livro.titulo} emprestado com sucesso para o Cliente {cliente.nome}!')


    def devolver_livro(self, matricula, isbn):
        try:
            cliente = session.query(Cliente).filter_by(matricula=matricula).first() 
            livro = session.query(Livro).filter_by(isbn=isbn).first()
            emprestimo = session.query(Emprestimo).filter_by(matricula=matricula, isbn=isbn).first()

            if not cliente and not livro:
                print(f'\nCliente {matricula} e Livro {isbn} não encontrados!')
                return

            elif not cliente:
                print(f'\nCliente {matricula} não encontrado!')
                return

            elif not livro:
                print(f'\nLivro {isbn} não encontrado!')
                return
            
            if livro.get_status() == 'Disponível':
                print(f'\nO Livro {livro.titulo} já está disponível!')
                return
            
            if not emprestimo:
                print(f'\nEmpréstimo não encontrado!')
                return
            else:
                emprestimo.data_devolucao = datetime.today()
                
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            livro.set_status(True)
            session.commit()
            print(f'\nLivro {livro.titulo} devolvido com sucesso!')


    def listar_autores_livro(self, isbn):
        try:
            livro = session.query(Livro).filter_by(isbn=isbn).first()
            associacao = session.query(Livro_Autor).filter_by(isbn=isbn).first()

            if not livro:
                print(f'\nLivro {isbn} não encontrado!')
                return
            
            if not associacao:
                print(f'\nLivro {isbn} não tem autores associados!')
                return

            livro_autores = session.query(Autor).join(Livro_Autor, Livro_Autor.matricula == Autor.matricula).filter(Livro_Autor.isbn == isbn).all()

            for livros in livro_autores:
                print(f'\nMatrícula do Autor: {livros.matricula} | Nome do Autor: {livros.nome} | Nacionalidade: {livros.nacionalidade} ')
        
        except Exception as error:
            print(f'\nErro inesperado: {error}')



    # ------ Empréstimo ------
    def listar_emprestimo(self, id_emprestimo):
        try:
            if id_emprestimo == 0:
                emprestimo = session.query(Emprestimo).all()
                
                for emprestimos in emprestimo:
                    data_devolucao = emprestimos.data_devolucao.strftime('%Y-%m-%d %H:%M:%S') if emprestimos.data_devolucao else "Ainda não devolvido"
                    print(f"\nID empréstimo: {emprestimos.id_emprestimo} | Data empréstimo: {emprestimos.data_emprestimo.strftime('%Y-%m-%d %H:%M:%S')} | Data devolução: {data_devolucao} | Matrícula do Cliente: {emprestimos.matricula} | ISBN do Livro: {emprestimos.isbn}")

            else:
                emprestimo = session.query(Emprestimo).filter_by(id_emprestimo=id_emprestimo).first()

                if emprestimo:
                    data_devolucao = emprestimo.data_devolucao.strftime('%Y-%m-%d %H:%M:%S') if emprestimo.data_devolucao else "Ainda não devolvido"
                    print(f"\nID empréstimo: {emprestimo.id_emprestimo} | Data empréstimo: {emprestimo.data_emprestimo.strftime('%Y-%m-%d %H:%M:%S')} | Data devolução: {data_devolucao} | Matrícula do Cliente: {emprestimo.matricula} | ISBN do Livro: {emprestimo.isbn}")

                else:
                    print(f'\nEmpréstimo {id_emprestimo} não encontrado!')
                    return
                
        except Exception as error:
            print(f'\nErro inesperado: {error}')

    def deletar_emprestimo(self, id_emprestimo):
        try:
            emprestimo = session.query(Emprestimo).filter_by(id_emprestimo=id_emprestimo).first()

            if not emprestimo:
                print(f'\nEmpréstimo {id_emprestimo} não encontrado!') 
                return 
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.delete(emprestimo)
            session.commit()
            print(f'\nEmpréstimo {emprestimo.id_emprestimo} removido com sucesso!')



    # ------ Livro Autor ------
    def associar_livro_autor(self, matricula, isbn):
        try:
            livro_autor = Livro_Autor(matricula, isbn)

            autor = session.query(Autor).filter_by(matricula=matricula).first()
            livro = session.query(Livro).filter_by(isbn=isbn).first()

            if not autor and not livro:
                print(f'\nAutor {matricula} e Livro {isbn} não encontrados!')
                return

            elif not autor:
                print(f'\nAutor {matricula} não encontrado!')
                return

            elif not livro:
                print(f'\nLivro {isbn} não encontrado!')
                return

            associacao_existente = session.query(Livro_Autor).filter_by(matricula=livro_autor.matricula, isbn=livro_autor.isbn).first()

            if associacao_existente:
                print(f'\nAssociação do Autor {livro_autor.matricula} e Livro {livro_autor.isbn} já cadastrada!')
                return
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.add(livro_autor)
            session.commit()
            print(f'\nAssociação do Autor {livro_autor.matricula} e Livro {livro_autor.isbn} criada com sucesso!')

    def listar_associacoes(self):
        try:
            livro_autor = session.query(Livro_Autor).all()

            for associacoes in livro_autor:
                print(f'\nMatrícula do Autor: {associacoes.matricula} | IBSN do Livro: {associacoes.isbn}')

        except Exception as error:
            print(f'\nErro inesperado: {error}')


    def deletar_associacao(self, matricula, isbn):
        try:
            autor = session.query(Autor).filter_by(matricula=matricula).first()
            livro = session.query(Livro).filter_by(isbn=isbn).first()

            if not autor and not livro:
                print(f'\nAutor {matricula} e Livro {isbn} não encontrados!')
                return

            elif not autor:
                print(f'\nAutor {matricula} não encontrado!')
                return

            elif not livro:
                print(f'\nLivro {isbn} não encontrado!')
                return

            associacao_existente = session.query(Livro_Autor).filter_by(matricula=matricula, isbn=isbn).first()

            if not associacao_existente:
                print(f'\nAssociação do Autor {matricula} e Livro {isbn} não encontrada!')
                return
            
        except Exception as error:
            print(f'\nErro inesperado: {error}')

        else:
            session.delete(associacao_existente)
            session.commit()
            print(f'\nAssociação do Autor {associacao_existente.matricula} e Livro {associacao_existente.isbn} excluída com sucesso!')
from biblioteca import *

biblioteca = Biblioteca(session)

def menu():
    while True:
        print("\n-====- MENU BIBLIOTECA -====-")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Autores")
        print("3. Gerenciar Clientes")
        print("4. Gerenciar Empréstimos")
        print("5. Gerenciar Associações Livro-Autor")
        print("6. Gerenciar Biblioteca")
        print("7. Sair\n")

        try:
            opcao = int(input('Digite sua opção: '))

            if opcao == 1:
                menu_livros()

            elif opcao == 2:
                menu_autores()

            elif opcao == 3:
                menu_clientes()

            elif opcao == 4:
                menu_emprestimos()

            elif opcao == 5:
                menu_livro_autor()

            elif opcao == 6:
                menu_biblioteca()

            elif opcao == 7:
                break

            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Digite uma opção válida!')

        except Exception as error:
            print(f'\nErro inesperado: {error}') 

def menu_livros():
    while True:
        print("\n-====- MENU LIVRO -====-")
        print("1. Cadastrar Livro")
        print("2. Listar Livro(s)")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Listar Autores de um Livro")
        print("8. Voltar\n")

        try:
            opcao = int(input('Digite sua opção: '))
            
            if opcao == 1:
                try:
                    isbn = int(input('\nDigite o isbn do Livro: '))
                    titulo = input('Digite o título do Livro: ')
                    ano_publicacao = input('Digite o ano de publicação do Livro: ')
                    genero = input('Digite o gênero do Livro: ')
                except ValueError:
                    print('\nISBN no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.criar_livro(isbn, titulo, ano_publicacao, genero)

            elif opcao == 2:
                try:
                    isbn = int(input('\nDigite 0 para listar todos os Livros ou isbn para listar o Livro: '))
                except ValueError:
                    print('\nISBN no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.listar_livro(isbn)

            elif opcao == 3:
                try:
                    isbn = int(input('\nDigite o ISBN do Livro que deve ser atualizado: ')) 

                    titulo = input('Digite o novo título do Livro (Pressione Enter para manter o atual): ')
                    ano_publicacao = input('Digite o novo ano de publicação do Livro (Pressione Enter para manter o atual): ')
                    genero = input('Digite o novo gênero do Livro (Pressione Enter para manter o atual): ')

                    titulo = titulo if titulo else None
                    ano_publicacao = ano_publicacao if ano_publicacao else None
                    genero = genero if genero else None

                except ValueError:
                    print('\nISBN no formato incorreto! Deve ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}')  
                else:
                    biblioteca.atualizar_livro(isbn, titulo, ano_publicacao, genero)

            elif opcao == 4:
                try:
                    isbn = int(input('\nDigite o ISBN do Livro que deve ser excluído: '))
                except ValueError:
                    print('\nISBN no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.deletar_livro(isbn)

            elif opcao == 5:
                try:
                    matricula = int(input('\nDigite a matrícula do Cliente para realizar o empréstimo: '))
                    isbn = int(input('\nDigite o ISBN do Livro para realizar o empréstimo: '))
                except ValueError:
                    print('\nMatrícula ou ISBN no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.emprestar_livro(matricula, isbn)

            elif opcao == 6:
                try:
                    matricula = int(input('\nDigite a matrícula do Cliente para devolver o livro: '))
                    isbn = int(input('\nDigite o ISBN do Livro que será devolvido: '))
                except ValueError:
                    print('\nMatrícula ou ISBN no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.devolver_livro(matricula, isbn)

            elif opcao == 7:
                try:
                    isbn = int(input('\nDigite o ISBN do Livro para listar seus autores: '))
                except ValueError:
                    print('\nISBN no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.listar_autores_livro(isbn)

            elif opcao == 8:
                break
                        
            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Digite uma opção válida!')

        except Exception as error:
            print(f'Erro inesperado: {error}')

def menu_autores():
    while True:
        print("\n-====- MENU AUTOR -====-")
        print("1. Cadastrar Autor")
        print("2. Listar Autor(es)")
        print("3. Atualizar Autor")
        print("4. Deletar Autor")
        print("5. Listar Livros de um Autor")
        print("6. Exibir detalhes")
        print("7. Voltar\n")

        try:
            opcao = int(input('Digite sua opção: '))
            
            if opcao == 1:
                try:
                    matricula = int(input('\nDigite a matrícula do Autor: '))
                    nome = input('Digite o nome do Autor: ')
                    documento = int(input('Digite o documento do Autor: '))
                    data_nascimento = input('Digite a data de nascimento do Autor (DD/MM/YYYY): ')
                    email = input('Digite o e-mail do Autor: ')
                    telefone = input('Digite o telefone do Autor: ')
                    nacionalidade = input('Digite a nacionalidade do Autor: ')       
                except ValueError:
                    print('\nMatrícula ou documento no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.criar_autor(matricula, nome, documento, data_nascimento, email, telefone, nacionalidade)

            elif opcao == 2:
                try:
                    matricula = int(input('\nDigite 0 para listar todos os Autores ou matrícula para listar o Autor: '))
                except ValueError:
                    print('\nMatrícula no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.listar_autor(matricula)

            elif opcao == 3:
                try:
                    matricula = int(input('\nDigite a matrícula do Autor que deve ser atualizado: ')) 

                    nome = input('Digite o novo nome do Autor (Pressione Enter para manter o atual): ')

                    novo_documento = input('Digite novo documento do Autor (Pressione Enter para manter o atual): ')
                    documento = int(novo_documento) if novo_documento else None

                    data_nascimento = input('Digite a nova data de nascimento do Autor (DD/MM/YYYY) (Pressione Enter para manter o atual): ')
                    if data_nascimento:
                        try:
                            data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                        except ValueError:
                                print(f'\nData de nascimento no formato incorreto! Utilize DD/MM/YYYY')
                                return     

                    email = input('Digite o novo e-mail do Autor (Pressione Enter para manter o atual): ')
                    telefone = input('Digite o novo telefone do Autor (Pressione Enter para manter o atual): ')
                    nacionalidade = input('Digite a nova nacionalidade do Autor (Pressione Enter para manter o atual): ') 

                    nome = nome if nome else None
                    data_nascimento = data_nascimento if data_nascimento else None
                    email = email if email else None
                    telefone = telefone if telefone else None
                    nacionalidade = nacionalidade if nacionalidade else None

                except ValueError:
                    print('\nMatrícula ou documento no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}')  
                else:
                    biblioteca.atualizar_autor(matricula, nome, documento, data_nascimento, email, telefone, nacionalidade)

            elif opcao == 4:
                try:
                    matricula = int(input('\nDigite a matrícula do Autor que deve ser excluído: '))
                except ValueError:
                    print('\nMatrícula no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.deletar_autor(matricula)

            elif opcao == 5:
                try:
                    matricula = int(input('\nDigite a matrícula do Autor para listar seus livros: '))
                except ValueError:
                    print('\nMatrícula no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.listar_livros_autor(matricula)

            elif opcao == 6:
                Autor.exibir_detalhes()
            
            elif opcao == 7:
                break
                        
            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Digite uma opção válida!')

        except Exception as error:
            print(f'Erro inesperado: {error}')


def menu_clientes():
    while True:
        print("\n-====- MENU CLIENTE -====-")
        print("1. Cadastrar Cliente")
        print("2. Listar Cliente(es)")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Listar Empréstimos de um Cliente")
        print("6. Exibir detalhes")
        print("7. Voltar\n")

        try:
            opcao = int(input('Digite sua opção: '))
            
            if opcao == 1:
                try:
                    matricula = int(input('\nDigite a matrícula do Cliente: '))
                    nome = input('Digite o nome do Cliente: ')
                    documento = int(input('Digite o documento do Cliente: '))
                    data_nascimento = input('Digite a data de nascimento do Cliente (DD/MM/YYYY): ')
                    email = input('Digite o e-mail do Cliente: ')
                    telefone = input('Digite o telefone do Cliente: ')  
                    endereco = input('Digite o endereço do Cliente: ')
                except ValueError:
                    print('\nMatrícula ou documento no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.criar_cliente(matricula, nome, documento, data_nascimento, email, telefone, endereco)

            elif opcao == 2:
                try:
                    matricula = int(input('\nDigite 0 para listar todos os Cliente ou matrícula para listar o Cliente: '))
                except ValueError:
                    print('\nMatrícula no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.listar_cliente(matricula)

            elif opcao == 3:
                try:
                    matricula = int(input('\nDigite a matrícula do Cliente que deve ser atualizado: ')) 

                    nome = input('Digite o novo nome do Cliente (Pressione Enter para manter o atual): ')

                    novo_documento = input('Digite o novo documento do Cliente (Pressione Enter para manter o atual): ')
                    documento = int(novo_documento) if novo_documento else None

                    data_nascimento = input('Digite a nova data de nascimento do Cliente (DD/MM/YYYY) (Pressione Enter para manter o atual): ')
                    if data_nascimento:
                        try:
                            data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                        except ValueError:
                                print(f'\nData de nascimento no formato incorreto! Utilize DD/MM/YYYY')
                                return     

                    email = input('Digite o novo e-mail do Cliente (Pressione Enter para manter o atual): ')
                    telefone = input('Digite o novo telefone do Cliente (Pressione Enter para manter o atual): ')
                    endereco = input('Digite o novo endereço do Cliente (Pressione Enter para manter o atual): ') 

                    nome = nome if nome else None
                    data_nascimento = data_nascimento if data_nascimento else None
                    email = email if email else None
                    telefone = telefone if telefone else None
                    endereco = endereco if endereco else None

                except ValueError:
                    print('\nMatrícula ou documento no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}')  
                else:
                    biblioteca.atualizar_cliente(matricula, nome, documento, data_nascimento, email, telefone, endereco)

            elif opcao == 4:
                try:
                    matricula = int(input('\nDigite a matrícula do Cliente que deve ser excluído: '))
                except ValueError:
                    print('\nMatrícula no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.deletar_cliente(matricula)

            elif opcao == 5:
                try:
                    matricula = int(input('\nDigite a matrícula do Cliente para listar seus empréstimos: '))
                except ValueError:
                    print('\nMatrícula no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.listar_emprestimos_cliente(matricula)

            elif opcao == 6:
                Cliente.exibir_detalhes()
            
            elif opcao == 7:
                break
                        
            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Digite uma opção válida!')

        except Exception as error:
            print(f'Erro inesperado: {error}')

def menu_emprestimos():
    while True:
        print("\n-====- MENU EMPRÉSTIMO -====-")
        print("1. Listar Empréstimo(s)")
        print("2. Deletar Empréstimo")
        print("3. Voltar\n")

        try:
            opcao = int(input('Digite sua opção: '))
            
            if opcao == 1:
                try:
                    id_emprestimo = int(input('\nDDigite 0 para listar todos os Empréstimos ou ID para listar o Empréstimo: '))
                except ValueError:
                    print('\nID do Empréstimo no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.listar_emprestimo(id_emprestimo)

            elif opcao == 2:
                try:
                    id_emprestimo = int(input('\nDigite o ID do Empréstimo que deve ser excluído: '))
                except ValueError:
                    print('\nID do Empréstimo no formato incorreto! Devem ser um número inteiro.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.deletar_emprestimo(id_emprestimo)

            elif opcao == 3:
                break
                        
            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Digite uma opção válida!')

        except Exception as error:
            print(f'Erro inesperado: {error}')


def menu_livro_autor():
    while True:
        print("\n-====- MENU LIVRO-AUTOR -====-")
        print("1. Cadastrar Associação")
        print("2. Listar Associações")
        print("3. Deletar Associação")
        print("4. Voltar\n")

        try:
            opcao = int(input('Digite sua opção: '))
            
            if opcao == 1:
                try:
                    matricula = int(input('\nDigite a matrícula do Autor: '))
                    isbn = int(input('\nDigite o ISBN do Livro: '))
                except ValueError:
                    print('\nMatrícula ou isbn no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.associar_livro_autor(matricula, isbn)

            elif opcao == 2:
                biblioteca.listar_associacoes()

            elif opcao == 3:
                try:
                    matricula = int(input('\nDigite a matrícula do Autor: '))
                    isbn = int(input('\nDigite o ISBN do Livro: '))
                except ValueError:
                    print('\nMatrícula ou isbn no formato incorreto! Devem ser números inteiros.')
                    return
                except Exception as error:
                    print(f'\nErro inesperado: {error}') 
                else:
                    biblioteca.deletar_associacao(matricula, isbn)

            elif opcao == 4:
                break
                        
            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Digite uma opção válida!')

        except Exception as error:
            print(f'Erro inesperado: {error}')

def menu_biblioteca():
    while True:
        print("\n-====- MENU BIBLIOTECA -====-")
        print("1. Nome da Biblioteca")
        print("2. Alterar nome da Biblioteca")
        print("3. Voltar\n")

        try:
            opcao = int(input('Digite sua opção: '))
            
            if opcao == 1:
                print(f'\nNome da Biblioteca: {Biblioteca.get_biblioteca()}')

            elif opcao == 2:
                novo_nome = input('\nDigite novo nome da Biblioteca: ')
                Biblioteca.set_biblioteca(novo_nome)

            elif opcao == 3:
                break
                        
            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Digite uma opção válida!')

        except Exception as error:
            print(f'Erro inesperado: ')

def main():
    criar_tabelas()
    menu()

if __name__ == "__main__":
    main()
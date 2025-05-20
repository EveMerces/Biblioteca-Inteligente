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
        print("6. Sair\n")

        opcao = int(input('Digite sua opção: '))

        if opcao == 1:
            pass

        elif opcao == 2:
            menu_autores()

        elif opcao == 3:
            pass

        elif opcao == 4:
            pass

        elif opcao == 5:
            pass

        elif opcao == 6:
            break

        else:
            opcao = int(input('Digite uma opção válida: '))

def menu_livros():
    pass

def menu_autores():
    while True:
        print("\n-====- MENU AUTOR -====-")
        print("1. Cadastrar Autor")
        print("2. Lista Autor")
        print("3. Atualizar Autor")
        print("4. Deletar Autor")
        print("5. Listar Livros de um Autor")
        print("6. Voltar\n")

        opcao = int(input('Digite sua opção: '))
        
        if opcao == 1:
            try:
                matricula = int(input('\nDigite a matrícula do Autor: '))
                nome = input('Digite o nome do Autor: ')
                documento = int(input('Digite o documento do Autor: '))
                data_nascimento = input('Digite a data de nascimento do Autor (DD-MM-YYYY): ')
                email = input('Digite o e-mail do Autor: ')
                telefone = input('Digite o telefone do Autor: ')
                nacionalidade = input('Digite a nacionalidade do Autor: ')       
            except ValueError:
                print('Matrícula ou documento no formato incorreto! Devem ser números inteiros.')
                return
            except Exception as error:
                print(f'Erro inesperado: {error}') 
            else:
                biblioteca.criar_autor(matricula, nome, documento, data_nascimento, email, telefone, nacionalidade)

        elif opcao == 2:
            matricula = int(input('\nDigite a matrícula do Autor: '))

            biblioteca.listar_autor(matricula)

        elif opcao == 3:
            pass

        elif opcao == 4:
            pass

        elif opcao == 5:
            pass

        elif opcao == 6:
            break
                    
        else:
            opcao = int(input('Digite uma opção válida: '))

def menu_clientes():
    pass

def menu_emprestimos():
    pass

def menu_livro_autor():
    pass

def main():
    criar_tabelas()
    menu()

if __name__ == "__main__":
    main()
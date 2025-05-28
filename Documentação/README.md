                                 𝙱𝚒𝚋𝚕𝚒𝚘𝚝𝚎𝚌𝚊 𝙸𝚗𝚝𝚎𝚕𝚒𝚐𝚎𝚗𝚝𝚎




  ![biblioteca](https://github.com/user-attachments/assets/20e75b36-08b7-40c2-babc-c92c39e7fa7d)





## 📝 Descrição
**Biblioteca Inteligente** é um sistema de gerenciamento de biblioteca desenvolvido em Python, utilizando SQLAlchemy e SQLite. 
----------------------------------------------------------------------------------------------------------------------------
## 🛠️ Estrutura do Projeto
- `biblioteca.py`: Configuração inicial do SQLAlchemy e SQLite.
- `Especificação do Projeto.pdf`: [Especificação do Projeto. Sistema de Gerenciamento com POO e SQLAlchemy.pdf](https://github.com/user-attachments/files/20265948/Especificacao.do.Projeto.Sistema.de.Gerenciamento.com.POO.e.SQLAlchemy.pdf)
- `Repositório`: https://github.com/EveMerces/Biblioteca-Inteligente
----------------------------------------------------------------------------------------------------------------------------
# 📚 Sistema de Gerenciamento de Biblioteca

O sistema tem como objetivo gerenciar uma biblioteca, incluindo o cadastro de livros, autores, clientes e o controle de empréstimos. Através de um modelo orientado a objetos e utilizando SQLAlchemy para persistência, é possível simular operações básicas de um sistema bibliotecário.

----------------------------------------------------------------------------------------------------------------------------

## 🧩 Descrição das Classes
### `Biblioteca`
Classe de controle (controller), gerencia as classes autor, cliente, livro, emprestimo, livro_autor. Ela é responsavel por *criar* os objetos dessas classes e *listar* os objetos.

### `Pessoa` (classe abstrata)
Classe base para `Autor` e `Cliente`. Contém atributos comuns como matrícula, nome, documento, data de nascimento, e-mail e telefone.

### `Autor`
Herda de `Pessoa`. Representa um autor com nacionalidade e associação com livros através da tabela intermediária `livros_autores`.

### `Cliente`
Herda de `Pessoa`. Representa um cliente da biblioteca com endereço, data de registro e relação com empréstimos.

### `Livro`
Contém informações como ISBN, título, ano de publicação, gênero e status (disponível ou emprestado). Pode estar associado a vários autores.

### `Emprestimo`
Controla os registros de empréstimos de livros, incluindo datas e ligação entre clientes e livros.

### `Livro_Autor`
Tabela associativa para representar a relação muitos-para-muitos entre livros e autores.

---------------------------------------------------------------------------------------------------------------------------
## 🔧 Funcionalidades Principais
Cadastro e atualização de clientes, autores e livros.

Emprestar e devolver livros.

Associação entre livros e autores.

Listagem e remoção de clientes, autores, livros e emprestimos.

Listagem de empréstimos por cliente e de livros por autor.

--------------------------------------------------------------------------------------------------------------------------
## 👥 Nome dos Integrantes
- Evelyn Mercês da Silva- RA: 2404227
- Paula Silveira e Silva- RA: 2402756
- Alex Manoel dos Santos Junio- RA: 1701381
- Paulo Henrique Pires Cordeiro- RA: 2402602

## ▶️ Como Executar

1. **Pré-requisitos:**

- Python 3.10+
- SQLAlchemy 
- Biblioteca `base.py` com a configuração do `Base` declarativo

1. **Passos para execução:**
   - Criação do banco de dados
   - Criação das tabelas

   ```bash
   pip install sqlalchemy

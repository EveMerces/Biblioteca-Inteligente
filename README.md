# Biblioteca Inteligente

## 📝 Descrição
**Biblioteca Inteligente** é um sistema de gerenciamento de biblioteca desenvolvido em Python, utilizando SQLAlchemy e SQLite. 
----------------------------------------------------------------------------------------------------------------------------
## 🛠️ Estrutura do Projeto
- `biblioteca.py`: Configuração inicial do SQLAlchemy e SQLite.
- `Especificação do Projeto.pdf`: [Especificação do Projeto. Sistema de Gerenciamento com POO e SQLAlchemy.pdf](https://github.com/user-attachments/files/20265948/Especificacao.do.Projeto.Sistema.de.Gerenciamento.com.POO.e.SQLAlchemy.pdf)

----------------------------------------------------------------------------------------------------------------------------
# 📚 Sistema de Gerenciamento de Biblioteca

O sistema tem como objetivo gerenciar uma biblioteca, incluindo o cadastro de livros, autores, clientes e o controle de empréstimos. Através de um modelo orientado a objetos e utilizando SQLAlchemy para persistência, é possível simular operações básicas de um sistema bibliotecário.

----------------------------------------------------------------------------------------------------------------------------

## 🧩 Descrição das Classes

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

Registro e devolução de empréstimos.

Associação entre livros e autores.

Listagem de empréstimos por cliente e de livros por autor (em desenvolvimento).
--------------------------------------------------------------------------------------------------------------------------
## 👥 Nome dos Integrantes
- Evelyn Mercês
- Paula Silveira
- Alex
- Paulo Henrique
## ▶️ Como Executar

1. **Pré-requisitos:**
   - Python 3.10+
   - SQLAlchemy
   - Biblioteca `base.py` com a configuração do `Base` declarativo

2. **Passos para execução:**
   - Configure a conexão com o banco de dados no arquivo principal.
   - Importe as classes necessárias.
   - Utilize as classes para realizar inserções e consultas utilizando SQLAlchemy.

   ```bash
   pip install sqlalchemy

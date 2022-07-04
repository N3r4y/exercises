# Função para mostrar o menu na tela
def show_menu():
    print('''    Escolha uma opção: 
    1. Inserir um novo cadastro
    2. Mostrar todos os cadastros
    3. Encerrar
    ''')

# Contador definido para 0.
# Esse contador será usado no incremento do identificador (id).
count = 0


# Função para cadastrar livros.
# Essa função usa a variável 'count' para incrementar o identificador(id).
# Se o count exceder o número 5, significa que o número máximo de livros cadastrados foi atingido.

def insert(books):
    global count
    if count < 5:
        count = count + 1                         # Incrementa o contador cada vez que a função é executada.
        identifier = count                        # Atribui o valor do contador à variável identifier
        name = input('Nome: ')
        autor = input('Autor: ')
        publisher = input('Editora: ')
        books.append((identifier, name, autor, publisher))
    else:
        print("""
        Sistema de cadastro lotado. Não é possível armazenar mais informações!
              """)


# Função para mostrar a lista de livros cadastrados na tela.

def show(books):
    global count                                  # Invoca a variável count que inicialmente foi definida como 0 (zero).
    if count > 0:                                 # Testa o valor da variável count para validar se a lista não está vazia.
        for books in books:                       # Percorre a lista books para imprimir todos os resultados cadastrados.
            identifier, name, autor, publisher = books
            print(f'Id: {identifier}, Nome: {name}, Autor: {autor}, Editora: {publisher}')
    else:
        print("""
        Lista vazia!
        """)

# Função principal que importará as demais funções que serão escolhidas pelo usuário.
# Essa função invocará o metodo referente ao código selecionado pelo usuário.

def main():
    books = []

    while True:
        show_menu()
        option = int(input('Opção?: '))
        if option == 1:
            insert(books)
        elif option == 2:
            show(books)
        elif option == 3:
            print("""
            Encerrando o programa!
            """)
            exit()
        else:
            print("""
            Opção inválida!
            """)
main()
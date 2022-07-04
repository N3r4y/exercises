from time import sleep


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
        print(f'\nInserindo novo cadastro...')
    else:
        print(f'\033[31mSistema de cadastro lotado. Não é possível armazenar mais informações!\033[m')
    sleep(2)


# Função para mostrar a lista de livros cadastrados na tela.

def show(books):
    global count                                  # Invoca a variável count que inicialmente foi definida como 0 (zero).
    if count > 0:                                 # Testa o valor da variável count para validar se a lista não está vazia.
        for books in books:                       # Percorre a lista books para imprimir todos os resultados cadastrados.
            identifier, name, autor, publisher = books
            print('Buscando livros cadastrados...\n')
            sleep(2)
            print(f'\033[33mId:\033[m {identifier}  \033[33mNome:\033[m {name}  \033[33mAutor:\033[m {autor}  \033[33mEditora:\033[m {publisher}')
    else:
        print("\033[31mLista vazia!\033[m")
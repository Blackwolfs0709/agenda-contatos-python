'''nomes = ['Ana', 'Rafa','João']

for nome in nomes:
    print(f'Ola, {nome}!')'''

#no for nome in nomes, o "nome" é uma variável temporária que representa cada elemento da lista "nomes" durante a iteração.

'''contatos = {
    'Ana': {'email': 'ana@email.com', 'idade': 24},
    'Rafa': {'email': 'rafa@email.com', 'idade': 30}
}

for nome, dados in contatos.items():
    print(nome, '-', dados['email'])'''

#no for nome, dados in contatos.items(), "nome" representa a chave do dicionário (o nome da pessoa) e "dados" representa o valor associado a essa chave (outro dicionário com email e idade).


#versão inicial da função adicionar_contato, que permite ao usuário adicionar um novo contato ao dicionário "contatos".
'''def adicionar_contato():
    nome = input('Nome: ')
    email = input('Email: ')
    idade = int(input('Idade: '))

    contatos[nome] = {
        'email': email, 
        'idade': idade
    }
    print(f'Contato {nome} adicionado com sucesso!'/n)
          
#chama a função para adicionar um novo contato
adicionar_contato()
#exibe os contatos atualizados
print(contatos)'''

#versão melhorada da função adicionar_contato.

contatos = {}

def adicionar_contatos():
    while True:
        nome = input("Nome: ")
        email = input("Email: ")
        idade = int(input("Idade: "))

        contatos[nome] = {"email": email, "idade": idade}
        print(f"\nContato '{nome}' adicionado!\n")

        continuar = input("Adicionar mais um contato? (s/n) ")
        if continuar.lower() != "s":
            break

adicionar_contatos()
print("\nAgenda final:", contatos)
def adicionar_contato():
    nome = input("Nome: ").strip()

    if nome in contatos:
        print("Esse contato já existe.")
        return

    email = input("Email: ").strip()
    #strip limpa os espaços

    while True:
        idade = input("Idade: ")
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print("Idade inválida. Digite apenas números.")


    contatos[nome] = {
        "email": email,
        "idade": idade
    }
    
    print(f"/nContato '{nome}' adicionado com sucesso!")

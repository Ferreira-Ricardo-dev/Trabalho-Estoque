print ("Cadastro de Estoque")
matriz = []
while True:
    verify = int(input("Digite qual operação você deseja fazer:\n1 - Cadastrar Produto\n2 - Visualizar estoque\n3 - Editar(Quantidade/Preço)\n4 - Excluir Produto\n5 - Sair do Sistema\n"))
    if verify == 1:
        produto = []
        nome = input("Digite o nome do produto: ")
        produto.append(nome)
        categoria = input("Digite a categoria do produto: ")
        produto.append(categoria)
        qtd = int(input("Digite a quantidade do produto: "))
        produto.append(qtd)
        valor_unt = float(input("Digite o valor unitário do produto: "))
        produto.append(valor_unt)  
        valor_total = qtd*valor_unt
        produto.append(valor_total)
        matriz.append(produto)

    elif verify == 2:
        if not matriz:
            print("Nenhum item cadastrado.")

        else:
            for i, produto in enumerate(matriz):
                if produto[2] < 5:
                    print(f"Produto {i+1} Com Estoque Baixo - Nome: {produto[0]}, Categoria: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}, Valor Total: {produto[4]}")
                else:
                    print(f"Produto {i+1} - Nome: {produto[0]}, Categoria: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}, Valor Total: {produto[4]}")

    elif verify == 3:
        nome_procurado = input("Digite o nome do produto que você deseja editar: ")
        encontrado = False
        for produto in matriz:
            if nome_procurado == produto[0]:
                new_qtd = int(input("Digite a nova quantidade: "))
                new_preco = float(input("Digite o novo preço: "))
                new_total = new_qtd * new_preco
                encontrado = True

                produto[2] = new_qtd
                produto[3] = new_preco
                produto[4] = new_total

                break

        if not encontrado:
            print(f"Não foi encontrado nenhum produto com o nome de {nome_procurado}.")

    elif verify == 4:
        nome_procurado = input("Digite o nome do produto que você deseja excluir: ")
        encontrado = False
        for produto in matriz:
            if nome_procurado == produto[0]:
                matriz.remove(produto)
                print(f"Produto {nome_procurado} excluído com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print(f"Não foi encontrado nenhum produto com o nome de {nome_procurado}.")

    elif verify == 5:
        print("Encerrando Operação...\nObrigado por usar nossos serviços.")
        break

    else:
        print("Opção inválida\nEscolha uma das opções válidas")
        continue

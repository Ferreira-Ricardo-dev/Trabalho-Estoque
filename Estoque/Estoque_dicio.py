def adicionar_item(matriz): #def com a opção de adicionar produtos
    name = input("Digite o nome do produto: ")
    matriz["Nome"].append(name)
    category = input("Digite a categoria do produto: ")
    matriz["Categoria"].append(category)
    qtd = int(input("Digite a quantidade do produto: "))
    matriz["Quantidade"].append(qtd)
    valor_unt = float(input("Digite o valor unitário do produto: "))
    matriz["Preço"].append(valor_unt)
    valor_tot = qtd*valor_unt
    matriz["Valor Total"].append(valor_tot)
    return matriz

def visualizar_item(matriz): #def que mostra todos os produtos cadastrados na matriz
    if not matriz:
        print("Nenhum item cadastrado.")
    else:
        num_matriz = len(matriz["Nome"])
        for i in range(num_matriz):
            nome_visualizador = matriz["Nome"][i]
            categoria_visualizador = matriz["Categoria"][i]
            quantidade_visualizador = matriz["Quantidade"][i]
            preco_visualizador = matriz["Preço"][i]
            valor_total_visualizador = matriz["Valor Total"][i]
            if quantidade_visualizador < 5:
                print("**Estoque Baixo**")
                print(f"Produto {i+1}, Nome: {nome_visualizador}, Categoria: {categoria_visualizador}, Quantidade: {quantidade_visualizador}, Preço: R${preco_visualizador}, Valor Total: R$ {valor_total_visualizador}")
            else:
                print(f"Produto {i+1}, Nome: {nome_visualizador}, Categoria: {categoria_visualizador}, Quantidade: {quantidade_visualizador}, Preço: R${preco_visualizador}, Valor Total: R$ {valor_total_visualizador}")


def editar_item(matriz): #def que edita um produto na matriz
    if not matriz:
        print("Nenhum item cadastrado")
    else:
        nome_procurado = input("Digite o nome do produto que você deseja editar: ")
        encontrado = False
        for i in range(len(matriz["Nome"])):
            if nome_procurado == matriz["Nome"][i]:
                    new_qtd = int(input("Digite a nova quantidade: "))
                    new_preco = float(input("Digite o novo preço: "))
                    new_total = new_qtd * new_preco
                    encontrado = True
                    matriz["Quantidade"][i] = new_qtd
                    matriz["Preço"][i] = new_preco
                    matriz["Valor Total"][i] = new_total
                    print(f"Produto {nome_procurado} editado com sucesso!")
                    return matriz
            if not encontrado:
                print(f"Não foi encontrado nenhum produto com o nome de {nome_procurado}.")
            return matriz

def excluir_item(matriz): #def para excluir um produto na matriz
    nome_procurado = input("Digite o nome do produto que você deseja excluir: ")
    encontrado = False
    for i in range(len(matriz)):
        if nome_procurado == matriz["Nome"][i]:
            matriz["Nome"].pop(i)
            matriz["Categoria"].pop(i)
            matriz["Quantidade"].pop(i)
            matriz["Preço"].pop(i)
            matriz["Valor Total"].pop(i)
            print(f"Produto '{nome_procurado}' excluído com sucesso!")
            encontrado = True
            break # Interrompe o loop
    if not encontrado:
        print(f"Não foi encontrado nenhum produto com o nome de {nome_procurado}.")
    return matriz

print("Gerenciamento de Estoques")
print("-----------------------------------------------------------")
nome = []
categoria = []
quantidade = []
preco = []
valor_total = []
matriz = {
    "Nome" : nome,
    "Categoria" : categoria,
    "Quantidade" : quantidade,
    "Preço" : preco,
    "Valor Total" : valor_total
}
while True:
    verify = int(input("Digite qual operação você deseja fazer:\n1 - Cadastrar Produto\n2 - Visualizar estoque\n3 - Editar(Quantidade/Preço)\n4 - Excluir Produto\n5 - Sair do Sistema\n"))
    if verify == 1:
        matriz = adicionar_item(matriz)
        
    elif verify == 2:
        visualizar_item(matriz)
        
    elif verify == 3:
        matriz = editar_item(matriz)
        
    elif verify == 4:
        matriz = excluir_item(matriz)
        
    elif verify == 5:
        print("Encerrando Operação...\nObrigado por usar nossos serviços.")
        break
    
    else:
        print("Opção inválida. Escolha uma das opções válidas (1 a 5).")
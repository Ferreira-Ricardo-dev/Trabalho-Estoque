import pandas as pd #imports das bibliotecas necessárias para exportar um arquivo em excel
import os 

def adicionar_item(matriz): #def com a opção de adicionar produtos
    code = input("Digite o código do produto: ")
    matriz["Código"].append(code)
    description = input("Digite uma descrição para o produto: ")
    matriz["Descrição"].append(description)
    category = input("Digite a categoria do produto (Matéria-Prima ou Produto Acabado): ")
    matriz["Categoria"].append(category)
    unit = input("Digite a unidade do produto (kg, L, un, outros): ")
    matriz["Unidade"].append(unit)
    print("Produto Cadastrado!")
    return matriz

def visualizar_item(matriz): #def que mostra todos os produtos cadastrados no dicionário
    num_matriz = len(matriz["Código"])
    for i in range(num_matriz -1, -1, -1):#usando start, stop, step para acessar o dicionário de traz para frente para visualização em pilha
        code_view = matriz["Código"][i]
        description_view = matriz["Descrição"][i]
        category_view = matriz["Categoria"][i]
        unit_view = matriz["Unidade"][i]

        print(f"Produto (ID {i+1}), Código: {code_view}, Descrição: {description_view}, Categoria: {category_view}, Unidade: {unit_view}")


print("Cadastro de itens")
print("-----------------------------------------------------------")
code = []
description = []
category = []
unit = []

matriz = {
    "Código" : code,
    "Descrição" : description,
    "Categoria" : category,
    "Unidade" : unit,
}
while True:
    verify = int(input("Digite qual operação você deseja fazer:\n1 - Cadastrar Produto\n2 - Visualizar itens cadastrados\n3 - Exportar os dados(Planilha Excel)\n4 - Encerrar o Sistema\n"))
    if verify == 1:
        matriz = adicionar_item(matriz)
        
    elif verify == 2:
        visualizar_item(matriz)
        
    elif verify == 3:
        while True:
            verify_sub = int(input("Você deseja exportar os dados como uma planilha do Excel:\n1-SIM\n2-NÃO\n"))
            if verify_sub == 1:
                if not matriz["Código"]:
                    print("Não é possível exportar uma planilha vazia, adicione algum item.")
                    break
                else:
                    matriz_df = pd.DataFrame(matriz)
                    nome_arquivo = input("Digite o nome da planilha (ex: planilha_final): ")
                    if ".xlsx" in nome_arquivo:
                        print("Digite o nome do arquivo sem a extensão")
                        continue
                    else:
                        nome_arquivo = nome_arquivo+".xlsx"
                    matriz_df.to_excel(nome_arquivo, index=False)
                    ''' A função to_excel nesse caso está recebendo o nome do arquivo excel que será criado e
                    também recebe o index=False para não exibir a coluna de índices na planilha final em Excel, 
                    caso seja preciso mostrar essa coluna e só remover o segundo argumento'''
                    caminho_arquivo = os.path.abspath(nome_arquivo) #função para mostrar para o usuário o caminho do arquivo

                    print("---Aquivo criado com sucesso!---")
                    print(f"Dados exportados para: {nome_arquivo}")
                    print(f"Localização do arquivo: {caminho_arquivo}")


            elif verify_sub == 2:
                break

            else:
                print("Entrada inválida, escolha uma opção válida.")
                continue
        
    elif verify == 4:
        print("Encerrando Operação...\nObrigado por usar nossos serviços.")
        break
    
    else:
        print("Opção inválida. Escolha uma das opções válidas (1 a 4).")
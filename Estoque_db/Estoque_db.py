#Tentando implementar Banco de Dados no sistema de estoque
#Importando bibliotecas
import sqlite3
from datetime import datetime

#Def para inicializar banco de dados
def inicializacao():
    #Criação das Tabelas e conexões/cursor
    conn = sqlite3.connect('estoque.db')
    conn.row_factory = sqlite3.Row #Formata as saídas para dicionário, facilitando a sintaxe
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    unidade TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unit REAL NOT NULL
);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS movimentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    datahora TEXT NOT NULL,
    quantidade_movimentada REAL NOT NULL,
    quantidade_final REAL NOT NULL,
    FOREIGN KEY (item_id) REFERENCES estoque(id) ON DELETE CASCADE
)""")
    return conn, cursor

def adicionar_item(nome, categoria, unidade, quantidade, valor_unit): #def com a opção de adicionar produtos
    conn, cursor = inicializacao()
    insert = ("""INSERT INTO estoque (nome, categoria, unidade, quantidade, valor_unit) VALUES (?, ?, ?, ?, ?)""")
    cursor.execute(insert, (nome, categoria, unidade, quantidade, valor_unit))
    print(f"Produto {nome} adicionado com sucesso!")
    conn.commit()
    conn.close()
    return

def visualizar_item(): #def que mostra todos os produtos cadastrados no banco de dados
    conn, cursor = inicializacao()
    cursor.execute("""SELECT * FROM estoque ORDER BY id ASC""")
    for produto in cursor:
        print(f"ID {produto['id']} - Nome: {produto['nome']} - Categoria: {produto['categoria']} - Unidade: {produto['unidade']} - Quantidade: {produto['quantidade']} - Valor: {produto['valor_unit']}")
        print("="*100)
    
    conn.commit()
    conn.close()
    return

#def para buscar itens especificos pelo nome ou pela categoria
def buscar_item(buscador):
    conn, cursor = inicializacao()
    cursor.execute("""SELECT * FROM estoque WHERE nome = ? OR categoria = ?""", (buscador, buscador))
    item_encontrado = cursor.fetchone()
    if item_encontrado is None:
        print("Nenhum produto encontrado!")
        conn.commit()
        conn.close()
        return None

    else:
        print("Produto encontrado!")
        print(f"ID {item_encontrado['id']} - Nome: {item_encontrado['nome']} - Categoria: {item_encontrado['categoria']} - Unidade: {item_encontrado['unidade']} - Quantidade: {item_encontrado['quantidade']} - Valor: {item_encontrado['valor_unit']}")
        print("="*100)
        conn.commit()
        conn.close()
        return item_encontrado
    
def movimentacao_item(buscador, opcao):
    conn, cursor = inicializacao()
    item_encontrado = buscar_item(buscador)
    if item_encontrado is None:
        print("Nenhum item encontrado!")
        conn.close()
        return
    else:
        nome = item_encontrado['nome']
        id_d = item_encontrado['id']
        quantidade_inicial = int(item_encontrado['quantidade'])
        quantidade_movimentada = 0
        tipo_movimento = ""
        data_n = datetime.now()
        datahora = data_n.strftime("%d/%m%Y, %H:%M;%S")
        if opcao == 1:
            while True:
                try:
                    quantidade_movimentada = int(input(f"Digite quantas unidades serão adicionadas à '{nome}': "))
                    break
                except TypeError:
                    print("Entrada inválida! Tente novamente.")
                    continue
            cursor.execute("""UPDATE estoque SET quantidade = quantidade + ? WHERE nome = ?""", (quantidade_movimentada, nome))
            conn.commit()
            tipo_movimento = "Entrada"
        elif opcao == 2:
            while True:
                try:
                    quantidade_movimentada = int(input(f"Digite quantas unidades serão retiradas de '{nome}': "))
                    break
                except TypeError:
                    print("Entrada inválida! Tente novamente.")
                    continue
                
            if quantidade_movimentada > quantidade_inicial:
                print("Não é possível realizar essa operação!")
                print(f"Quantidade no estoque: {quantidade_inicial}\nRetirada Requisitada: {quantidade_movimentada}")
                return
            else:
                cursor.execute("""UPDATE estoque SET quantidade = quantidade - ? WHERE nome = ?""", (quantidade_movimentada, nome))
                tipo_movimento = "Saída"
                conn.commit()
        
        cursor.execute("SELECT quantidade FROM estoque WHERE nome = ?", (nome, ))
        quantidade_atualizada_list = cursor.fetchone()
        quantidade_atualizada = quantidade_atualizada_list[0]
        insert = ("""INSERT INTO movimentos (item_id, tipo, datahora, quantidade_movimentada, quantidade_final) 
        VALUES (?, ?, ?, ?, ?)""")
        cursor.execute(insert, (id_d, tipo_movimento, datahora, quantidade_movimentada, quantidade_atualizada))
        conn.commit()
        print(f"Movimentação de {quantidade_movimentada} unidades realizada com sucesso. Novo estoque: {quantidade_atualizada}")
        conn.close()
        return

def editar_item(buscador, opcao): #def que edita um produto no banco de dados
    conn, cursor = inicializacao()
    item_encontrado = buscar_item(buscador)
    if item_encontrado is None:
        print("Nenhum item encontrado!")
        conn.close()
        return
    else:
        nome = item_encontrado['nome']
        id = item_encontrado['id']
        if opcao == 1:
            while True:
                try:
                    editor = int(input(f"Qual valor de {nome} será alterado:\n1 - Nome\n2 - Categoria\n3 - Unidade\n4 - Valor\n5 - Quantidade(!)"))
                    break
                except ValueError:
                    print("Você deve digitar uma das opções!")
                    continue

            if editor == 1:
                nome_new = input(f"Digite o novo nome para '{nome}': ")
                cursor.execute("UPDATE estoque SET nome = ? WHERE id = ?", (nome_new, id))
                print(f"Nome '{nome}' atualizado com sucesso para {nome_new}")

            elif editor == 2:
                categoria_new = input(f"Digite o nova categoria para '{nome}': ")
                cursor.execute("UPDATE estoque SET categoria = ? WHERE id = ?", (categoria_new, id))
                print(f"Categoria de '{nome}' atualizado com sucesso para {categoria_new}")

            elif editor == 3:
                unidade_new = input(f"Digite a nova unidade para '{nome}': ")
                cursor.execute("UPDATE estoque SET unidade = ? WHERE id = ?", (unidade_new, id))
                print(f"Unidade de '{nome}' atualizado com sucesso para {unidade_new}")

            elif editor == 4:
                valor_new = float(input(f"Digite o novo valor para '{nome}': "))
                cursor.execute("UPDATE estoque SET valor_unit = ? WHERE id = ?", (valor_new, id))
                print(f"Valor de '{nome}' atualizado com sucesso para {valor_new}")

            elif editor == 5:
                print("Alterar a quantidade por 'edição' não registra uma transação no sistema!!")
                while True:
                    try:
                        operacao = int(input("Deseja prosseguir com a operação:\n1 - SIM\n2 - NÃO"))
                        break
                    except ValueError:
                        print("Você deve digitar uma das opções!")
                        continue
                if operacao == 1:
                    quantidade_new = input(f"Digite a nova quantidade para '{nome}': ")
                    cursor.execute("UPDATE estoque SET quantidade = ? WHERE id = ?", (quantidade_new, id))
                    print(f"Quantidade de '{nome}' atualizado com sucesso para {quantidade_new}")

                elif operacao == 2:
                    print("Operação Cancelada")

        elif opcao == 2:
            print(f"Atenção!!! caso o item {nome} for excluido todos os registros envolvendo o item serão perdidos!")
            while True:
                try:
                    editor = int(input("Continuar exclusão:\n1 - SIM\n2 - NÃO\n"))
                    break
                except ValueError:
                    print("Você deve digitar uma das opções!")
                    continue
                except editor != 1 and editor != 2:
                    print("Opção inválida! Tente novamente.")
                    continue
            if editor == 1:
                cursor.execute("DELETE FROM estoque WHERE nome = ?", (nome, ))
                print(f"Produto '{nome}' excluido com sucesso!")
            elif editor == 2:
                print(f"Exclusão de {nome} cancelada") 


        conn.commit()
        conn.close()
        return

def verificar_estoque(): #def para verificar se há linhas no banco de dados
    conn, cursor = inicializacao()
    cursor.execute("SELECT COUNT(*) FROM estoque")
    linhas = cursor.fetchone()
    resultado = linhas[0]
    if resultado == 0:
        return resultado
    return 1
    
def alerta_estoque():
    conn, cursor = inicializacao()
    verify_estoque = verificar_estoque()
    if verify_estoque != 0:
        quantidade_alerta = 20
        cursor.execute("SELECT * FROM estoque WHERE quantidade <= ?", (quantidade_alerta, ))
        produtos_estoque_baixo = cursor.fetchall()
        for produto in produtos_estoque_baixo:
            print(f"ALERTA - Produto ID {produto['id']} - Nome: {produto['nome']} - ESTOQUE BAIXO {produto['quantidade']}")
            print("="*100)
        conn.close()
        return
    return


print("--          Gerenciamento de Estoques          --")
print("="*50)
inicializacao()
while True:
    alerta_estoque()
    while True:
        try:
            verify = int(input("Digite qual operação você deseja fazer:\n1 - Cadastrar Produto\n2 - Visualizar estoque\n3 - Buscar Produto\n4 - Movimentar Estoque (ENTRADA/SAÍDA)\n5 - Editar/Excluir item\n6 - Sair do sistema\n"))
            break
        except ValueError:
            print("Digite uma opção válida!")
            continue
    if verify == 1:
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto(Limpeza, Alimentos, etc): ")
        unidade = input("Digite a unidade do produto(un, cx, ml, etc): ")
        while True:
            try:
                quantidade = int(input("Digite a quantidade: "))
                valor_unit = float(input("Digite o valor unitário dos produtos: "))
                break
            except TypeError:
                print("Entrada inválida! Tente novamente.")
                continue
            except Exception as e:
                print(f"Ocorreu um erro inesperado {e}")
                print("Tente Novamente.")
                continue
        adicionar_item(nome, categoria, unidade, quantidade, valor_unit)
        print("\n")
        
    elif verify == 2:
        verify_estoque = verificar_estoque()
        if verify_estoque != 0:
            visualizar_item()
            print("\n")
        else:
            print("O banco de dados está vazio, adicione algum item para fazer operações.\n")
        
    elif verify == 3:
        verify_estoque = verificar_estoque()
        if verify_estoque != 0:
            buscador = input("Digite o nome ou a categoria do produto que deseja buscar: ")
            buscar_item(buscador)
            print("\n")
        else:
            print("O banco de dados está vazio, adicione algum item para fazer operações.\n")

    elif verify == 4:
        verify_estoque = verificar_estoque()
        if verify_estoque != 0:        
            buscador = input("Digite o nome ou a categoria do produto que deseja movimentar: ")
            opcao = int(input("Digite qual operação deseja fazer:\n1 - Entrada\n2 - Saída\n"))
            movimentacao_item(buscador, opcao)
            print("\n")
        else:
            print("O banco de dados está vazio, adicione algum item para fazer operações.\n")

    
    elif verify == 5:
        verify_estoque = verificar_estoque()
        if verify_estoque != 0:
            buscador = input("Digite o nome ou a categoria do produto que deseja modificar: ")
            while True:
                try:
                    opcao = int(input("Qual operação você deseja fazer:\n1 - Editar\n2 - Excluir\n"))
                    break
                except ValueError:
                    print("Você deve digitar uma das opções!")
                    continue
            editar_item(buscador, opcao)
            print("\n")
        else:
            print("O banco de dados está vazio, adicione algum item para fazer operações.\n")

    elif verify == 6:
        print("Encerrando Operação...\nObrigado por usar nossos serviços.")
        break
    
    else:
        print("Opção inválida. Escolha uma das opções válidas (1 a 5).")
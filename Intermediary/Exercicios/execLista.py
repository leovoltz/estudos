import os

listas_compras = []

while True:
    print("~" * 40)
    print("Selecione uma das opções")
    print("~" * 40)
    print("\t[I] - Inserir \n\t[A] - Apagar \n\t[L] - Listar \n\t[F] - Finalizar")
    opcao = input("Digite a opção desejada: ").upper()
    print(opcao)
    os.system('clear')
   
    if opcao == "I":
        item = input("Digite o nome do que deseja adicionar a lista: ")
        listas_compras.append(item)
    
    elif opcao == "A":
        try:
            os.system('clear')
            apagar = int(input("Digite o código do produto que deseja excluir da lista: "))
            del listas_compras[apagar]
        except IndexError:
            print("Código não existe na lista.")
        except Exception:
            print("Erro desconhecido!")
    
    elif opcao == "L":
        os.system('clear')
        for indice, produto in enumerate(listas_compras):
            print(f'Cód: {indice} - Item: {produto}')

    elif opcao == "F":
        os.system('clear')
        print("A lista foi finalizada com os seguintes items:")
        for indice, produto in enumerate(listas_compras):
            print(f'Cód: {indice} - Item: {produto}')

    else:
        print("Digite uma opção valida! ")

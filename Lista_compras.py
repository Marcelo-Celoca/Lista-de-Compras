lista_compras = []

print("--- LISTA DE COMPRAS ---")

while True:
    print("\nMENU:")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Excluir item")
    print("4 - Sair")

    try:
        # Pegamos a opção e já tentamos converter para número
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            novo_item = input("Adicione um item: ")
            lista_compras.append(novo_item) # Adiciona na lista
            print(f"✅ '{novo_item}' adicionado com sucesso!")

        elif opcao == 2:
            print("\n📋 SUA LISTA DE COMPRAS:")
            if not lista_compras: # Verifica se a lista está vazia
                print("Sua lista está vazia por enquanto.")
            else:
                # O 'for' percorre cada item da lista e mostra um por um
                for i, item in enumerate(lista_compras, start=1):
                    print(f"{i}. {item}")

        elif opcao == 3:
            if not lista_compras:
                print("⚠️ A lista está vazia, não há o que remover.")
            else:
                # Mostramos a lista primeiro para ele escolher o número
                print("\nQual item deseja remover?")
                for i, item in enumerate(lista_compras, start=1):
                    print(f"{i}. {item}")
                
                try:
                    indice = int(input("\nDigite o número do item: "))
                    # Removemos usando o índice - 1 (porque a lista começa em 0)
                    removido = lista_compras.pop(indice - 1)
                    print(f"🗑️ Item '{removido}' removido com sucesso!")
                except (ValueError, IndexError):
                    print("❌ Erro: Posição inválida! Escolha um número que esteja na lista.")

        elif opcao == 4:
            print("Saindo... Até logo!")
            break # Encerra o loop while

        else:
            print("⚠️ Opção inválida! Escolha 1, 2 ou 3.")

    except ValueError:
        # Se o usuário digitar uma letra no menu, o programa cai aqui
        print("❌ Erro: Por favor, digite apenas o número da opção (1, 2, 3 ou 4).")
        

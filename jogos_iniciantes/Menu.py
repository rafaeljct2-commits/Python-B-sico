while True:
    print("\n=== MENU ===")
    print("1 - Calculadora")
    print("2 - Tabuada")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Abrindo calculadora...")
    elif opcao == "2":
        print("Abrindo tabuada...")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

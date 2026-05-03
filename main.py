import funcoes

def menu_principal():
    print("1 - Cadastrar ponto de retirada")
    print("2 - Listar pontos de retirada")
    print("3 - Buscar ponto de retirada por cidade")
    print("4 - Remover ponto de retirada")
    print("5 - Atualizar ponto de retirada")
    print("6 - Sair")


print("Bem-vindo ao sistema de pontos de retirada! \n")

while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")
    print("-"*50)
    if opcao == "1":
        funcoes.cadastrar_ponto()
    elif opcao == "2":
        funcoes.listar_pontos()
    elif opcao == "3":
        funcoes.buscar_ponto_por_cidade()
    elif opcao == "4":
        funcoes.remover_ponto()
    elif opcao == "5":
        funcoes.atualizar_ponto()
    elif opcao == "6":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
    print("-"*50)

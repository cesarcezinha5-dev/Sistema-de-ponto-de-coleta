import json
from viacep import buscar_endereco_por_cep


def cadastrar_ponto():
    nome = input("Digite o nome do ponto de retirada: ")
    cep = input("Digite o CEP do ponto de retirada: ")
    endereco = buscar_endereco_por_cep(cep)
    numero = input("Digite o número do ponto de retirada: ")
    

    if not endereco:
        print("Endereço não encontrado para o CEP informado.")
        return

    ponto = {
    "nome": nome,
    "cep": cep,
    "logradouro": endereco["logradouro"],
    "bairro": endereco["bairro"],
    "cidade": endereco["localidade"],
    "estado": endereco["uf"],
    "numero": numero
}

    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            pontos = json.load(arquivo)
    except FileNotFoundError:
        pontos = []

    pontos.append(ponto)

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(pontos, arquivo, ensure_ascii=False, indent=4)
        print("Ponto de retirada cadastrado com sucesso!")


def listar_pontos():
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            pontos = json.load(arquivo)
            for ponto in pontos:
                print(f"Nome: {ponto['nome']}")
                print(f"Endereço: {ponto['logradouro']}, {ponto['numero']} - {ponto['bairro']}")
                print(f"Cidade: {ponto['cidade']}")
                print(f"Estado: {ponto['estado']}")
                print("-"*50)
    except FileNotFoundError:
        print("Nenhum ponto de retirada cadastrado.")

    
def buscar_ponto_por_cidade():
    cidade = input("Digite a cidade para buscar o ponto de retirada: ")
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            pontos = json.load(arquivo)
            encontrado = False
            for ponto in pontos:
                if ponto["cidade"].lower() == cidade.lower():
                    print(f"Nome: {ponto['nome']}")
                    print(f"Endereço: {ponto['logradouro']}, {ponto['numero']} - {ponto['bairro']}")
                    print(f"Cidade: {ponto['cidade']}")
                    print(f"Estado: {ponto['estado']}")
                    print("-"*50)
                    encontrado = True
            if not encontrado:
                print("Nenhum ponto de retirada encontrado na cidade informada.")
    except FileNotFoundError:
        print("Nenhum ponto de retirada cadastrado.")


def remover_ponto():
    cep = input("Digite o CEP do ponto de retirada a ser removido: ")

    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            pontos = json.load(arquivo)

        quantidade_antes = len(pontos)

        pontos = [ponto for ponto in pontos if ponto["cep"] != cep]

        quantidade_depois = len(pontos)

        if quantidade_antes == quantidade_depois:
            print("Nenhum ponto de retirada encontrado com o CEP informado.")
            return

        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(pontos, arquivo, ensure_ascii=False, indent=4)

        print("Ponto de retirada removido com sucesso!")

    except FileNotFoundError:
        print("Nenhum ponto de retirada cadastrado.")


def atualizar_ponto():
    cep = input("Digite o CEP do ponto de retirada que deseja atualizar: ")
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            pontos = json.load(arquivo)
            for ponto in pontos:
                if ponto["cep"] == cep:
                    nome = input("Digite o novo nome do ponto de retirada: ")
                    numero = input("Digite o novo número do ponto de retirada: ")
                    endereco = buscar_endereco_por_cep(cep)

                    if not endereco:
                        print("Endereço não encontrado para o CEP informado.")
                        return

                    ponto["nome"] = nome
                    ponto["logradouro"] = endereco["logradouro"]
                    ponto["bairro"] = endereco["bairro"]
                    ponto["cidade"] = endereco["localidade"]
                    ponto["estado"] = endereco["uf"]
                    ponto["numero"] = numero
                    break
            else:
                print("Nenhum ponto de retirada encontrado com o CEP informado.")
                return
        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(pontos, arquivo, ensure_ascii=False, indent=4)
            print("Ponto de retirada atualizado com sucesso!")
    except FileNotFoundError:
        print("Nenhum ponto de retirada cadastrado.")

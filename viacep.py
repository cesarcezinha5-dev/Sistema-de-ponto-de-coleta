import requests

def buscar_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" in dados:
            return None

        return dados
    else:
        return None
Descrição

Este projeto é um sistema desenvolvido em Python que simula pontos de retirada (pickup points), semelhante ao funcionamento de marketplaces como Mercado Livre e Shopee.

O sistema permite cadastrar pontos de retirada e preencher automaticamente o endereço através do CEP utilizando a API pública ViaCEP.

Funcionalidades
Cadastrar ponto de retirada
Listar pontos cadastrados
Buscar pontos por cidade
Atualizar dados de um ponto
Remover ponto
Armazenamento em arquivo JSON
Tecnologias utilizadas
Python
requests (consumo de API)
JSON (persistência de dados)
Como funciona a integração com ViaCEP

Ao informar o CEP, o sistema consulta a API ViaCEP e retorna automaticamente:

Logradouro
Bairro
Cidade
Estado (UF)

Observações
Os pontos cadastrados são fictícios e servem apenas para simulação, mas os CEPs utilizados podem ser reais para garantir o retorno correto da API.
